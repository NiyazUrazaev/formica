from django.forms import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response

from aim.models import UserAim


class GetUserAimsView(APIView):

    def get(self, request):

        profile_id = request.GET.get('profile_id', None)
        if profile_id is None:
            return Response(status=400, data='No profile_id in kwargs!')

        user_aims = UserAim.objects.filter(profile__id=profile_id).select_related('aim')
        data = []
        for user_aim in user_aims:
            model_entry = {
                'user_aim': model_to_dict(user_aim),
                'aim': model_to_dict(user_aim.aim, exclude=('picture',))
            }
            data.append(model_entry)

        return Response(status=200, data=data)

    def post(self, request):
        pass