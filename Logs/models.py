from django.db import models
from Users.models import Student, Professor

# Create your models here.

class ProfLog(models.Model):
    _student = models.ForeignKey(Student)
    _professor = models.ForeignKey(Professor)
    _like = models.BooleanField(default = False)
    _dislike = models.BooleanField(default = False)
    _dont_know = models.BooleanField(default = False)
    def __str__(self):
        return self._student.get_name() + "-" + self._professor.get_name()
    def get_like(self):
        return str(self._like)
    def get_dislike(self):
        return str(self._dislike)
    def get_dont_know(self):
        return str(self._dont_know)
    def update_like(self,like):
        self._like = like
    def update_dislike(self,dislike):
        self._dislike = dislike
    def update_dont_know(self,dont_know):
        self._dont_know = dont_know
    def is_valid_log(self):
        if self._like == True:
            if self._dislike == True :
                return False
            if self._dont_know == True:
                return False
        elif self._dislike == True:
            if self.get_dont_know == False:
                return False
        else:
            return True