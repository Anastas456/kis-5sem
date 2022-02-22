from django.db import models


POSITION_CHOICES = [
    ('Менеджер', 'Менеджер'),
    ('Агент', 'Агент'),
    ('Администратор', 'Администратор'),
    ('Бухгалтер', 'Бухгалтер')
]


class Organization(models.Model):
    organization_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'organization'

    def __str__(self):
        return self.organization_name



class Employee(models.Model):
    organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='organization')
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, choices=POSITION_CHOICES)
    date_of_birth = models.DateField()
    photo = models.ImageField(blank=True, null=True)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee'

    def __str__(self):
        return str(self.surname + ' ' + self.name)


