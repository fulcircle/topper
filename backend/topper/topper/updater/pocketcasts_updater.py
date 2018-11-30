import requests
from topper.models import Podcast
from django.conf import settings
from topper.updater.updater import Updater
from django.db import transaction


class PocketCastsUpdater(Updater):

    MAX_PODCASTS = 100

    def __init__(self):
        super().__init__('Pocketcasts')
        self.token = None

        self._username = settings.POCKET_CASTS['username']
        self._password = settings.POCKET_CASTS['password']

        self._session = requests.Session()
        self.token = self._login()

    def _login(self):
        login_url = "https://api.pocketcasts.com/user/login"
        data = {"email": self._username, "password": self._password, "scope": "webplayer"}
        attempt = self._make_req(login_url, data=data)

        return attempt.json()['token']

    def _make_req(self, url, method='GET', data=None):
        if method == 'JSON':
            req = requests.Request('POST', url, json=data, cookies=self._session.cookies)
        elif method == 'POST' or data:
            req = requests.Request('POST', url, data=data, cookies=self._session.cookies)
        elif method == 'GET':
            req = requests.Request('GET', url, cookies=self._session.cookies)
        else:
            raise Exception("Invalid method")

        if self.token:
            req.headers['Authorization'] = f"Bearer {self.token}"

        prepped = req.prepare()
        return self._session.send(prepped)

    def _get_share_url(self, podcastId, id):
        resp = self._make_req('https://api.pocketcasts.com/podcasts/share_link', 'JSON', data={'episode': id, 'podcast': podcastId})
        return resp.json()['url']

    @transaction.atomic
    def update(self):
        attempt = self._make_req('https://api.pocketcasts.com/user/new_releases', method='POST')

        podcasts = 0
        for episode in attempt.json()['episodes']:
            if podcasts > self.MAX_PODCASTS:
                break

            podcasts += 1
            podcast, created = Podcast.objects.get_or_create(service=self.service, code=episode['uuid'])
            podcast.title = episode['title']
            podcast.category = episode['podcastTitle']
            podcast.duration = episode['duration']
            podcast.story_date = episode['published']
            podcast.podcastId = episode['podcastUuid']
            podcast.url = self._get_share_url(episode['podcastUuid'], episode['uuid'])

            self.save(podcast, created)

