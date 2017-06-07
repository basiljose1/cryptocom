from rest_framework.response import Response
from rest_framework.views import APIView
from core.api.serializers import TokenSerializer

class TokenView(APIView):
	
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        msg = serializer.validated_data['msg']
        return Response(msg, status=msg['status_code'])

    def get(self, request, format=None):
    	msg = {
                'status':'failure',
                'errors':'GET Method not allowed.',
                'status_code':405
                }
        return Response(msg, status=msg['status_code'])