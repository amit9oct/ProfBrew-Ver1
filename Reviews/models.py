from django.db import models
from Users.models import Professor,Student,DEFAULT_FIELD_VALUE,College,Branch
from django.utils import timezone
# Create your models here.
MAX_LENGTH_OF_REVIEW = 2000


class Likes(models.Model):
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE)
    class Meta:
        abstract = True
    def get_student(self):
        return self._student
        
class Reviews(models.Model):
    """
    Abstract class for inheritance in professor, college and branch review class
    """
    _review = models.CharField(max_length=MAX_LENGTH_OF_REVIEW,default=DEFAULT_FIELD_VALUE,null=True)
    _number_of_likes = models.IntegerField(default=0)
    _date_time = models.DateTimeField(null=False,default=timezone.now())
    def get_timestamp(self):
        return str(self._date_time)
    def get_number_of_likes(self):
        return self._number_of_likes
    def get_review(self):
        return self._review
    def update_review(self,review):
        self._review = review
    def update_number_of_likes(self,number_of_likes):
        self._number_of_likes = number_of_likes 
    class Meta:
        abstract = True
        
class ProfessorReviews(Reviews):
    """
    _professor = Foreign key established with Professor class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._professor)+'-'+str(self._student)
    _professor = models.ForeignKey(Professor,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)
    def get_professor(self):
        return self._professor
    def get_student(self):
        return self._student
    
class CollegeReviews(Reviews):
    """
    _college = Foreign key established with College class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._college)+'-'+str(self._student)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)
    def get_college(self):
        return self._college
    def get_student(self):
        return self._student

class BranchReviews(Reviews):
    """
    _branch = Foreign key established with Branch class in app Users
    _student = Foreign key established with Student class in app Users
    """
    def __str__(self):    
        return str(self._branch)+'-'+str(self._student)
    _branch = models.ForeignKey(Branch,default=DEFAULT_FIELD_VALUE,null=False)
    _college = models.ForeignKey(College,default=DEFAULT_FIELD_VALUE,null=False)
    _student = models.ForeignKey(Student,default=DEFAULT_FIELD_VALUE,null=False)
    def get_branch(self):
        return self._branch
    def get_college(self):
        return self._college
    def get_student(self):
        return self._student
    
class ProfessorReviewLikes(Likes):
    _review = models.ForeignKey(ProfessorReviews,default=DEFAULT_FIELD_VALUE)
    _liked = models.BooleanField(default = False)
    _disliked = models.BooleanField(default = False)
    def __str__(self):
        return str(self._review.get_student())+' and '+str(self._student)
    def get_review(self):
        return self._review
    def has_liked(self):
        return self._liked
    def has_disliked(self):
        return self._disliked
    def update_liked(self,like):
        self._liked=like
    def update_disliked(self,dislike):
        self._disliked=dislike