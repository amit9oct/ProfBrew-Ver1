
from Users.models import Student
from Reviews.models import ProfessorReviewLikes,ProfessorReviews
from django.http.response import HttpResponse



def get_most_liked_review():
    all_reviews = ProfessorReviews.objects.all()
    max_likes_review = all_reviews[0]
    max_likes = 0
    for review in all_reviews:
        if review.get_number_of_likes() > max_likes:
            max_likes_review = review
            max_likes = review.get_number_of_likes()
    return max_likes_review
