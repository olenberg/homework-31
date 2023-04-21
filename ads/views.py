from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
import json
from .models import Ad
from categories.models import Category
from avito import settings
from users.models import User
from rest_framework.generics import ListAPIView
from .serializers import AdsListSerializer


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsListSerializer

    def get(self, request, *args, **kwargs):
        category_id = request.GET.get("cat", None)
        if category_id:
            self.queryset = self.queryset.filter(category_id__exact=category_id)

        ad_text = request.GET.get("text", None)
        if ad_text:
            self.queryset = self.queryset.filter(name__icontains=ad_text)

        location_name = request.GET.get("location", None)
        if location_name:
            self.queryset = self.queryset.filter(author__location__name__icontains=location_name)

        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)
        if price_from and price_to:
            self.queryset = self.queryset.filter(price__range=(price_from, price_to))

        return super().get(self, request, *args, **kwargs)


class AdList(ListView):
    model = Ad
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list =self.object_list.select_related("author").order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        ads = []
        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "author": ad.author.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category_id,
                "location": ad.author.location_id,
                "image": ad.image.url if ad.image else None
            })
        response = {
            "items": ads,
            "total": paginator.count,
            "num_pages": paginator.num_pages
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class AdDetail(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": ad.category.name,
            "image": ad.image.url if ad.image else None,
            "location": ad.author.location_id
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class AdDelete(DeleteView):
    model = Ad
    success_url = "ads/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdCreate(CreateView):
    model = Ad
    fields = ["name", "author", "price", "description", "category", "image"]
    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ad.objects.create(
            name=ad_data["name"],
            author=get_object_or_404(User, pk=ad_data['author_id']),
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            category=get_object_or_404(Category, pk=ad_data["category_id"])
        )
        ad.save()
        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "category_id": ad.category_id
        })

@method_decorator(csrf_exempt, name="dispatch")
class AdUpdate(UpdateView):
    model = Ad
    fields = ["name", "author", "price", "description", "is_published", "category", "image"]
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]
        self.object.author = get_object_or_404(User, pk=ad_data["author"])
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.is_published = ad_data["is_published"]
        self.object.category = get_object_or_404(Category, pk=ad_data["category"])
        self.object.image = ad_data["image"]
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author_id,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category_id": self.object.category_id
        })


@method_decorator(csrf_exempt, name="dispatch")
class AdImage(UpdateView):
    model = Ad
    fields = ["logo"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.logo = request.FILES["logo"]
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "logo": self.object.logo.url if self.object.logo else None
        })
