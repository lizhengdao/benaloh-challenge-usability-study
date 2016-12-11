from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from helios_usabilitystudy.models import Question
import json
import os


def home(request):
    with open(os.path.join(os.path.dirname(__file__), "../helios_main/static/helios_main/index.html"),
              'r') as index_html_file:
        return HttpResponse(index_html_file.read(), content_type='text/html')


@csrf_exempt
def assign(request):
    if 'id' not in request.POST:
        return HttpResponse('{"Error": "No ID supplied."}', content_type='application/json', status=400)
    question = Question.objects.all()
    return HttpResponse(json.dump({
        'question_id': question.pk,
        'question': question.question,
    }), content_type='application/json')
