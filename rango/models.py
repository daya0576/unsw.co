# coding: UTF-8

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
from django.conf import settings
from DjangoUeditor.commands import UEditorButtonCommand,UEditorComboCommand
from DjangoUeditor.commands import UEditorEventHandler


class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True)
    school_cn = models.CharField(max_length=100, blank=True)
    school_en = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True)
    url = models.URLField()

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subject, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    no = models.CharField(max_length=20)
    name = models.CharField(max_length=50, unique=True)
    level = models.IntegerField(default=0)

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    url = models.URLField()
    description = models.CharField(max_length=128)

    subject = models.ForeignKey(Subject)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class CatPage(models.Model):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category)
    url = models.URLField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class SubPage(models.Model):
    title = models.CharField(max_length=128)
    subject = models.ForeignKey(Subject)
    url = models.URLField()
    views = models.IntegerField(default=0)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.title


class BaiduEditor(models.Model):
    # title = models.CharField(max_length=100, blank=True, )
    content = UEditorField(u'', width='100%', height=300,
                     toolbars="full",
                     imagePath='Comment_images/%(basename)s_%(datetime)s.%(extname)s',
                     filePath='Comment_files/%(basename)s_%(datetime)s.%(extname)s',
                     upload_settings={
                         "imageMaxSize": 1204000},
                     settings={},
                     command=None,
                     # event_handler=myEventHander(),
                     blank=True)


class Answers(models.Model):
    category = models.ForeignKey(Category)
    author = models.ForeignKey(User)
    content = models.CharField(max_length=10000, blank=True)
    post_date = models.DateTimeField()
    edit_date = models.DateTimeField()
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.content


class CategoryUserLikes(models.Model):
    category = models.ForeignKey(Category)
    user = models.ForeignKey(User)

