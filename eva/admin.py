from django.contrib import admin
from .models import Work, Page, Word, Radical, File, UserRecord


class PageInline(admin.TabularInline):
    model = Page
    extra = 1


class WordInline(admin.TabularInline):
    model = Word
    extra = 1


class RadicalInline(admin.TabularInline):
    model = Radical
    extra = 1


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('workName', 'author')
    list_filter = ['author']
    inlines = [PageInline]


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('workId', 'num')
    list_filter = ['workId']
    fieldsets = (
        ('Basic Information', {
            'fields': (('wordCount', 'rowCount', 'colCount'), ('width', 'height'))
        }),
        ('Details', {
            'fields': (('workId', 'num'), 'url')
        }),
    )
    inlines = [WordInline]


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('pageId', 'num')
    list_filter = ['pageId']
    fieldsets = (
        ('Basic Information', {
            'fields': (('pageId', 'num'), ('width', 'height'))
        }),
        ('Coordinates', {
            'fields': (('x1', 'y1'), ('x2', 'y2'), ('coreX', 'coreY'))
        }),
    )
    inlines = [RadicalInline]


@admin.register(Radical)
class RadicalAdmin(admin.ModelAdmin):
    list_display = ('wordId', 'num')
    list_filter = ['wordId']


@admin.register(UserRecord)
class UserRecordAdmin(admin.ModelAdmin):
    list_display = ('userId', 'score')
    list_filter = ['userId']


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ['file']
