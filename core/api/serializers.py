from rest_framework import serializers
from core.models import Token

class TokenSerializer(serializers.Serializer):

    token = serializers.CharField(max_length=8, required=False)

    def validate(self, attrs):

        token = attrs.get('token')

        if token:
            if not Token.objects.filter(key=token).exists():
            	msg = {
                'status':'failure',
                'errors':'Invalid token given.',
                'status_code':400
                }
                # raise serializers.ValidationError(msg)
            else:
                msg = {
                'status':'success',
                'errors':'',
                'status_code':200
                }

        else:
            msg = {
                'status':'failure',
                'errors':'Must include token.',
                'status_code':400
                }
            # raise serializers.ValidationError(msg)

        attrs['msg'] = msg
        return attrs