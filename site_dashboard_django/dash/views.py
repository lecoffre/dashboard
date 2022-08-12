
from pickle import NONE
from this import d
from unicodedata import name
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.test import SimpleTestCase, override_settings
from django.shortcuts import render, redirect
from django.urls import path
from dash.models import Task, Project, UserStory
from dash.form import ProjectForm, UsForm
from datetime import datetime

class Form:
    add_project = ProjectForm()
    add_us = UsForm()

def redirect_view(request):
    response = redirect('/dashboard/')
    return response


def index(request):
    #latest_question_list = Task.objects.order_by('-pub_date')[:5]
    try:
        projects = Project.objects.all()
        tasks = Task.objects.all()
        tasks_names = [t.name for t in Task.objects.all()]
        tasks_number = [t.number for t in Task.objects.all()]
    except:
        tasks = None
        tasks_names = 0
        tasks_number= 0
        projects = None

    
    context = {'Projects': projects,'Tasks': tasks, 'data1':tasks_names, 'data2':tasks_number, 'Now' : datetime.now().date().isoformat()}
    return render(request, 'dash/index.html', context)

def projects(request):
    mssg = "hello"
    
    if request.method == 'POST': # If the form has been submitted...
        if 'add_project' in request.POST:
            form = ProjectForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                cd = form.cleaned_data
                p = Project(name=cd['name'])
                p.save()
                mssg = "valid"
            else:
                mssg = "not valid"

            # Process the data in form.cleaned_data
            # ...


    projects = Project.objects.all()
    context = {'Projects': projects, 'forms' : Form, "message":mssg, 'type':"normal"}
    return render(request, 'dash/projects.html', context)

def project_detail(request, project_id):
    selected_project = Project.objects.get(id=project_id)
    mssg = "hello"
    if request.method == 'POST': # If the form has been submitted...
        if 'add_us' in request.POST:
            form = UsForm(request.POST) # A form bound to the POST data
            if form.is_valid():
                data = form.cleaned_data
                #p = Project.objects.update(us_id=)
                UserStory.objects.create(
                    name = data['name'],
                    i_want = data['i_want'],
                    project_id = project_id,
                    product_back_log_id = '',

                )

                mssg = "valid"
            else:
                mssg = "not valid"

            # Process the data in form.cleaned_data
            # ...

    project = Project.objects.get(pk=project_id)
    
    try:
        us_total_number = project.us.count()
        pbl_number = project.pbl.us.count()
    except:
        pbl_number=0
        pass
    data1 = pbl_number
    data2 = us_total_number - pbl_number
    context = {'Project': project, 'data1':data1, 'data2':data2, 'forms':Form}
    return render(request, 'dash/project_detail.html', context)

def us_detail(request, us_id):
    us = UserStory.objects.get(pk=us_id)
    context = {'US': us,}
    return render(request, 'dash/us_detail.html', context)

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





