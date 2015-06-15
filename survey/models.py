from django.db import models
from Users.models import DEFAULT_FIELD_VALUE
from Reviews.models import MAX_LENGTH_OF_REVIEW

# Create your models here.

class OtherDetails(models.Model):
    _email = models.EmailField(null=False,default=DEFAULT_FIELD_VALUE,primary_key=True)
    _job_satisfaction = models.CharField(max_length=MAX_LENGTH_OF_REVIEW)
    _research_avenues = models.CharField(max_length=MAX_LENGTH_OF_REVIEW)
    _job_satisfaction_rate = models.CharField(max_length=10)
    _research_avenues_rate = models.CharField(max_length=10)
    _college_review_rate = models.CharField(max_length=10)
    def __str__(self):
        return self._email
    def get_job_satisfaction(self):
        return self._job_satisfaction
    def get_reseach_avvenues(self):
        return self._research_avenues