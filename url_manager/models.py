#coding: utf-8

from django.db import models
from django.contrib import admin

ERROR_MSG = {
            0: "data error",
            1: "it is not a url",
            2: "url creation error",
            3: "there is no such a url",
        }

class WrongURL(Exception):
    def __init__(self, key):
        self.error_message = ERROR_MSG[key]

    def __str__(self):
        return self.error_message

    def __unicode__(self):
        return self.error_message

class LongURL(models.Model):
    url = models.URLField(unique=True)

    def __unicode__(self):
        return self.url

class ShortURL(models.Model):
    id = models.CharField(max_length=128, primary_key=True)
    longUrl = models.OneToOneField(LongURL)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ['-id']

class LongURLAdmin(admin.ModelAdmin):
    list_display = ('url',)

class ShortURLAdmin(admin.ModelAdmin):
    list_display = ('id', 'longUrl',)

admin.site.register(LongURL, LongURLAdmin)
admin.site.register(ShortURL, ShortURLAdmin)

