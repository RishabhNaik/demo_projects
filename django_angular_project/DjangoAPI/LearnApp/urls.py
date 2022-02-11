from django.conf.urls import url
from LearnApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^teacher/$',views.teacherApi),
    url(r'^teacher/([0-9]+)$',views.teacherApi),

    #  url(r'^employee/$',views.employeeApi),
    # url(r'^employee/([0-9]+)$',views.employeeApi),

    # url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)