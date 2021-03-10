from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Articles, Comments
from .forms import ArticlesForm


def news_detail(request, pk):
    article = Articles.objects.get(id=pk)
    comments = Comments.objects.filter(article_id=pk)
    form = ArticlesForm(request.POST or None, instance=article)
    


    if request.method == "POST":
        comments.create(
            comment_text=request.POST.get("comment"), author=request.user, article_id=pk
        )
        # return redirect('/news')
        

    return render(
        request,
        "news/details_view.html",
        {"article": article, "form": form, "commentsModel": comments},
    )


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


def news_create(request):

    error = ""
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/news")
        else:
            error = "Form has got mistake"

    form = ArticlesForm()

    data = {"form": form, "error": error}
    return render(request, "news/news_create.html", data)
