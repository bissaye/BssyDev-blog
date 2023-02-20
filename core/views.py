from django.shortcuts import render, redirect
import core.models as core_models
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator


def index(request):
    categories = core_models.Categorie.objects.all()
    context = {
        "homeActive": "active",
        "categories": categories
    }
    return render(request,'core/pages/home_page.html', context=context)

def about(request):
    if request.method.lower() == 'post':
        suscriber = core_models.Email.objects.create(
            email= request.POST["email"]
        )
        suscriber.save()
    context = {
        "aboutActive": "active"
    }
    return render(request,'core/pages/about_page.html', context=context)

def post(request, id=0):
    if id != 0:
        post = get_object_or_404(core_models.Posts, pk=id)
        commentaires = core_models.Commentaires.objects.filter(post=id)
        print("single post")
        print(f"post : {post}")
        context = {
            "post": post,
            "postActive": "active",
            "commentaires": commentaires
        }
        return render(request, 'core/pages/post_page.html', context=context)

    elif 'categorie' in request.GET.keys():
        posts = core_models.Posts.objects.filter(categorie__name = request.GET["categorie"])
        paginator = Paginator(posts, 8)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        print("all post")
        context = {
            "postActive": "active",
            "posts": page_obj
        }
        return render(request, 'core/pages/post_home_page.html', context=context)
    else:
        if 'title' in request.GET.keys():
            posts = core_models.Posts.objects.filter(titre__icontains=request.GET["title"])
            posts = posts | core_models.Posts.objects.filter(description__icontains=request.GET["title"])
        else:
            posts = core_models.Posts.objects.all().order_by('-pk')


        paginator = Paginator(posts, 8)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        print("all post")
        context = {
            "postActive": "active",
            "posts": page_obj
        }
        return render(request, 'core/pages/post_home_page.html', context=context)



def comment(request):
    if request.method == "POST":
        post = get_object_or_404(core_models.Posts, id=int(request.POST["post"]))
        new_comment = core_models.Commentaires(
            adresse= request.POST["email"],
            commentaire = request.POST["commentaire"],
        )
        new_comment.post = post
        new_comment.save()

        return redirect(f"post/{post.id}")