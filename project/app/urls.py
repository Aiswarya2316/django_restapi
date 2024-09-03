from django.urls import path
from.import views
urlpatterns = [
    path('',views.dictionary),
    path('std',views.std),
    path('fun2',views.fun2),
    path('fun3',views.fun3),
    path('fun4',views.fun4),




]