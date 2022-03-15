from django.db import models
from employees.models import Organization, Employee
from clients.models import Client


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country_name


class City(models.Model):
    country = models.ForeignKey(Country, models.DO_NOTHING, db_column='country')
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'city'

    def __str__(self):
        return self.city_name


class Preliminary_agreement(models.Model):
    date_of_agreement = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    employee = models.ForeignKey(Employee, models.DO_NOTHING, db_column='employee')
    country_of_visit = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_of_visit')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    number_of_trip_members = models.IntegerField(max_length=11)
    start_date_of_trip = models.DateField()
    end_date_of_trip = models.DateField()

    class Meta:
        managed = False
        db_table = 'preliminary_agreement'

    def __str__(self):
        return self.date_of_agreement


class Visiting_city(models.Model):
    preliminary_agreement = models.ForeignKey(Preliminary_agreement, models.DO_NOTHING, db_column='preliminary_agreement')
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')

    class Meta:
        managed = False
        db_table = 'visiting_city'

    def __str__(self):
        return self.preliminary_agreement