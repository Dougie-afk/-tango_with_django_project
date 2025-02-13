from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Construct dict to pass template engine as context
    # Key boldmessage matches to {{ boldmessage }} in index template

    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list



    # Return rendered response to send to
    return render(request,'rango/index.html',context=context_dict)



def about(request):
    context_dict = {'boldmessage':'This tutorial has been put together by Douglas Lande'}
    return render(request,'rango/about.html',context = context_dict)

