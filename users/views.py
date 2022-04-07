from rest_framework.generics import CreateAPIView
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from homer.models import JobPost
from homer.serializers import JobPostSerializer
from.models import Notification
User = get_user_model()
# from rest_framework.response import Response

# Create your views here.
# Create your views here.


class CustomerView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            useremail = user.email
            username = user.name
            # userfcm = user.fcm_token
            userid = user.id

            job_list = []
            job_post = JobPost.objects.filter(user=userid)
            for job in job_post:
                job_list.append(JobPostSerializer(job).data)

            user = User.objects.get(id=user.id)
            return Response({'useremail': useremail, 'username': username, 'apps': job_list})
        except:
            return Response({'error': 'something went wrong while getting User data'})


class NotificationView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = NotificationSerializer

    def get(self, request, format=None):

        user = self.request.user
        # useremail = user.email
        # username = user.name
        # userfcm = user.fcm_token
        userid = user.id
        # u = user.fcm_token
        # print(username)
        # print(u)
        print("Getting")
        user = self.request.user
        # fcm_tokens = user.fcm_token
        # print(fcm_tokens)
        data = Notification.objects.all()
        serializer = NotificationSerializer(
            data, context={'request': request}, many=True)
        print("sasahshash")
        return Response(serializer.data)

    def get_queryset(self):
        jobs = Notification.objects.all()
        return jobs

    def get_object(self, pk):
        try:
            return Notification.objects.get(pk=pk)
        except Notification.DoesNotExist:
            raise Http404


class NotificationCreateApiView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = NotificationSerializer

    def post(self, request,   format=None):
        data = self.request.data
        user = self.request.user
        fcm_tokens = user.get('fcm_token')
        print(fcm_tokens)
        # serializer.is_valid(raise_exception=True)
        # serializer.validate()
        # serializer.save()
        notification = Notification.objects.create(
            user=user, title=data['title'], description=data['description'], fcm_token=fcm_tokens)
        serializer = NotificationSerializer(notification)
        notification.save()

        return Response(serializer.data, status=201)


# class FcmTokenPost(APIView):
#     permission_classes = (permissions.AllowAny,)
#     serializer_class = FcmTokenSerializer

#     def get(self, request):
#         print("Getting")
#         user = self.request.user
#         username = user.id
#         print(username)
#         data = FcmToken.objects.all()
#         serializer = FcmTokenSerializer(
#             data, context={'request': request}, many=True)
#         print("sasahshash")
#         return Response(serializer.data)

#     def get_queryset(self):
#         jobs = FcmToken.objects.all()
#         return jobs

#     def get_object(self, pk):
#         try:
#             return FcmToken.objects.get(pk=pk)
#         except FcmToken.DoesNotExist:
#             raise Http404

#     def post(self, request, data,   format=None):
#         # data = self.request.data
#         serializer = FcmTokenSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         # serializer.validate()
#         serializer.save()
#         return Response(serializer.data, status=201)

# class NotificationCreateApiView(CreateAPIView):
#     def post(self, request, format=None):
#         try:
#             data = self.request.data
#             user = self.request.user
#             username = user.name
#             # print(data)
#             if not data['title']:
#                 return Response({'error': 'Kindly! Choose your Degree'})

#             job = Notification.objects.get(id=data['user'])

#             if int(data['user']) >= job.user:
#                 notification = Notification.objects.create(
#                     user=user, username=username, title=data['title'], description=data['description'], is_read=data['is_read'])
#                 notification.save()
#                 print("ssasaa")
#             else:

#                 pass
#             return Response({'success': 'order has been placed'})
#         except Exception as e:
#             print(e)
#             return Response({'error': 'error while creating order'})
