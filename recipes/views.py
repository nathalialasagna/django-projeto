# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_list_or_404, render

from recipes.models import Recipe

# from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        # [make_recipe() for _ in range(10)]
    })


def category(request, category_id):

    #    recipes = Recipe.objects.filter(
    #        category__id=category_id, is_published=True,).order_by('-id')
    #
    #     category_name = getattr(
    #        getattr(recipes.first(), 'Category', None), 'name', 'Not found')

    #    if not recipes:
    #     return HttpResponse(content='Not Found', status=404)
    #          raise Http404('Not Found')

    recipes = get_list_or_404(Recipe.objects.filter(
        category__id=category_id, is_published=True,).order_by('-id'))

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
        # 'title': f'{recipes.first().category.name}'
        # [make_recipe() for _ in range(10)]
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        id=id).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        # 'recipe': make_recipe(),
        'recipe': recipe,
        'is_detail_page': True,
    })
