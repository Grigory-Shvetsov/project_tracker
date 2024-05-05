from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.views import View
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.template.loader import render_to_string
from django.shortcuts import render



# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

# def index(request):
#     template = render_to_string('quality_control/index.html')
#     return HttpResponse(template)

def index(request):
    return render(request, 'quality_control/index.html')


# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = "<h1>Список багов</h1><ul>"
#     for bug in bugs:
#         bugs_html += f'<li><a href = "{bug.id}/">{bug.title}</a>, <a>{bug.status}</a></li><br>'
#     bugs_html += '</ul>'
#     return HttpResponse(bugs_html)



def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bug_list': bugs})


# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#     response_html = f"<p>Детали бага {bug_id}:</p><a>Описание: {bug.description}</a>"
#     return HttpResponse(response_html)


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {'bug': bug})


# def feature_list(request):
#     features = FeatureRequest.objects.all()
#     features_html = f"<h1>Список запросов на улучшение</h1><ul>"
#     for feature in features:
#         features_html += f'<li><a href = "{feature.id}/">{feature.title}</a>, <a>{feature.status}</a></li>'
#     features_html += "</ul>"
#     return HttpResponse(features_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'feature_list': features})



# def feature_id_detail(request, feature_id):
#     feature = get_object_or_404(BugReport, id=feature_id)
#     response_html = f"<p>Детали улучшения {feature_id}:</p><a>Описание: {feature.description}</a>"
#     return HttpResponse(response_html)


def feature_id_detail(request, feature_id):
    feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_id_detail.html', {'feature': feature})





class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = f"<h1>Система контроля качества</h1><a href='{bug_list_url}'>Список всех багов</a><br><a href='{feature_list_url}'>Запросы на улучшение</a>"
        return HttpResponse(html)
    


class BugListView(ListView):
    model = BugReport

    def get(self, request, *args, **kwargs):
        bugs = self.get_queryset()
        bugs_html = "<h1>Список багов</h1><ul>"
        for bug in bugs:
            bugs_html += f'<li><a href = "{bug.id}/">{bug.title}</a></li><br>'
        bugs_html += '</ul>'
        return HttpResponse(bugs_html)
    

class FeatureListView(ListView):
    model = FeatureRequest

    def get(self, request, *args, **kwargs):
        features = self.get_queryset()
        features_html = f"<h1>Список запросов на улучшение</h1><ul>"
        for feature in features:
            features_html += f'<li><a href = "{feature.id}/">{feature.title}</a></li><br>'
        features_html += "</ul>"
        return HttpResponse(features_html)
    

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        bug = self.get_object()
        response_html = f"<h2>Детали бага {bug.id}:</h2><ul><li>title: {bug.title}</li> <li>description: {bug.description}</li><li>status: {bug.status}</li><li>priority: {bug.priority}</li><li>project: {bug.project}</li><li>task: {bug.task}</li></ul>"
        return HttpResponse(response_html)
    
class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        feature = self.get_object()
        response_html = f"<h2>Детали улучшения {feature.id}:</h2><ul><li>title: {feature.title}</li> <li>description: {feature.description}</li><li>status: {feature.status}</li><li>priority: {feature.priority}</li><li>project: {feature.project}</li><li>task: {feature.task}</li></ul>"
        return HttpResponse(response_html)


