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


# class CategoryListView(ListView):
#     model = Category
#     template_name = "hierarchy/category_list.html"


@login_required
def group_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    object_list = Post.objects.filter(category=category)
    template = 'hierarchy/post_list.html'

    post_list = Category.objects.filter(parent_id=category.id)
    # print('!!!!!!!!!!!!self.title:', drilldown_tree_for_node(node=2))
    category_tree = Category.objects.filter(id=category.parent_id)
    # print('!!!!!!!!!!!!category_tree:', category_tree)

    context = {
        'object_list': object_list,
        'post_list': post_list,
        'category': category,
        'category_tree': category_tree,
    }
    return render(request, template, context)


# class PostByCategoryView(ListView):
#     context_object_name = 'posts'
#     template_name = 'hierarchy/post_list.html'

#     def get_queryset(self):
#         self.category = Category.objects.get(slug=self.kwargs['slug'])
#         queryset = Post.objects.filter(category=self.category)
#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.category
#         return context
