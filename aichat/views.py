from django.http import HttpResponse
from django.views.generic import TemplateView

# Home page    
# def home_page_view(request):
#     return HttpResponse("Hello! This is my AI chatbot.")

# React home page
class React(TemplateView):
    template_name = 'index.html'