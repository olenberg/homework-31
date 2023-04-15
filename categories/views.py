from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
import json
from .models import Category
from avito import settings


class CategoryList(ListView):
    model = Category

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)
        self.object_list = self.object_list.order_by("name")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        categories = []
        for category in page_obj:
            categories.append({
                "id": category.id,
                "name": category.name,
            })

        response = {
            "items": categories,
            "total": paginator.count,
            "num_page": paginator.num_pages,
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})


class CategoryDetail(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return JsonResponse({
            "id": category.id,
            "name": category.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryUpdate(UpdateView):
    model = Category
    fields = ["name"]
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        category_data = json.loads(request.body)
        self.object.name = category_data["name"]
        self.object.save()
        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        }, safe=False, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class CategoryDelete(DeleteView):
    model = Category
    success_url = "categories/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class CategoryCreate(CreateView):
    model = Category
    fields = ["name"]
    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)
        category = Category.objects.create(name=category_data["name"])
        category.save()
        return JsonResponse({
            "id": category.id,
            "name": category.name,
        })
