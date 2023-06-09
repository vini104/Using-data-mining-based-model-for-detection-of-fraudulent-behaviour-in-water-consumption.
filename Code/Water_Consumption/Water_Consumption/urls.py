"""Water_Consumption URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from Users_Controller import views as user_views
from Admin_Controller import views as admin_views



urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', user_views.index, name='index' ),
    url(r'^base/$', user_views.base, name='base' ),
    url(r'^user_logins/$', user_views.user_logins, name='user_logins'),
    url(r'^user_registers/$', user_views.user_registers, name='user_registers'),
    url(r'^user_wateranalysis/$', user_views.user_wateranalysis, name='user_wateranalysis'),
    url(r'^user_feedback/$', user_views.user_feedback, name='user_feedback'),
    url(r'^ucharts/(?P<chart_type>\w+)', user_views.ucharts,name="ucharts"),


    url(r'^admin_login/$', admin_views.admin_login, name='admin_login'),
    url(r'^admin_viewfeedback/$', admin_views.admin_viewfeedback, name='admin_viewfeedback'),
    url(r'^viewalldetails/$', admin_views.viewalldetails, name='viewalldetails'),
    url(r'^viewtreandingtopics/(?P<chart_type>\w+)/$', admin_views.viewtreandingtopics,name="viewtreandingtopics"),
    url(r'^negativefeedbacktivechart/(?P<chart_type>\w+)/$',admin_views.negativefeedbacktivechart,name="negativefeedbacktivechart"),
    url(r'^charts/(?P<chart_type>\w+)', admin_views.charts,name="charts"),


]
