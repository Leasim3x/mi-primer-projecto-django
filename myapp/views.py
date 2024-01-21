from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h2>Hello Word</h2>")

def about(request):
    return HttpResponse('About')