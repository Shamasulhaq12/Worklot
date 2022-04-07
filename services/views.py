from rest_framework.views import APIView
from django.shortcuts import render
from django.contrib.auth import get_user_model
# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import JobBidSerializer, PortfolioSerializer, Government_detailsSerializer, ServiceSerializer
from rest_framework.response import Response
from .models import JobBid, Portfolio, Government_details, Service
from django.http import Http404
User = get_user_model()
# Create your views here.


# def file_upload(request):
#     if request.method == 'POST':
#         my_file = request.FILES.get('file')
#         Image.objects.create(image=my_file)
#         return HttpResponse('')
#     return JsonResponse({'post': 'fasle'})


class JobBidListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobBidSerializer

    def get(self, request):
        data = JobBid.objects.all()
        serializer = JobBidSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        jobs = JobBid.objects.all()
        return jobs

    def get_object(self, pk):
        try:
            return JobBid.objects.get(pk=pk)
        except JobBid.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        data = self.request.data
        user = self.request.user
        print(user)
        serializer = JobBidSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate()
        serializer.save()
        return Response(serializer.data, status=201)


class JobBidView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobBidSerializer

    def get(self, request):
        data = JobBid.objects.all()
        serializer = JobBidSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        jobs = JobBid.objects.filter(job_confirm=True)
        return jobs

    def get_object(self, pk):
        try:
            return JobBid.objects.get(pk=pk)
        except JobBid.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobBidSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=204)


class WorkerPortfolioListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        jobs = Portfolio.objects.all()
        return jobs

    def get_object(self, pk):
        try:
            return Portfolio.objects.get(pk=pk)
        except JobBid.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.request.user
        data = Portfolio.objects.filter(pk=user.id)
        serializer = PortfolioSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        data = self.request.data
        user = self.request.user
        serializer = PortfolioSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate()
        serializer.save()
        # obj = Portfolio.objects.create(user=User, about_me=data['about_me'])
        # obj.save()
        return Response(serializer.data, status=201)


class WorkerPortfolioView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        jobs = Portfolio.objects.all()
        return jobs

    def get_object(self, pk):
        try:
            return Portfolio.objects.get(pk=pk)
        except JobBid.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.request.user
        data = Portfolio.objects.filter(pk=user.id)
        serializer = PortfolioSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = PortfolioSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=204)


class Government_detailsList(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = Government_detailsSerializer

    def get_queryset(self):
        detail = Government_details.objects.all()
        return detail

    def get_object(self, pk):
        try:
            return Government_details.objects.get(pk=pk)
        except Government_details.DoesNotExist:
            raise Http404

    def get(self, request):
        user = self.request.user
        data = Government_details.objects.filter(pk=user.pk)
        serializer = Government_detailsSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):

        data = self.request.data
        user = self.request.user
        serializer = Government_detailsSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate()
        serializer.save()
        # obj = Government_details.objects.create(
        #     name=User.name, id_card_Num=data['id_card_Num'])
        # obj.save()
        return Response(serializer.data, status=201)


class Government_detailsView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = Government_detailsSerializer

    def get_queryset(self):
        detail = Government_details.objects.all()
        return detail

    def get_object(self, pk):
        try:
            return Government_details.objects.get(pk=pk)
        except Government_details.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.request.user
        data = Government_details.objects.filter(pk)
        serializer = Government_detailsSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = Government_detailsSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=204)


class ServiceViews(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ServiceSerializer

    def get(self, request):
        data = Service.objects.all()
        serializer = ServiceSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        service = Service.objects.all()
        return service

    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Service.DoesNotExist:
            raise Http404
