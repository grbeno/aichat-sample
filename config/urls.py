from django.contrib import admin
from django.urls import path, re_path, include
from aichat.views import React


urlpatterns = [
	path('admin/', admin.site.urls),

	# helloworld app
	path("", include("aichat.urls")),
    
	# React
    re_path(r'^.*$', React.as_view(), name='frontend'),
]


