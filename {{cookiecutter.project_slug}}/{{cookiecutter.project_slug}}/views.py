from django.views import generic


class IndexView(generic.TemplateView):
    template_name = '{{cookiecutter.project_slug}}/index.html'


class AboutView(generic.TemplateView):
    template_name = '{{cookiecutter.project_slug}}/about.html'
