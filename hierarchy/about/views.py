# from django.views.generic.base import TemplateView


# class AboutAuthorView(TemplateView):
#     template_name = 'about/author.html'

from django.shortcuts import render
from folder_hierarchy.models import Category


def aboutauthorview(request):
    post_list = Category.objects.select_related().all()
    template = 'about/author.html'

    context = {
        'post_list': post_list,
    }
    return render(request, template, context)
