from Users.models import Student, Professor
from University.models import College
from django.shortcuts import render,redirect
from Ratings.models import ProfRatings
from Reviews.models import ProfessorReviews


class ReviewView:
    def __init__(self,review_object,visited):
        self.review_object = review_object
        self.visited = visited
    def is_visited(self):
        return self.visited
    def mark_visited(self):
        self.visited = True
#review object should have a level tag

def profile(request,user_type):
    #this method loads the profile which are editable
    temp_username = request.session['username'] 
    temp_user = None
    if user_type == 'Student':
        temp_user = Student.objects.filter(_username=temp_username)
        yearList = []
        yearTupleList = Student.YEAR_TYPE
        for yearTuple in yearTupleList:
            x = yearTuple[1]
            yearList.append(x)
        collegeList = College.objects.all()            
        context = {'student': temp_user[0],'collegeList': collegeList,'yearList': yearList}
        return render(request,'profile/editableStudentProfile.html',context)
    elif user_type == 'Professor':
        temp_user = Professor.objects.filter(_username=temp_username)
        coursesList = temp_user[0].get_courses_teaching().all()
        qualificationsList = temp_user[0].get_qualifications().all()
        positionsList = temp_user[0].get_position().all()
        collegeList = College.objects.all()
        rateList = ProfRatings.objects.filter(_prof =  temp_user[0])
        context = {
                   'professor': temp_user[0],
                   'collegeList': collegeList,
                   'coursesList':coursesList,
                   'qualificationsList' : qualificationsList,
                   'positionsList' : positionsList,
                   'rate' : rateList[0]
        }
        return render(request,'profile/editableProfessorProfile.html',context)

def profile_view(request,username):
    temp_username = username
    user_type = None
    if Professor.objects.filter(_username=temp_username).count() == 0:
        user_type = 'Student'
    else:
        user_type = 'Professor'
    temp_user = None
    if user_type == 'Student':
        temp_user = Student.objects.filter(_username=temp_username)
        yearList = []
        yearTupleList = Student.YEAR_TYPE
        for yearTuple in yearTupleList:
            x = yearTuple[1]
            yearList.append(x)
        collegeList = College.objects.all()            
        context = {'student': temp_user[0],'collegeList': collegeList,'yearList': yearList}
        return render(request,'profile/studentProfile.html',context)
    elif user_type == 'Professor':
        temp_user = Professor.objects.filter(_username=temp_username)
        coursesList = temp_user[0].get_courses_teaching().all()
        qualificationsList = temp_user[0].get_qualifications().all()
        positionsList = temp_user[0].get_position().all()
        collegeList = College.objects.all()
        rateList = ProfRatings.objects.filter(_prof =  temp_user[0])
        context = {
                   'professor': temp_user[0],
                   'collegeList': collegeList,
                   'coursesList':coursesList,
                   'qualificationsList' : qualificationsList,
                   'positionsList' : positionsList,
                   'rate' : rateList[0]
        }
        return render(request,'profile/professorProfile.html',context)

def get_profile(request):
    user_id = request.GET['username']
    return profile_view(request,user_id)

def profile_of_prof(request,prof_id,user_type):
        temp_user = Professor.objects.filter(_username = prof_id)
        coursesList = temp_user[0].get_courses_teaching().all()
        qualificationsList = temp_user[0].get_qualifications().all()
        positionsList = temp_user[0].get_position().all()
        collegeList = College.objects.all()
        rateList = ProfRatings.objects.filter(_prof = prof_id)
        rate = rateList[0]
        review_list = ProfessorReviews.objects.filter(_professor=temp_user)
        context = {
                   'professor': temp_user[0],
                   'collegeList': collegeList,
                   'coursesList':coursesList,
                   'qualificationsList' : qualificationsList,
                   'positionsList' : positionsList,
                   'rate' : rate,
                   'review_list':review_list,
        }
        return render(request,'profile/professorProfile.html',context)

"""
can't load reviews from normal rendering because it requires recursive calls
make a button load reviews and send ajax request and then using that make recurssive calls
load them up in chunks
"""
