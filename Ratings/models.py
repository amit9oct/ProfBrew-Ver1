from django.db import models
from Users.models import Professor,DEFAULT_FIELD_VALUE


MAX_LEN_OF_COMMENTS=1000
WT_OF_LIKES = 0.5
WT_OF_QUALIFICATIONS = 0.5
WT_OF_COMMENTS = 0.5 

    
class Ratings(models.Model):
    """
    Ratings()-
        _no_of_likes -> number of likes the prof/college has
        _no_of_dislikes -> number of dislikes the prof/college has
    """
    _number_of_likes = models.BigIntegerField(null=False,default=0)
    _number_of_dislikes = models.BigIntegerField(null=False,default=0)
    _rate = models.FloatField(null=False,default=0)
    def get_total_likes(self):
        return self._number_of_likes-self._number_of_dislikes
    def likes(self):
        self._number_of_likes += 1
    def dislikes(self):
        self._number_of_dislikes += 1
    def get_likes(self):
        return self._number_of_likes
    def get_dislikes(self):
        return self._number_of_dislikes
    def get_rate(self):
        return self._rate
    def update_likes(self,likes):
        self._number_of_likes = likes
    def update_dislikes(self,dislikes):
        self._number_of_dislikes = dislikes
    class Meta:
        abstract=True

class ProfRatings(Ratings):
    """
    ProfRatings()-
        _prof -> Professor to be rated
    """
    _prof = models.ForeignKey(Professor,null=False,default=DEFAULT_FIELD_VALUE)
    def __str__(self):
        self.assign_rate()
        self.save()
        return self._prof.name+'-'+str(self._rate)
    def assign_rate(self):
        self._rate=WT_OF_LIKES*self.get_total_likes()+WT_OF_QUALIFICATIONS*self._prof.get_number_of_qualifications()
    def get_prof(self):
        return self._prof