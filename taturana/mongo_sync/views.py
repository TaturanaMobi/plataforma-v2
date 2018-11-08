from django.http import JsonResponse
from rest_framework.views import APIView

from mongo_sync.const import ALLOWED_OBJECTS_MAP
from mongo_sync.tasks import sync_task

__all__ = ('Sync',)


class Sync(APIView):

    def post(self, request):
        data = request.data
        if data.get('object') in ALLOWED_OBJECTS_MAP and data.get('hash'):
            sync_task.delay(**data)
            return JsonResponse({'status': 'scheduled'})
        return JsonResponse({'status': 'param_error'})
