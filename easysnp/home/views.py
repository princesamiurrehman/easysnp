from django.template import loader
from django.http import HttpResponse

def index(request):
    template = loader.get_template('home.html')
    context = {
        'website': 'easysnp',
    }
    return HttpResponse(template.render(context, request))

