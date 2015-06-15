from django.http.response import HttpResponse
from Users.models import Professor, Branch,Course,Prof_Position,Qualification_Type
from University.models import College

PATH = '/home/profbrew/ProfBrew/Users/tempfiles/'

def insertIntoDatabase(request):
    clg = College.objects.filter(college_name='BITS Pilani Pilani Campus')[0]
    filename = PATH+request.GET['filename']
    if Branch.objects.filter(_branch_name=request.GET['filename'].split('.')[0]).count() == 0:
        Branch.objects.create(_branch_name=request.GET['filename'].split('.')[0])
    branch = Branch.objects.filter(_branch_name=request.GET['filename'].split('.')[0])[0]
    courses = Course.objects.filter(course_name = 'Not Available')[0]
    position = Prof_Position.objects.filter(position_name = 'Professor')[0]
    qualification = Qualification_Type.objects.filter(qualification_name = 'PHD')[0]
    #open the file named filename
    with open(filename, "r") as ins:
        for line in ins:
            line=line[:-1]
            sp_slip = line.split(' ')
            tempStr = ''
            for some in sp_slip:
                tempStr += some
            username = tempStr
            prof = Professor.objects.create(name=line,_username=username,_password='professor',_email='bits@pilani.bits-pilani.ac.in',_college=clg,_area_of_interest = 'Not Applicable',_best_known_for = 'Not Applicable',_popular_name = username,_branch = branch,_ratings = 0,user_type = 2)
            prof.get_position().add(position)
            prof.get_courses_teaching().add(courses)
            prof.get_qualifications().add(qualification)
            prof.save()
        return HttpResponse("Data from file "+filename+" added to database!!!")