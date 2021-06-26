from django.urls import path
from polls import views

urlpatterns = [
    path('', views.index, name='index'),
    # /polls/5/
    # sends the values of question_id to the views
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),


] 