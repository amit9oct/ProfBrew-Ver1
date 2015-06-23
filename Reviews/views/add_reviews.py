'''
Created on Jan 26, 2015

@author: Amitayush Thakur
'''
from Reviews.models import ProfessorReviews
from Users.models import Professor, Student
from django.shortcuts import redirect,render
from django.http.response import HttpResponse
import Users.views
from ProfBrew.urls import INTERNAL, APPLICATION
import json

FRESH_REVIEW = 1
EXISTING_REVIEW = 2
REVIEW_TYPE = {
    'ADD_FRESH_REVIEW':FRESH_REVIEW,
    'Existing Review':EXISTING_REVIEW,
}

def add_fresh_review(request):
    user_type = request.session.get('user_type',None)
    if user_type != 'Student':
        request.session['call_type'] = INTERNAL
        msg = 'Visitor cannot add review!!!'
        title = 'Cannot Add review!!!'
        otherdata = "<a href='/login/'>Login or signup to add a review. Click here to go login or signup!!</a>"
        context = { 'message':msg , 'otherdata':otherdata,'title':title}
        return render(request,'error.html',context)
    student_id = request.session['username']
    prof_id = request.POST['prof_id']
    review_type = request.POST['review_type']
    review_text = request.POST['review_text']
    return add_prof_review(request,prof_id,student_id,None,REVIEW_TYPE['ADD_FRESH_REVIEW'],review_text)

def add_prof_review(request,prof_id,student_id,review_id,review_type,review_text):
    prof = Professor.objects.filter(_username=prof_id)[0]
    student = Student.objects.filter(_username=student_id)[0]
    if review_type == FRESH_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        if request.session['call_type'] == APPLICATION:
            response_data= {}
            response_data['message'] = review_text
            return HttpResponse(json.dumps(response_data),"application/json")
        request.session['call_type'] = INTERNAL
        request.session['mnemonics'] = 'PROF_PROFILE_VIEW/'+ prof_id
        return redirect('/prof_profile/?prof='+prof_id)
    elif review_type == EXISTING_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        prev_review = ProfessorReviews.objects.filter(_review_id=review_id)[0]
        prev_review.update_next_review(new_review)
        prev_review.save()
    return HttpResponse(review_text)

def prof_review(request):
    prof_id = request.POST['prof_id']
    student_id = request.POST['student_id']
    review_type = REVIEW_TYPE[request.POST['review_type']]
    review_text = request.POST['review_text']
    prof = Professor.objects.filter(_username=prof_id)[0]
    student = Student.objects.filter(_username=student_id)[0]
    if review_type == FRESH_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        if request.session['call_type'] == APPLICATION:
            response_data= {}
            response_data['message'] = review_text
            return HttpResponse(json.dumps(response_data),"application/json")
        request.session['call_type'] = INTERNAL
        request.session['mnemonics'] = 'PROF_PROFILE_VIEW/'+ prof_id
        return HttpResponse(review_text)
    elif review_type == EXISTING_REVIEW:
        new_review = ProfessorReviews.objects.create(_professor=prof,_student=student,_review=review_text)
        prev_review = ProfessorReviews.objects.filter(_review_id=review_id)[0]
        prev_review.update_next_review(new_review)
        prev_review.save()
    return HttpResponse(review_text)
