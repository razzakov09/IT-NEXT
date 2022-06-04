from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.db.models import Q
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from .forms import PostCommentForm


def index(request):
    ads = Advert.objects.all()
    products = Product.objects.all()

    context = {
        'ads': ads,
        'products': products
    }
    return render(request, 'index.html', context= context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'it_shop.html', context=context)


def about(request):
    staff = Staff.objects.all()[:4]
    context = {
        'staff': staff
    }
    return render(request, 'it_about.html', context=context)


def blog_list(request):
    blogs = Blog.objects.all()[::-1]#[:3]
    blog_paginator = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    page = blog_paginator.get_page(page_num)
    context = {
        'page': page,
        'count':blog_paginator.count
    }
    return render(request, 'it_blog.html', context=context)


class SearchResultsView(ListView):
    model = Blog
    template_name = 'search.html'

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Blog.objects.filter(Q(title__icontains=query))

        if list(object_list) == []:
            object_list = 0
        return object_list


def blog_grid(request):
    blogs = Blog.objects.all()
    blog_paginator = Paginator(blogs, 3)
    page_num = request.GET.get('page')
    page = blog_paginator.get_page(page_num)
    context = {
        'page': page,
        'count': blog_paginator.count
    }
    return render(request, 'it_blog_grid.html', context=context)


def service(request):
    services = Service.objects.all()
    staff = Staff.objects.all()[:4]
    context = {
        'services': services,
        'staff': staff
    }
    return render(request, 'it_service.html', context=context)


def blog_detail(request):
    if request.method == 'POST':
        form = PostCommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    new_comment = PostComment.objects.all()

    form = PostCommentForm()
    comment_data = {'form': form,
                    'new_comment': new_comment}

    return render(request, template_name='it_blog_detail.html',context=comment_data)




