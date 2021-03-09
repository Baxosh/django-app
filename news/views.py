from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Articles, Comments
from .forms import ArticlesForm


def news_detail(request, pk):
    article            = Articles.objects.get(id=pk)
    commentsModel      = Comments.objects.all()
    form               = ArticlesForm(request.POST or None, instance=article)
    incoming_comments  = request.POST.get('comment')
    comments           = Comments(comment_text=incoming_comments)
    users              = request.user.username
    

    print(comments)

    if request.method == "POST":
        comments.save()
        if form.is_valid():
            form.save()
            return redirect("/news")
    return render(request, "news/details_view.html", {"article": article, "form": form, 'comments': commentsModel, 'users': users})


def news_home(request):
    news = Articles.objects.all()
    return render(request, "news/news_home.html", {"news": news})


def news_delete(request, pk):
    article = Articles.objects.get(id=pk)
    if request.method == "POST":
        article.delete()
        return redirect("/news")
    return render(request, "news/news_delete.html", {"article": article})


def news_update(request, pk):
    article = Articles.objects.get(id=pk)
    error = ""
    form = ArticlesForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect("/news")

    data = {"article": article, "form": form}
    return render(request, "news/news_update.html", data)


def create(request):
    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/news")
        else:
            error = "Form has got mistake"

    form = ArticlesForm()

    data = {"form": form, "error": error}
    return render(request, "news/create.html", data)
