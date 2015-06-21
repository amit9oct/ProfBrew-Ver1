
from Users.models import Student
from Reviews.models import ProfessorReviewLikes,ProfessorReviews
from django.http.response import HttpResponse



def get_most_liked_review():
    all_reviews = ProfessorReviews.objects.all()
    max_like_review_list = []
    for review in all_reviews:
        max_like_review_list.append(review)
    max_like_review_list.sort(key=lambda x: x.get_number_of_likes(), reverse=False)
    i = 0
    top_4_list = []
    for review in max_like_review_list:
        top_4_list.append(review)
        i += 1
        if i>=4:
            break
    return top_4_list
