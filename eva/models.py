from django.db import models
from django.urls import reverse
from django.conf import settings
import datetime
import uuid


class Work(models.Model):
    """Model representing a book of Work"""
    workName = models.CharField(max_length=30, null=False)
    author = models.CharField(max_length=10, null=True)
    pageNum = models.IntegerField(null=False)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this work."""
        return reverse('work-detail', args=[str(self.id)])

    def __str__(self):
        return self.workName


class Page(models.Model):
    wordCount = models.IntegerField(null=False)
    rowCount = models.IntegerField(null=False)
    colCount = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    workId = models.ForeignKey('Work', null=True, on_delete=models.SET_NULL)
    num = models.IntegerField(null=False, help_text='The page number in the work.')
    url = models.CharField(max_length=100, help_text='This is the relative'
                                                     'path for the pic.',
                           null=False)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this page."""
        return reverse('page-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.workId) + ' p. ' + str(self.num)


class Word(models.Model):
    width = models.IntegerField(null=False)
    height = models.IntegerField(null=False)
    x1 = models.IntegerField(null=False, help_text='The x coordinate of '
                                                   'upper-left point')
    y1 = models.IntegerField(null=False, help_text='The y coordinate of '
                                                   'upper-left point')
    y2 = models.IntegerField(null=False, help_text='The y coordinate of '
                                                   'lower-right point')
    x2 = models.IntegerField(null=False, help_text='The x coordinate of '
                                                   'lower-right point')
    coreX = models.IntegerField(null=False)
    coreY = models.IntegerField(null=False)
    pageId = models.ForeignKey('Page', on_delete=models.SET_NULL, null=True)
    num = models.IntegerField(null=False)

    def __str__(self):
        return str(self.pageId) + ' w. ' + str(self.num)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this word."""
        return reverse('word-detail', args=[str(self.id)])


class Radical(models.Model):
    wordId = models.ForeignKey('Word', on_delete=models.SET_NULL, null=True)
    url = models.CharField(max_length=100, help_text='This is the relative'
                                                     'path for the pic.',
                           null=False)
    num = models.IntegerField(null=False)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this radical."""
        return reverse('radical-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.wordId) + ' r. ' + str(self.id)


def file_rename(instance, filename):
    ext = filename.split('.')[-1]
    x = datetime.datetime.now()
    # Using UUID4 to generate unique file name and path [YYYY/MM/DD/uuid_file_name.extension]
    file_name = '/'.join([x.strftime("%Y"), x.strftime("%m"), x.strftime("%d"), str(uuid.uuid4())])
    file_name = "%s.%s" % (file_name, ext)
    return file_name


class File(models.Model):
    file = models.FileField(blank=False, null=False, upload_to=file_rename)

    def __str__(self):
        return self.file.name


class UserRecord(models.Model):
    """This model is to record the evaluation results of the work that users upload."""
    userId = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(null=False)
    review = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=150)

    def get_absolute_url(self):
        """Returns the url to access a detail record for this radical."""
        return reverse('record-detail', args=[str(self.id)])

    def __str__(self):
        return str(self.userId) + ' r. ' + str(self.id)
