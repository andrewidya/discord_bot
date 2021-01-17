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
    aliases = models.CharField(
        verbose_name="Game Name Aliases", max_length=140, null=True, blank=True)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    platform = models.ManyToManyField(
        Platform, through="PlatformReleasedSeries", verbose_name="Platforms")

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
    series = models.ForeignKey(
        SeriesTitle, verbose_name="Series Title", on_delete=models.CASCADE)
    platform = models.ForeignKey(
        Platform, verbose_name="Platform", on_delete=models.CASCADE)

    def __str__(self):
        return self.series.name + ":" + self.platform.name


class MonsterHunterDatabase(models.Model):
    series = models.OneToOneField(
        SeriesTitle, verbose_name="Series Name", on_delete=models.CASCADE)
    discord_channel = models.CharField(verbose_name="Discord Channel", max_length=60)

    class Meta:
        verbose_name = "Monster Hunter Database"
        verbose_name_plural = "Monster Hunter Databases"

    def __str__(self):
        return self.series.name


class SeriesWeapon(models.Model):
    group = models.ForeignKey(
        MonsterHunterDatabase, verbose_name="Series Name", on_delete=models.CASCADE)
    weapon = models.ForeignKey(
        Weapon, verbose_name="Weapon", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Available Weapon"
        verbose_name_plural = "Available Weapons"

    def __str__(self):
        return self.group.series.name + ":" + self.weapon.name


class SeriesMonster(models.Model):
    group = models.ForeignKey(
        MonsterHunterDatabase, verbose_name="Series Name", on_delete=models.CASCADE)
    monster = models.ForeignKey(
        Monster, verbose_name="Monster", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Available Monster"
        verbose_name_plural = "Available Monsters"

    def __str__(self):
        return self.group.series.name + ":" + self.monster.name


class AdditionalProperties(models.Model):
    GROUPING = {
        ('style', 'Style'),
        ('other', 'Other')
    }

    group = models.ForeignKey(
        MonsterHunterDatabase, verbose_name="Series Name", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Name", max_length=60)
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    prop_grouping = models.CharField(
        verbose_name="Label", max_length=20, choices=GROUPING)

    class Meta:
        verbose_name = "Additional Properties"
        verbose_name_plural = "Additional Properties"

    def __str__(self):
        return self.group.series.name + ":" + self.name + ":" + self.prop_grouping
    