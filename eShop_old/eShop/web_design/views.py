from django.views.generic import TemplateView
from os.path import exists

def IndexView(request):
    pass

class PageView(TemplateView):

    def get_template_names(self):
        template_name = self.kwargs.get('template','index.html')
        return template_name



