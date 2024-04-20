from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.all()
    ordering = '-published_at'
    object_list.order_by(ordering)
    context = {'object_list': object_list}
    return render(request, template, context)
