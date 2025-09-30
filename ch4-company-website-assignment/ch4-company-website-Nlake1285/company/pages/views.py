# pages/views.py
from django.shortcuts import render
from django.views.generic import TemplateView  # new


# Create your views here.
def home_page_view(request):        # new
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for visiting!"
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):   # new
    template_name = "about.html"
    
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context

class ProductPageView(TemplateView):  # new
    template_name = "products.html"
    
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context["product_list"] = [
            {"name": "Widget 1", "price": 19.99},
            {"name": "Widget 2", "price": 29.99},
            {"name": "Widget 3", "price": 39.99},
            {"name": "Widget 4", "price": 49.99},
        ]
        return context