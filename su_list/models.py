from django.db import models

from accounts.models import User



# 중요하지만 급하지 않아 리스트 모델
class SeriousNoUrgentList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serious_no_urgent = models.TextField('중요and안급함', null=True)



# 중요하고 급해 리스트 모델
class SeriousYesUrgentList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serious_yes_urgent = models.TextField('중요and급함', null=True)


# 중요하지도 않고 급하지도 않아 리스트 모델
class NoSeriousNoUrgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_serious_no_urgent = models.TextField('안중요and안급함', null=True)


# 중요하진 않은데 급해 리스트 모델
class NoSeriousYesUrgent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    no_serious_yes_urgent = models.TextField('안중요and급함', null=True)


