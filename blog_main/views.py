from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import *
def home(request):
    # categories = Category.objects.all()
    # print(categories)
    
    featured_post = Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    print(featured_post)
    post=Blog.objects.filter(is_featured=False,status='Published').order_by('updated_at')
    print(post)
    context={
        # 'categories':categories,
        'featured_post':featured_post,
        'posts':post,
    }
    return render(request,'home.html',context)
    return HttpResponse('<h2>Home Page<h2>')