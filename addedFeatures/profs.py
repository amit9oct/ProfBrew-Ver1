from django.http.response import HttpResponse
from Users.models import Professor,Branch
from Ratings.models import ProfRatings
from django.shortcuts import render

def get_top_prof_rate():
    prof_list = Professor.objects.filter(name__icontains = '')
    len_of_prof_list = len(prof_list)
    i=0
    prof_rate_complete_list = []
    while i<len_of_prof_list:
        prof_rate_list = ProfRatings.objects.filter(_prof = prof_list[i])
        prof_rate_complete_list.append(prof_rate_list[0])
        i += 1
    prof_rate_complete_list.sort(key=lambda x: x.get_rate(), reverse=True)
    count = len(prof_rate_complete_list)
    return prof_rate_complete_list[0]
