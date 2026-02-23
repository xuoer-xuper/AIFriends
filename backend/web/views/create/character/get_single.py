from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class GetSingleCharacterView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            character_id = request.GET.get('character_id')
        except:
            return Response({
                'result': '系统异常，请稍后重试'
            })