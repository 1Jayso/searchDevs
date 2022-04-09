from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully Functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'Thia is a project shocasing my portfolio'
    },
    {
        'id': '3',
        'title': 'Social Network App',
        'description': 'This is an awesome project I am looking to\
        donate to the oppesource community'
    },
]


def projects(request):
    projects = Project.objects.all()
    context = {
  
        'projects': projects
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html",
                  {'projectObj': projectObj})


def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        print(form)
        print(request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES,  instance=project)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)