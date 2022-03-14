from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
# from django.template import loader
# Create your views here.

#
# def item_list(request):
#     item = Item.objects.all()
#     template = loader.get_template('food/index.html')
#     context = {
#          'item_list': item,
#     }
#     return HttpResponse(template.render(context, request))

# replace this code in class based view
# def item_list(request):
#     item = Item.objects.all()
#     context = {
#          'item_list': item,
#     }
#     return render(request, 'food/index.html', context)


class IndexView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

# replace this code class based details view
# def item_details(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         'item': item
#     }
#     return render(request, "food/details.html", context)


class ItemDetails(DetailView):
    model = Item
    template_name = 'food/details.html'
    context_object_name = 'item'

# replacing class based view
# def create_item(request):
#     form = ItemForm(request.POST)
#     if form.is_valid():
#         form.save()
#         return redirect('Food:item-list')
#     return render(request, 'food/item_form.html', {'form': form})


class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('Food:item-list')
    return render(request, 'food/item_form.html', {'form': form, 'item' : item})


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('Food:item-list')
    return render(request, 'food/item_delete.html', {'item': item})