from django.conf.urls import url
from Task import views
# SET THE NAMESPACE!
app_name = 'Task'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^index/$', views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^task/$', views.task,name='task'),
    url(r'^tasksave/$', views.tasksave,name='tasksave'),
    url(r'^show/$', views.show,name='show'),
    url(r'^Eshow/$', views.Eshow,name='Eshow'),
]

