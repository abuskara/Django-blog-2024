from django.http import HttpResponse, Http404
from blogging.models import Post
from django.template import loader
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Post


# Create your views here.
def stub_view(request, *args, **kwargs):
    body = "Stub View \n\n"
    if args:
        body += "Args: \n"
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Keyword args: \n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    context_object_name = "posts"

    def get_queryset(self):
        # Filter out posts that have no published_date
        return Post.objects.exclude(published_date__exact=None).order_by(
            "-published_date"
        )


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        # Override to exclude posts without a published_date
        obj = super().get_object(queryset)
        if obj.published_date is None:
            raise Http404("Post not found")
        return obj


"""
def list_view(request):
    published = Post.objects.exclude(published_date__exact= None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}
    return render(request, 'blogging/list.html', context)

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}
    return render(request, 'blogging/detail.html', context)
"""
