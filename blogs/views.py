from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import *
# Create your views here.
def posts_by_category(request,category_id):
    # Fetch post of cat_id
    posts = Blog.objects.filter(status='Published',category=category_id)
    # to go to the home page or custom action
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
        # redirect the user to homepage
    #     return redirect('home')

    # if u want to show 404 page
    category=get_object_or_404(Category,pk=category_id)
    context ={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html',context)