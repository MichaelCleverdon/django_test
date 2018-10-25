from django.shortcuts import render

from catalog.forms import PostForm
from catalog.models import Post
from django.views import generic


def index(request):
    # View function for home page of site

    # Generate counts of some of the main objects

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=None)


def library(request):
    context = None
    return render(request, 'library.html', context=context)


"""Post creation, start of forms"""


def createpost(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('content'):
            p = Post()
            p.title = request.POST.get('title')
            p.content = request.POST.get('content')
            p.save()
            return render(request, 'library.html')
    else:
        return render(request, 'library.html')


def showpost(request):
    alltitles = Post.objects.all()
    #  allcontext = Post.context.all()
    context = {
        'alltitles': alltitles
    }
    return render(request, 'library.html', context)


class PostListView(generic.ListView):
    model = Post
    context_object_name = 'my_post_list'
    queryset = Post.objects.filter(title__startswith='First')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)

        context['some_data'] = 'This is just some data'
        return context


def postNew(request):
    form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def postDetail(request):
    return None


def postEdit(request):
    if request.method == "POST":
        form = PostForm(request.POST)
    else:
        form = PostForm()
    return render(request, 'postedit.html', {'form': form})