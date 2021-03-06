from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse ,Http404,HttpResponseRedirect
from .models import Question ,Choice
from django.core.urlresolvers import reverse
# Create your views here.


def index(request):
    try:
        latest_question_list = Question.objects.all()
    except:
        raise Http404("Question does not exist")
    return render(request, 'polls/index.html', context={'latest_question_list': latest_question_list})



def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
        return render(request,'polls/detail.html', context={'question':question})
    except Question.DoesNotExist:
        raise Http404("Question does not exists")




def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError,Choice.DoesNotExist):
        return render(request,'polls/detail.html',{
            'question':question,
            'error_message':'You did not select a choice'
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('result',args=(question_id)))



def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/result.html', {'question': question})

def contact(request):
    return render(request,'polls/contact.html')
