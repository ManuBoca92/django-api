from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __unicode__(self):
        return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)
