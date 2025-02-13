from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

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


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category = category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html',context=context_dict)


