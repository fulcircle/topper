from django.db import models


class Service(models.Model):
    GOOD = 'G'
    ERROR = 'E'
    RETRIEVING = 'R'

    CURRENT_STATUS = (
        (GOOD, u'✓ good'),
        (ERROR, u'× error'),
        (RETRIEVING, u'~ running')
    )

    name = models.CharField(max_length=255)
    url = models.URLField()
    last_run = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=1, default=GOOD, choices=CURRENT_STATUS)

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Story(models.Model):
    NEW = 'N'
    OK = 'O'
    ERROR = 'E'
    STATUS = (
        (NEW, 'New'),
        (OK, 'Ok'),
        (ERROR, 'Error'),
    )

    service = models.ForeignKey(Service, related_name='stories', on_delete=models.CASCADE)
    code = models.CharField(max_length=255)
    title = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=2000, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    comments = models.IntegerField(default=0)
    comments_url = models.URLField(max_length=2000, null=True, blank=True)
    score = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True, db_index=True)
    story_date = models.DateTimeField(null=True)
    status = models.CharField(max_length=1, default=NEW, choices=STATUS)
    top_ten = models.BooleanField(default=False)
    description = models.CharField(max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = 'story'
        verbose_name_plural = 'stories'
        unique_together = (('service', 'code', 'date'),)
        ordering = ('-score', 'date')

    def __unicode__(self):
        return self.code


class SubredditStory(Story):

    subreddit = models.CharField(max_length=255)


class Podcast(Story):

    duration = models.IntegerField(default=0)
    podcastId = models.CharField(max_length=200)

