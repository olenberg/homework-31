from django.db.models import Q, Count
from django.shortcuts import render
from .models import User, Location
import json
from avito import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.http import JsonResponse


class UserList(ListView):
    model = User
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        paginator = Paginator(self.object_list.annotate(total_ads=Count("ad", filter=Q(ad__is_published__gte=True)))
                              .select_related("location").order_by("username"), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        users = []
        for user in page_obj:
            users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.first_name,
                "username": user.username,
                "password": user.password,
                "role": user.role,
                "age": user.age,
                "location": user.location.name,
                "total_ads": user.total_ads
            })

        response = {
            "items": users,
            "total": paginator.count,
            "num_page": paginator.num_pages,
        }
        return JsonResponse(response, safe=False, json_dumps_params={"ensure_ascii": False})

class UserDetail(DetailView):
    model = User
    def get(self, *args, **kwargs):
        user = self.get_object()
        response = {
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "location": str(user.location)
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


class UserDelete(DeleteView):
    model = User
    success_url = "users/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class UserCreate(CreateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "password", "age", "location"]
    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            password=user_data["password"],
            age=user_data["age"]
        )
        location, created = Location.objects.get_or_create(name=user_data.get('location'))
        user.location = location
        user.save()
        response = {
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "location_id": user.location_id,
            "location": str(user.location)
        }
        return JsonResponse(response, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name="dispatch")
class UserUpdate(UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "password", "age", "location"]
    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.username = user_data["username"]
        self.object.password = user_data["password"]
        self.object.role = user_data["role"]
        self.object.age = user_data["age"]
        location, created = Location.objects.get_or_create(name=user_data.get('location'))
        self.object.location = location
        self.object.save()
        response = {
            'id': self.object.id,
            'username': self.object.username,
            'first_name': self.object.first_name,
            'last_name': self.object.last_name,
            'role': self.object.role,
            'age': self.object.age,
            'location_id': self.object.location_id,
            'location': str(self.object.location)
        }
        return JsonResponse(response,json_dumps_params={"ensure_ascii": False})
