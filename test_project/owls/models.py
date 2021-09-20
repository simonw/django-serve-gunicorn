from django.db import models


class Owl(models.Model):
    ioc_sequence = models.IntegerField()
    common_name = models.CharField(max_length=64)
    binomial_name = models.CharField(max_length=64)

    def __str__(self):
        return self.common_name
