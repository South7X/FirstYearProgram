from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views import generic
from django.urls import reverse
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls:detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls:results.html'
# def index(request):
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    context = {'latest_question_list': latest_question_list}
#    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls:results.html', {'question': question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s" % question_id)
# Create your views here.
