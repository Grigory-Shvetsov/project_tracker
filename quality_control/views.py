from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.shortcuts import get_object_or_404


def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = "<h1>Список багов</h1><ul>"
    for bug in bugs:
        bugs_html += f'<li><a href = "{bug.id}/">{bug.title}</a>, <a>{bug.status}</a></li><br>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    response_html = f"<p>Детали бага {bug_id}:</p><a>Описание: {bug.description}</a>"
    return HttpResponse(response_html)


def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = f"<h1>Список запросов на улучшение</h1><ul>"
    for feature in features:
        features_html += f'<li><a href = "{feature.id}/">{feature.title}</a>, <a>{feature.status}</a></li>'
    features_html += "</ul>"
    return HttpResponse(features_html)


def feature_id_detail(request, feature_id):
    feature = get_object_or_404(BugReport, id=feature_id)
    response_html = f"<p>Детали улучшения {feature_id}:</p><a>Описание: {feature.description}</a>"
    return HttpResponse(response_html)




# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         bug_list_url = reverse('quality_control:bug_list')
#         feature_list_url = reverse('quality_control:feature_list')
#         html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
#         return HttpResponse(html)
