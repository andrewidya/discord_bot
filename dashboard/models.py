from django.db import models

# Create your models here.
class Platform(models.Model):
    name = models.CharField(verbose_name="Name", max_length=60)

    class Meta:
        verbose_name = "Platform"
        verbose_name_plural = "Platforms"

    def __str__(self):
        return self.name


class SeriesTitle(models.Model):
    name = models.CharField(verbose_name="Name", max_length=60)

    class Meta:
        verbose_name = "Series Title"
        verbose_name_plural = "Series Titles"

    def __str__(self):
        return self.name


class Weapon(models.Model):
    name = models.CharField(verbose_name="Name", max_length=60)

    class Meta:
        verbose_name = "Weapon"
        verbose_name_plural = "Weapons"

    def __str__(self):
        return self.name


class Monster(models.Model):
    name = models.CharField(verbose_name="Name", max_length=60)

    class Meta:
        verbose_name = "Monster"
        verbose_name_plural = "Monsters"

    def __str__(self):
        return self.name


class PlatformReleasedSeries(models.Model):
    series_name = models.ForeignKey(
        SeriesTitle, verbose_name="Series Title", on_delete=models.CASCADE)
    platform = models.ForeignKey(
        Platform, verbose_name="Platform", on_delete=models.CASCADE)

    def __str__(self):
        return self.series_name + ":" + self.platform


class MonsterHunterDatabase(models.Model):
    name = models.ForeignKey(
        SeriesTitle, verbose_name="Series Name", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Monster Hunter Database"
        verbose_name_plural = "Monster Hunter Databases"

    def __str__(self):
        return self.name


class SeriesWeapon(models.Model):
    series_name = models.ForeignKey(
        MonsterHunterDatabase, verbose_name="Series Name", on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        Weapon, verbose_name="Weapon", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Available Weapon"
        verbose_name_plural = "Available Weapons"

    def __str__(self):
        return self.series_name + ":" + self.weapon


class SeriesMonster(models.Model):
    series_name = models.ForeignKey(
        MonsterHunterDatabase, verbose_name="Series Name", on_delete=models.CASCADE)
    monster = models.ForeignKey(
        Monster, verbose_name="Monster", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Available Monster"
        verbose_name_plural = "Available Monsters"

    def __str__(self):
        return self.series_name + ":" + self.monster
