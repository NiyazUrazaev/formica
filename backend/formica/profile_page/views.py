from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile


class ProfilePageInfoView(APIView):

    def get(self, request):

        profile_id = request.GET.get('profile_id', None)
        if profile_id is None:
            return Response(status=400, data='No profile_id in kwargs!')

        try:
            profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Response(status=400, data='No profile with this id!')

        return Response(status=200, data=model_to_dict(profile, exclude=('password', 'avatar')))

    def post(self, request):
        pass


class MyProfileView(APIView):

    def get(self, request):

        # Fixme: Че-то тут нет id
        profile_id = request.user.id
        if profile_id is None:
            return Response(status=403, data='The user is not logged in')

        try:
            profile = Profile.objects.get(id=profile_id)
        except Profile.DoesNotExist:
            return Response(status=400, data='No profile with this id!')

        return Response(status=200, data=model_to_dict(profile, exclude=('password', 'avatar')))