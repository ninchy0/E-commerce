from django.shortcuts import render
from .models import *
from django.views.generic import View

# Create your views here.
class BaseView(View):
    views = {}
    views['category'] = Category.objects.filter(status = 'active')

class HomeView(BaseView):
    def get(self, request):
        self.views['sliders'] = Slider.objects.filter(status = 'active')
        self.views['ads'] = Ad.objects.all()
        self.views['brands'] = Brand.objects.filter(status = 'active')
        self.views['hots'] = Item.objects.filter(status = 'active', label = 'hot')
        self.views['news'] = Item.objects.filter(status='active', label='new')

        return render(request, 'index.html', self.views)

class CategoryItemView(BaseView):
    def get(self, request, slug):
        category_id = Category.objects.get(slug=slug).id
        self.views['cat_items'] = Item.objects.filter(category = category_id)
        return render(request, 'category.html', self.views)


# BRANDS KO ADAR MA VIEW GARNE