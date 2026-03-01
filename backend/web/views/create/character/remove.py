from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from web.models.character import Character


class RemoveCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            character_id = request.query_params.get('character_id')
            character = Character.objects.get(id=character_id, author__user=request.user)
            return Response({
                'result': 'success'
            })
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })
