from django.urls import URLPattern, path
from exam import views

urlpatterns=[path('test/',views.test),
path('handtracking/',views.handtracking, name="handtrack"),
path("test/index.html/",views.whiteboard),
# path('screens/login.html',views.login),
]