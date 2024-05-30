from django.shortcuts import render

# Create your views here.
def resource(request):
    page = 'resource'
    context = {'page':page}
    return render(request, 'user/resource.html', context)