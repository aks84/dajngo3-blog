from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Article


def index(request):
	articles = Article.objects.all()
	paginator = Paginator(articles, 3)
	page = request.GET.get('page')
	posts = paginator.get_page(page)
	return render(request, 'index.html', {'posts':posts })


def single(request, id):
	single = Article.objects.get(id=id)

	nextpost = Article.objects.filter(id__gt=single.id).order_by('id').first()
	prevpost = Article.objects.filter(id__lt=single.id).order_by('id').last()
	
	return render(request, 'single.html', {'single': single, 'prevpost':prevpost, 'nextpost':nextpost})



