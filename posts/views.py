from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    f = open(f'static/{posts.body}')
    s = f.read()
    content = {
        'title': posts.title,
        'author': posts.author,
        'image': posts.image,
        'body': s,
        'created_at': posts.created_at
    }
    return render(request, 'posts.html', {'posts':content})