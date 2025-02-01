from .models import Category

def menu_categories(request):
    return {'menu_categories': Category.objects.filter(include_in_menu=True)}
