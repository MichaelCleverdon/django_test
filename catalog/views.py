from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils import timezone

from catalog.forms import PostForm
from catalog.models import Post
from django.views import generic


def index(request):
    # View function for home page of site

    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=None)


"""Post creation, start of forms"""


def home(request):
    return render(request, 'home.html', {})


"""
class PostListView(generic.ListView):
    model = Post
    context_object_name = 'my_post_list'
    queryset = Post.objects.filter(title__startswith='First')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'
        return context
"""


def postNew(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def postDetail(request):
    return None


def postEdit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def create_account(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)

            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})
