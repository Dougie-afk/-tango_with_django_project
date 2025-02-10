from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # Construct dict to pass template engine as context
    # Key boldmessage matches to {{ boldmessage }} in index template
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return rendered response to send to
    return render(request,'rango/index.html',context=context_dict)
def about(request):
    context_dict = {'boldmessage':'This tutorial has been put together by Douglas Lande'}
    return render(request,'rango/about.html',context = context_dict)
