from django.http.response import HttpResponse
from Users.models import Professor,Branch
from Ratings.models import ProfRatings
from django.shortcuts import render



def search(request):
    raw_text_by_user = request.GET['txtSearch']
    search_type = request.GET['search_type']
    request.session['last_url'] = '/search/?txtSearch='+raw_text_by_user+'&search_type=Professor'
    if search_type == 'Professor':
        prof_list = Professor.objects.filter(name__icontains = raw_text_by_user)
        len_of_prof_list = len(prof_list)
        i=0
        prof_rate_complete_list = []
        while i<len_of_prof_list:
            prof_rate_list = ProfRatings.objects.filter(_prof = prof_list[i])
            prof_rate_complete_list.append(prof_rate_list[0])
            i += 1
        prof_rate_complete_list.sort(key=lambda x: x.get_rate(), reverse=True)
        count = len(prof_rate_complete_list)
        context = {'prof_rate_list': prof_rate_complete_list,'number_of_search_result': count}
        return render(request,'search/home.html',context)

def branch_search(request):
    raw_text_by_user = request.GET['branch']
    branch_object = Branch.objects.filter(_branch_name=raw_text_by_user)
    prof_list = Professor.objects.filter(_branch = branch_object[0])
    len_of_prof_list = len(prof_list)
    i=0
    prof_rate_complete_list = []
    while i<len_of_prof_list:
        prof_rate_list = ProfRatings.objects.filter(_prof = prof_list[i])
        prof_rate_complete_list.append(prof_rate_list[0])
        i += 1
    prof_rate_complete_list.sort(key=lambda x: x.get_rate(), reverse=True)
    count = len(prof_rate_complete_list)
    context = {'prof_rate_list': prof_rate_complete_list,'number_of_search_result': count}
    return render(request,'search/home.html',context)

def load_branch(request):
    branch_list = Branch.objects.all()
    context = {'branch_list':branch_list}
    return render(request,'search/branch.html',context)
