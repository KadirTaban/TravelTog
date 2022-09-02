from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .serializers import HomeSerializer
from home.models import Journey

# Create your views here.


class HomeView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token,'secret',algorithm=['HS256'])
        except jwt.ExpiredSignatureError:  
            raise AuthenticationFailed('Unauthenticated!')

        journey = Journey.objects.filter(id=payload['id']).first()
        serializer = HomeSerializer(journey)


        return Response(serializer.data)