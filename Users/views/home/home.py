from django.shortcuts import render_to_response,render
from django.http import HttpResponse
from ProfBrew.urls import EXTERNAL
from addedFeatures.profs import get_top_prof_rate
from addedFeatures.reviews import get_most_liked_review


def home(request):
    request.session['last_url'] = '/home/'
    request.session['call_type'] = EXTERNAL
    temp = request.session.get('user_type',None)
    if temp != 'Student' and temp != 'Professor':
        request.session['user_type'] = 'Visitor'
    top_prof_rate = get_top_prof_rate()
    top_review_list = get_most_liked_review()
    context = {'top_prof':top_prof_rate.get_prof, 'top_prof_rate':top_prof_rate, 'top_review_list':top_review_list}
    return render(request,"home/home.html",context)

def search(request):
    return render(request,'search/home.html')

def error500(request):
        msg = 'Error 500!!!'
        title = 'Server Error'
        otherdata = "Server Error.<a href='/home/'>Click here to go back!!</a>"
        context = { 'message':msg , 'otherdata':otherdata,'title':title}
        return render(request,'error.html',context)


def error404(request):
        msg = 'Error 404!!!'
        title = 'Page Not Found Error'
        otherdata = "Page Not Found.<a href='/home/'>Click here to go back!!</a>"
        context = { 'message':msg , 'otherdata':otherdata,'title':title}
        return render(request,'error.html',context)

def terms_and_conditions(request):
    with open('templates/TermsAndConditionsForWebsiteUsage.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(),content_type='application/pdf')
        response['Content-Disposition'] = 'filename=TermsAndConditionsForWebsiteUsage.pdf.pdf'
        return response
    pdf.closed
