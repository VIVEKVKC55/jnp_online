from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from account.models import Wishlist
from catalog.models import Product

class WishlistView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'default/account/wishlist/list.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        """Retrieve wishlist items for the logged-in user"""
        return Wishlist.objects.filter(user=self.request.user)


class ToggleWishlistView(LoginRequiredMixin, View):
    """Handles adding/removing products from the wishlist with AJAX support."""

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get("pk"))  # Ensure this ID exists
        wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

        if created:
            return JsonResponse({"status": "added", "product_id": product.id})
        else:
            wishlist_item.delete()
            return JsonResponse({"status": "removed", "product_id": product.id})
