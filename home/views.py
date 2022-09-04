from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .serializers import MainFlowSerializer, MyGallerySerializer
from home.models import Journey
from django.http import JsonResponse
from django.template import loader


class MyGalleryView(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token,'secret',algorithm=['HS256'])
        except jwt.ExpiredSignatureError:  
            raise AuthenticationFailed('Unauthenticated!')

        journey = Journey.objects.filter(username=payload['username']).first()
        serializer = MyGallerySerializer(journey)

        return Response(serializer.data)

class MainFlowView(APIView):
    def get(self,request):
        mydata = Journey.objects.all()
        template = loader.get_template('login.html')
        context = {
          'mymembers': mydata,
        }
        print(mydata)
        return HttpResponse(template.render(context, request))
        



