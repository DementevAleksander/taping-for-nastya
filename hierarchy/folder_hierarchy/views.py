# from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# from mptt.utils import drilldown_tree_for_node

from .models import Post, Category

User = get_user_model()


def index(request):
    post_list = Category.objects.select_related().all()
    template = 'hierarchy/category_list.html'

    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


def сourse_content(request):
    post_list = Category.objects.select_related().all()
    template = 'hierarchy/сourse_content.html'

    context = {
        'post_list': post_list,
    }
    return render(request, template, context)


@login_required
def group_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = Post.objects.filter(category=category)
    template = 'hierarchy/post_list.html'
    post_list = Category.objects.filter(parent_id=category.id)
    category_tree = Category.objects.filter(id=category.parent_id)
    up_hierarchy = category.get_ancestors(ascending=False, include_self=False)
    # print("!!!!!!!!!!!!!!!!_get_ancestors:", up_hierarchy)

    context = {
        'object_list': object_list,
        'post_list': post_list,
        'category': category,
        'category_tree': category_tree,
        'up_hierarchy': up_hierarchy,
    }
    return render(request, template, context)
