from django.contrib import admin

from dashboard.models import (
    Platform, SeriesTitle, Weapon, Monster, PlatformReleasedSeries,
    MonsterHunterDatabase, SeriesWeapon, SeriesMonster)

# Register your models here.
@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    pass


class PlatformReleasedSeriesInlineAdmin(admin.TabularInline):
    model = PlatformReleasedSeries


@admin.register(SeriesTitle)
class SeriesTitleAdmin(admin.ModelAdmin):
    inlines = [PlatformReleasedSeriesInlineAdmin]


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class SeriesWeaponInlineAdmin(admin.TabularInline):
    model = SeriesWeapon
    autocomplete_fields = ['weapon']
    extra = 0
    suit_classes = 'suit-tab suit-tab-series_weapon'


class SeriesMonsterInlineAdmin(admin.TabularInline):
    model = SeriesMonster
    autocomplete_fields = ['monster']
    extra = 0
    suit_classes = 'suit-tab suit-tab-series_monster'


@admin.register(MonsterHunterDatabase)
class MonsterHunterDatabaseAdmin(admin.ModelAdmin):
    list_display = ['series', 'discord_channel']
    inlines = [SeriesWeaponInlineAdmin, SeriesMonsterInlineAdmin]
    fieldsets = [
        ('Series Title', {
            'classes': 'suit-tab suit-tab-series_title',
            'fields': ['series', 'discord_channel']
        })
    ]

    suit_form_tabs = (
        ('series_title', 'Series Title'), ('series_weapon', 'Weapons'),
        ('series_monster', 'Monsters'))
