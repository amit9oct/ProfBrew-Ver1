from django.db import models
from django.utils import timezone
from Users.models import Professor, Student


MAX_LEN_OF_SEARCH_KEYWORD = 200

class Search(models.Model):
    BY_COLLEGE = 1
    BY_BRANCH = 2
    BY_PROFESSOR = 3
    SEARCH_TYPE = ((BY_COLLEGE,'Search by College'),(BY_PROFESSOR,'Search by Professor'),(BY_COLLEGE,'Search by College'),)
    _search_type = models.IntegerField(choices=SEARCH_TYPE)
    _search_key_word = models.CharField(max_length = MAX_LEN_OF_SEARCH_KEYWORD)
    _time = models.DateTimeField(null=False,default=timezone.now())
    
class SearchMadeByProfessor(Search):
    _user = models.ForeignKey(Professor, null=False)
    def __str__(self):
        return str(self._user)+self._search_key_word

class SearchMadeByStudent(Search):
    _user = models.ForeignKey(Student, null=False)
    def __str__(self):
        return str(self._user)+self._search_key_word
    
class SearchMadeByVisitor(Search):
    _user = models.IPAddressField(null=False)
    def __str__(self):
        return str(self._user)+self._search_key_word    
