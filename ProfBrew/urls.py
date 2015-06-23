from django.conf.urls import patterns, include, url
from django.contrib import admin

INTERNAL = 1
EXTERNAL = 2
APPLICATION = 3
CALL_TYPE = {(INTERNAL,'Internal'),(EXTERNAL,'External'),}
handler404 = 'Users.views.home.home.error404'
handler500 = 'Users.views.home.home.error500'
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProfBrew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('Users.views.home.home',
    url(r'^$','home'),
    url(r'^home/$', 'home'),
    url(r'^TermsAndConditions/$','terms_and_conditions'),
)
urlpatterns += patterns('Users.views.login.login',
    url(r'^login/$','login'),
    url(r'^myprofile/$','load_editable_profile'),
    url(r'^myaccount/$','load_editable_profile_after_session'),
)
urlpatterns += patterns('Users.views.caller',
    url(r'^register/student/$','caller'),
    url(r'^caller/$','caller'),
    url(r'^like/review/$','caller'),
)
urlpatterns += patterns('Users.views.register.register',
    url(r'^register/$','register'),
)
urlpatterns += patterns('Users.views.register.filldb',
    url(r'^filldb/$','insertIntoDatabase'),
)
urlpatterns += patterns('Reviews.views.add_reviews',
    url(r'^fresh/review/$','prof_review'),
    url(r'^add/review/$','add_fresh_review'),
)
urlpatterns += patterns('Reviews.views.likes',
    url(r'^likes/review/$','likes')
)
urlpatterns += patterns('SearchEngine.views.search',
    url(r'^search/$', 'search'),
    url(r'^searchBranch/$','branch_search'),
    url(r'^branch_load/$','load_branch'),
)
urlpatterns += patterns('SearchEngine.views.prof_profile',
    url(r'^prof_profile/$','prof_profile'),
)
urlpatterns += patterns('survey.createStudent.createStudent',
    url(r'^survey_home/','survey_home'),
    url(r'^survey/','survey'),
    url(r'^survey_submit','survey_submit'),
)
urlpatterns += patterns('Users.views.profile.profile',
    url(r'^profile/$','get_profile'),
)
urlpatterns += patterns('Users.views.login.logout',
    url(r'^logout/$','logout'),
)
urlpatterns += patterns('Ratings.views.basic.add_all_profs',
    url(r'^add_all_profs/$','add_all_profs'),
)
urlpatterns += patterns('Ratings.views.basic.rate_prof',
    url(r'^rate/$','rate'),
)
mnemonics = {
    '/home/':'HOME',
    '/login/':'LOGIN_PAGE',
    '/register/':'VERIFY_CRED',
    '/caller/':'REGISTER_PAGE',
}
