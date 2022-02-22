from django.db import models


SEX_CHOICES = [
    ('Ж', 'женский'),
    ('М', 'мужской')
]

STATUS_CHOICES = [
    ('Обычный', 'Обычный'),
    ('Привилегированный', 'Привилегированный'),
    ('VIP', 'VIP')
]

class Client(models.Model):
    status = models.CharField(max_length=255, choices=STATUS_CHOICES)
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=255, choices=SEX_CHOICES)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)


    class Meta:
        managed = False
        db_table = 'client'

    def __str__(self):
        return self.surname


class Russian_passport(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    passport_series = models.IntegerField(max_length=11)
    passport_number = models.IntegerField(max_length=11)
    date_of_issue = models.DateField()
    expiration_date = models.DateField()
    issuing_authority = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'russian_passport'

    def __str__(self):
        return self.client


class International_passport(models.Model):
    client = models.ForeignKey(Client, models.DO_NOTHING, db_column='client')
    country_code = models.CharField(max_length=255)
    passport_number = models.IntegerField(max_length=11)
    nationality = models.CharField(max_length=255)
    issuing_authority = models.CharField(max_length=255)
    date_of_issue = models.DateField()
    expiration_date = models.DateField()
    
    class Meta:
        managed = False
        db_table = 'international_passport'

    def __str__(self):
        return self.client
