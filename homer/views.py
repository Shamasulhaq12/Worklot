from rest_framework.generics import ListAPIView
from rest_framework import permissions
from .serializers import JobPostSerializer, ProfileSerializer
from rest_framework.response import Response
from .models import JobPost, Profile
from rest_framework.views import APIView

from django.http import Http404
# Create your views here.


# def file_upload(request):
#     if request.method == 'POST':
#         my_file = request.FILES.get('file')
#         Image.objects.create(image=my_file)
#         return HttpResponse('')
#     return JsonResponse({'post': 'fasle'})


class JobPostListView(ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobPostSerializer

    def get(self, request):
        data = JobPost.objects.all()
        serializer = JobPostSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        jobs = JobPost.objects.filter(job_confirm=True)
        return jobs

    def get_object(self, pk):
        try:
            return JobPost.objects.get(pk=pk)
        except JobPost.DoesNotExist:
            raise Http404

    def post(self, request, format=None):

        data = self.request.data
        user = self.request.user
        serializer = JobPostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # serializer.validate()
        serializer.save()
        return Response(serializer.data, status=201)


class JobPostDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobPostSerializer

    def get(self, request, pk, format=None):
        data = JobPost.objects.filter(pk=pk)
        serializer = JobPostSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        jobs = JobPost.objects.all()
        return jobs

    def get_object(self, pk):
        try:
            return JobPost.objects.get(pk=pk)
        except JobPost.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        job = self.get_object(pk)
        serializer = JobPostSerializer(job, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, pk, format=None):
        job = self.get_object(pk)
        job.delete()
        return Response(status=204)


class ProfileDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = JobPostSerializer

    def get(self, request, pk, format=None):
        data = Profile.objects.filter(pk=pk)
        serializer = ProfileSerializer(
            data, context={'request': request}, many=True)
        return Response(serializer.data)
