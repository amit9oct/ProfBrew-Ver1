from University.models import College
from Users.models import Branch, Student,Users, Professor
from django.shortcuts import render
import Users.views
from django.http.response import HttpResponse
from ProfBrew.urls import INTERNAL


def register(request):
    college_list = College.objects.all()
    branch_list = Branch.objects.all()
    year_tupple_list = Student.YEAR_TYPE
    year_list = []
    for year_tupple in year_tupple_list:
        x=year_tupple[1]
        year_list.append(x)
    context = {'college_list': college_list,'branch_list':branch_list,'year_list': year_list}
    return render(request,'register/register.html',context)

def register_student(request):
    if request.method == 'GET':
        return render("<html>Bad way to access!!!!</html>")
    elif request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        name = fname+' '+lname
        email = request.POST['email']
        password = request.POST['password']
        clgname = request.POST['clgname']
        branch_name = request.POST['branch']
        degree = request.POST['degree']
        year = request.POST['year']
        year_tupple_list = Student.YEAR_TYPE
        num_year = 0
        for year_tupple in year_tupple_list:
            if year_tupple[1] == year:
                num_year = year_tupple[0]
        branch_list = Branch.objects.filter(_branch_name=branch_name)
        clg_list = College.objects.filter(college_name=clgname)
        clg=clg_list[0]
        branch=branch_list[0]
        Student.objects.create(_username=username,user_type=Users.models.Users.STUDENT,_password=password,name=name,_email=email,_college=clg,_contributing_factor=0,_branch=branch,_degree_pursued=degree,_year=num_year)
        request.session['call_type'] = INTERNAL
        request.session['mnemonics'] = 'LOGIN_PAGE'
        return Users.views.caller.caller(request)

def username_present(request):
    username = request.POST.get('username',None)
    user_type = request.POST.get('user_type',None)
    if user_type=='Student':
        tempObj = Student.objects.filter(_username=username)
        if len(tempObj) != 0:
            return HttpResponse("User Name already exists")
        else:
            return HttpResponse("False")
    else:
        tempObject = Professor.objects.filter(_username=username)
        if len(tempObject) != 0:
            return HttpResponse("User Name already exists")
        else:
            return HttpResponse("False")