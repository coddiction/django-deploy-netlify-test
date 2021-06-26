from django.shortcuts import HttpResponse, render, get_object_or_404
from django.http import Http404
from polls.models import Question

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:]
    # latest_question_text_list = [q.question_text for q in latest_question_list]
    context = {
        'latest_question_list': latest_question_list,
    }
    
    return render(request, 'index.html', context=context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except:
    #     raise Http404('Question does not existion')  
    # shortcut for try and except
    question = get_object_or_404(Question, pk=question_id)  
    return render(request, 'detail.html', {'question':question})



def results(request, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}")        

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")        