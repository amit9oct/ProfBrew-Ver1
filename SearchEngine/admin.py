from django.contrib import admin
from SearchEngine.models import SearchMadeByProfessor, SearchMadeByStudent,\
    SearchMadeByVisitor

admin.site.register(SearchMadeByProfessor)
admin.site.register(SearchMadeByStudent)
admin.site.register(SearchMadeByVisitor)
