
from this import d
from unicodedata import name
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.shortcuts import render, redirect
from django.urls import path
from dash.models import Task, Project
from dash.form import ProjectForm
from datetime import datetime

def redirect_view(request):
    
    response = redirect('/dashboard/')
    return response


def index(request):
    #latest_question_list = Task.objects.order_by('-pub_date')[:5]

    tasks = Task.objects.all()
    tasks_names = [t.name for t in Task.objects.all()]
    tasks_number = [t.number for t in Task.objects.all()]
    projects = Project.objects.all()
    context = {'Projects': projects,'Tasks': tasks, 'data1':tasks_names, 'data2':tasks_number, 'Now' : datetime.now().date().isoformat()}
    return render(request, 'dash/index.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {'Projects': projects, 'form' : ProjectForm()}
    return render(request, 'dash/projects.html', context)

def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    context = {'Project': project}
    return render(request, 'dash/project_detail.html', context)

def about(request):
    context = {}
    return render(request, 'dash/about.html', context)




def response_error_handler(request, exception=None):
    return HttpResponse('Error handler content', status=403)


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    path('403/', permission_denied_view),
]

handler403 = response_error_handler
handler404 = 'mysite.views.my_custom_page_not_found_view'


# ROOT_URLCONF must specify the module that contains handler403 = ...
@override_settings(ROOT_URLCONF=__name__)
class CustomErrorHandlerTests(SimpleTestCase):

    def test_handler_renders_template_response(self):
        response = self.client.get('/403/')
        # Make assertions on the response here. For example:
        self.assertContains(response, 'Error handler content', status_code=403)