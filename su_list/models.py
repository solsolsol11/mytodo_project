from django.db import models

from accounts.models import User


class Sulist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serious_no_urgent = models.TextField('중요and안급함', null=True)
    serious_yes_urgent = models.TextField('중요and급함', null=True)
    no_serious_no_urgent = models.TextField('안중요and안급함', null=True)
    no_serious_yes_urgent = models.TextField('안중요and급함', null=True)


