import requests
import datetime
import pytz
from api.models import Story
from topper.updater.updater import Updater
from django.db import transaction


class HackerNewsUpdater(Updater):

    MAX_STORIES = 100

    def __init__(self):
        super().__init__('Hacker News')

    @transaction.atomic
    def update(self):
        endpoint = 'https://hacker-news.firebaseio.com/v0/topstories.json'
        resp = requests.get(endpoint)
        story_ids = resp.json()
        stories = 0
        for idx, id in enumerate(story_ids):
            if stories > self.MAX_STORIES:
                break
            resp = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{id}.json')
            data = resp.json()

            if data['type'] != 'story':
                continue

            stories += 1
            story, created = Story.objects.get_or_create(service=self.service, code=id)

            story.title = data['title']
            story.comments = data['descendants']
            story.comments_url = f"{self.service.url}/item?id={id}"

            story.story_date = datetime.datetime.utcfromtimestamp(data['time']).replace(tzinfo=pytz.UTC)

            story.score = data['score']

            if 'url' not in data:
                story.url = story.comments_url
            else:
                story.url = data['url']

            self.save(story, created)

