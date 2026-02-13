from .models import *

def get_categories(request):
    categories=Category.objects.all()
    return dict(categories=categories)

def get_about(request):
    try:
        about_us=About.objects.get()
    except:
        about_us=None
    print(about_us)
    return dict(about=about_us)