from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from core.api.serializers import TokenSerializer
from core.models import Token

class TokenView(APIView):
    serializer_class = TokenSerializer
    queryset = Token.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        msg = {
                'status':['success'],
                'errors':[]
                }
        return Response(msg, status=status.HTTP_200_OK)

    def get(self, request, format=None):
    	msg = {
                'status':['failure'],
                'errors':['GET Method not allowed.']
                }
        return Response(msg, status=status.HTTP_405_METHOD_NOT_ALLOWED)