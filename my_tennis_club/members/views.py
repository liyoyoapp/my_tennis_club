from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def members(request):
    context = {
        "first_name": "ABC",
        "last_name": "Li",
    }
    return render(request, 'members/index.html',context)
    #return HttpResponse("Hello, world. You're at the Member page.")