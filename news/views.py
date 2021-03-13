from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from .models import Articles, Comments
from .forms import ArticlesForm, CommentsForm


def news_detail(request, pk):
    article = Articles.objects.get(id=pk)
    comments = Comments.objects.filter(article_id=pk)
    form = CommentsForm(request.POST or None)

    if request.method == "POST":
        # print(article.author)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.article_id = pk
            post.save()
            return redirect(f"/news/{pk}")

    return render(
        request,
        "news/details_view.html",
        {"article": article, "form": form, "comments": comments},
    )


def comment_update(request, id):
    # article = Articles.objects.get(id=pk)
    comment = Comments.objects.get(id=id)
    form = CommentsForm(request.POST or None, instance=comment)
    if request.method == "POST":
        form.save()
        comment.save()
        return redirect(f"/news/edit/{id}")

    return render(
        request, "news/comment_update.html", {"comment": comment, "form": form}
    )


def delete(request, id):
    comment = Comments.objects.get(id=id)
    comment.delete()
    return redirect("/news/")


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
