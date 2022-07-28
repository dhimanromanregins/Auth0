from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout
from django.http import HttpResponseRedirect
from .models import *

def index(request):
    products = [
        {'title': 'PlayStation', 'price': 300, 'image': 'https://cdn.auth0.com/blog/django-webapp/playstation.png'},
        {'title': 'iPhone', 'price': 900, 'image': 'https://cdn.auth0.com/blog/django-webapp/iphone.png'},
        {'title': 'Yummy Pizza', 'price': 10, 'image': 'https://cdn.auth0.com/blog/django-webapp/pizza.png'},
    ]

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)




# ... index definition ...

@login_required
def profile(request):
    user = request.user
    auth0user = user.social_auth.get(provider='auth0')
    userdata = {
        'user_id': auth0user.uid,
        'name': user.first_name,
        'picture': auth0user.extra_data['picture']
    }

    return render(request, 'profile.html', {
        'auth0User': auth0user,
        'userdata': json.dumps(userdata, indent=4)
    })


# ... index, profile ...

def logout(request):
    django_logout(request)
    domain = 'dev-klkardnk.us.auth0.com'
    client_id = 'YjUvbasIGyqTnjlzplqCRYRHnRKk4YQn'
    return_to = 'http://localhost:8000'
    return HttpResponseRedirect(f'https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}')

def Blog(requests):
    blog_blog = blog.objects.all()
    return render(requests, 'blog.html',{'blog_blog':blog_blog})

def single_blog(requests,pk):
    blog_blog = blog.objects.get(id=pk)
    return render(requests, 'single_blog.html',{'blog_blog':blog_blog})

