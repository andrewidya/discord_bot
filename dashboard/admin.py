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
    pass


@admin.register(Monster)
class MonsterAdmin(admin.ModelAdmin):
    pass


class SeriesWeaponInlineAdmin(admin.TabularInline):
    model = SeriesWeapon


class SeriesMonsterInlineAdmin(admin.TabularInline):
    model = SeriesMonster


@admin.register(MonsterHunterDatabase)
class MonsterHunterDatabaseAdmin(admin.ModelAdmin):
    inlines = [SeriesWeaponInlineAdmin, SeriesMonsterInlineAdmin]
