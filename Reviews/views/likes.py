'''
Created on Jan 30, 2015

@author: Amitayush Thakur
'''
from Users.models import Student,Professor
from Reviews.models import ProfessorReviewLikes,ProfessorReviews
from django.http.response import HttpResponse


def liked_already(liking_student,review,factor):
    like_list = ProfessorReviewLikes.objects.filter(_student=liking_student,_review=review)
    if len(like_list)==0 :
        return False
    else:
        has_liked = like_list[0].has_liked()
        has_disliked = like_list[0].has_disliked()
        if has_liked:
            if int(factor) == -1:
                review.update_number_of_likes(review.get_number_of_likes()-1)
                review.save()
                return False
            else:
                return True
        elif has_disliked:
            if int(factor) == 1:
                review.update_number_of_likes(review.get_number_of_likes()+1)
                review.save()
                return False
            else:
                return True
            
    
def like_prof_review(request,review,factor):
    liking_student_id = request.session['username']
    liking_student_list = Student.objects.filter(_username=liking_student_id)
    liking_student = liking_student_list[0]
    if not liked_already(liking_student,review,factor):
        student_like_list = ProfessorReviewLikes.objects.filter(_student=liking_student,_review=review)
        number_of_likes_by_one_student =len(student_like_list)
        if number_of_likes_by_one_student == 0:
            if int(factor) == 1:
                ProfessorReviewLikes.objects.create(_student=liking_student,_review=review,_liked=True,_disliked=False)
            elif int(factor) == -1:
                ProfessorReviewLikes.objects.create(_student=liking_student,_review=review,_liked=False,_disliked=True)
        elif number_of_likes_by_one_student==1:
            student_like=student_like_list[0]
            if int(factor)==1:
                student_like.update_liked(True)
                student_like.update_disliked(False)
            elif int(factor)==-1:
                student_like.update_liked(False)
                student_like.update_disliked(True)
            student_like.save()
        review.update_number_of_likes(review.get_number_of_likes()+int(factor))
        review.save()
    return HttpResponse(str(review.get_number_of_likes()))
	
def likes(request):
        student_id = request.POST['student_id']
        prof_id = request.POST['prof_id']
        date_time = request.POST['time_stamp']
        student = Student.objects.filter(_username=student_id)
        prof = Professor.objects.filter(_username=prof_id)
        review_list = ProfessorReviews.objects.filter(_student=student[0],_professor=prof[0])
        review = review_list[0]
        for rev in review_list:
            if rev.get_timestamp() == date_time:
                review = rev
        factor = request.POST['factor']
        return like_prof_review(request,review,factor)
