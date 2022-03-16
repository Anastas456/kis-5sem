from django.db import models
from preliminary_agreements.models import Preliminary_agreement, City
from clients.models import Client


STARS_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('апартаменты', 'апартаменты')
]
NUTRITION_CHOICES = [
    ('RO', 'RO'),
    ('BB', 'BB'),
    ('HB', 'HB'),
    ('FB', 'FB'),
    ('AI', 'AI'),
    ('UAI', 'UAI')
]


class Contract(models.Model):
    contract_date = models.DateTimeField(auto_now_add=True)
    preliminary_agreement = models.ForeignKey(Preliminary_agreement, models.DO_NOTHING, db_column='preliminary_agreement')
    organization = models.IntegerField(max_length=11)
    agent = models.IntegerField(max_length=11)
    client = models.IntegerField(max_length=11)
    start_date_of_trip = models.DateField()
    end_date_of_trip = models.DateField()

    class Meta:
        managed = False
        db_table = 'contract'

    def __str__(self):
        return str(self.contract_date)


class Trip_member(models.Model):
    contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='contract')
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')

    class Meta:
        managed = False
        db_table = 'trip_member'

    def __str__(self):
        return str(self.contract) 


class Hotel(models.Model):
    city = models.ForeignKey(City, models.DO_NOTHING, db_column='city')
    hotel_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_stars = models.CharField(choices=STARS_CHOICES, max_length=255)

    class Meta:
        managed = False
        db_table = 'hotel'

    def __str__(self):
        return self.hotel_name


class Hotel_reservation(models.Model):
    hotel = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotel')
    room_type = models.CharField(max_length=255)
    nutrition = models.CharField(choices=NUTRITION_CHOICES, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'hotel_reservation'

    def __str__(self):
        return str(self.hotel)


class Route(models.Model):
    contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='contract')
    hotel_reservation = models.ForeignKey(Hotel_reservation, models.DO_NOTHING, db_column='hotel_reservation')

    class Meta:
        managed = False
        db_table = 'route'

    def __str__(self):
        return str(self.contract)