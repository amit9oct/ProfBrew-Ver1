from django.contrib import admin
from Users.models import Student,Professor,Prof_Position,Qualification_Type,Branch,Course

admin.site.register(Qualification_Type)
admin.site.register(Prof_Position)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Branch)
admin.site.register(Course)