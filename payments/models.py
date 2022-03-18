from django.db import models
from contracts.models import Contract


class Currency(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    rate = models.FloatField()

    class Meta:
        managed = False
        db_table = 'currency'

    def __str__(self):
        return self.code



class Payment(models.Model):
    payment_date = models.DateTimeField(auto_now_add=True)
    organization = models.IntegerField()
    contract = models.ForeignKey(Contract, models.DO_NOTHING, db_column='contract')
    amount_in_rubles = models.IntegerField()
    currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='currency', null=True)

    class Meta:
        managed = False
        db_table = 'payment'

    def __str__(self):
        return str(self.payment_date)

