'''
Created on Mar 1, 2015

@author: Amitayush Thakur
'''
from django.shortcuts import render
from django.http.response import HttpResponse

def logout(request):
    request.session.flush()
    msg = 'Successfully Logged Out!!!'
    title = 'Logged Out'
    otherdata = "<a href='/home/'>Click here to go back!!</a>"
    context = { 'message':msg , 'otherdata':otherdata,'title':title}
    return render(request,'error.html',context)