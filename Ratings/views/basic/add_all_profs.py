'''
Created on Mar 7, 2015

@author: Amitayush Thakur
'''
from Users.models import Professor
from Ratings.models import ProfRatings
from django.http.response import HttpResponse

def add_all_profs(request):
    prof_list = Professor.objects.all()
    for prof in prof_list:
        prof_rate_list_number = ProfRatings.objects.filter(_prof=prof).count()
        if prof_rate_list_number == 0:
            ProfRatings.objects.create(_prof=prof)
    return HttpResponse("All professor added!!")