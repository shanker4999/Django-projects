from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    #polls/05
    url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    #polls/05/result
    url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='result'),
    #polls/05/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^contact/$',views.contact,name='contact'),

]



