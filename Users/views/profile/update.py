from django.http.response import HttpResponseBadRequest
from Users.models import Student
from django.shortcuts import render
from University.models import College
from ProfBrew.urls import INTERNAL
import Users.views

def update(request):
    username = request.session['username']
    usertype = request.session['user_type']
    if request.method == 'GET':
        return HttpResponseBadRequest
    elif request.method == 'POST':
        if usertype == 'Student':
            if 'textName' in request.POST:
                Student.objects.filter(_username=username).update(name=request.POST['textName'])
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request)
            if 'textEmail' in request.POST:
                Student.objects.filter(_username=username).update(_email=request.POST['textEmail'])
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request) 
            if 'textPhone' in request.POST:
                Student.objects.filter(_username=username).update(_mobile_number=request.POST['textPhone'])
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request) 
            if 'sltCollege' in request.POST:
                clg = College.objects.filter(college_name=request.POST['sltCollege'])
                Student.objects.filter(_username=username).update(_college=clg[0])
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request)
            if 'sltYear' in request.POST:
                yearList = []
                yearTupleList = Student.YEAR_TYPE
                numYear = 0
                for yearTuple in yearTupleList:
                    x = yearTuple[1]
                    yearList.append(x)
                    if yearTuple[1] == request.POST['sltYear']:
                        numYear = yearTuple[0]
                Student.objects.filter(_username=username).update(_year=numYear)
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request)
            if 'textDegree' in request.POST:
                Student.objects.filter(_username=username).update(_degree_pursued=request.POST['textDegree'])
                request.session['call_type'] = INTERNAL
                request.session['mnemonics'] = 'PROFILE_VIEW'
                return Users.views.caller.caller(request)