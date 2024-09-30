from django.shortcuts import render

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Question
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = "bạn đang nhìn thấy kết quả của câu hỏi số %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("bạn đã bình chọn cho câu hỏi số %s." % question_id)