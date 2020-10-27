from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from portfolio.models import Project

class ProjectListView(ListView):
    model = Project
    template_name = "projects.html"
    def get_context_data(self, **kwargs):
        projects = Project.objects.all()
        context = {
                "projects": projects
                }
        return context

class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"
    def get_context_data(self, **kwargs):
        project = Project.objects.get(title=self.object)
        context = {
                "project": project
                }
        return context
