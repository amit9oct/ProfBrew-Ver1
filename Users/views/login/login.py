from django.shortcuts import render,redirect
from django.http.response import HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from Users.models import Student, Professor
from ProfBrew.urls import mnemonics,INTERNAL, EXTERNAL
from Users.views.profile.profile import profile
import Users.views

def login(request):
    if not 'last_url' in request.session:
        request.session['last_url'] = '/home/'
    if not 'call_type' in request.session:
        request.session['call_type'] = EXTERNAL
    return render(request,'login/login.html')

def verify_credentials(request,user_type,last_url):
    if request.method == 'GET':
        return HttpResponseBadRequest
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        temp_user = None
        if user_type=='Student':
            temp_user = Student.objects.filter(_username=username,_password=password)
        else:
            temp_user = Professor.objects.filter(_username=username,_password=password)
        if len(temp_user) == 0:
            request.session['mnemonics'] = mnemonics[last_url] 
            request.session['call_type'] = INTERNAL
            return Users.views.caller.caller(request)
        elif len(temp_user) == 1:
            user = temp_user[0]
            request.session['username'] = user.get_username()
            request.session['user_type'] = user.get_user_type()
            request.session['mnemonics'] = 'PROFILE_VIEW'#mnemonics[last_url] 
            request.session['call_type'] = INTERNAL
            #return HttpResponse(request.session['mnemonics'])
            return Users.views.caller.caller(request)
        
@csrf_exempt
def load_editable_profile(request):
    #this function sends a direct request to the profile method
    last_url = request.session['last_url']
    user_type = request.POST['user_type']
    request.session['mnemonics'] = 'VERIFY_CRED'
    if request.method == 'GET':
        return HttpResponseBadRequest
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        temp_user = None
        if user_type=='Student':
            temp_user = Student.objects.filter(_username=username,_password=password)
        else:
            temp_user = Professor.objects.filter(_username=username,_password=password)
        if len(temp_user) == 0:
            request.session['mnemonics'] = mnemonics[last_url]
            request.session['call_type'] = INTERNAL
            return redirect(last_url)
        elif len(temp_user) == 1:
            user = temp_user[0]
            request.session['username'] = user.get_username()
            request.session['user_type'] = user.get_user_type()
            request.session['mnemonics'] = 'PROFILE_VIEW' 
            request.session['call_type'] = INTERNAL
            return profile(request,request.session['user_type'])

