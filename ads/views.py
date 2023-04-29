from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Ad
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from .serializers import AdListSerializer, AdDetailSerializer, AdCreateSerializer, AdUpdateSerializer, AdDestroySerializer
from rest_framework.permissions import IsAuthenticated
from ads.permissions import IsOwnerOrAdminOrModerator


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer

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


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDestroySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrModerator]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrModerator]


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
