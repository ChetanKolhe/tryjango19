from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from posts.models import Posts
from .forms import PostForm

def post_create(request):
    if request.method == "POST":
        print(request.POST)
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form
    }
    return render(request, "post_form.html", context)


def post_details(request,id=None):
    # if request.user.is_authenticated:
    #     context = {"data": "Authenicated"}
    # else:
    #     context = {"data": "Non Authenticated"}
    #instance = Posts.objects.get(id=3)
    instance=get_object_or_404(Posts, id=id)
    context = {
        "instance": instance,


    }
    return render(request, "post.html", context)


def post_list(request):
    queryset=Posts.objects.all()
    context={
        "object_list": queryset,
        "title": "list"

    }
    return render(request, "index.html",context)
    #return HttpResponse("<H1>Hello Technical Blog<H1>")


def post_update(request):
    return HttpResponse("<H1>Hello Technical Blog<H1>")


def post_delete(request):
    return HttpResponse("<H1>Hello Technical Blog<H1>")


