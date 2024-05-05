import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from webhook.serializers import WebhookSerializer
from webhook.services import create_notification


@csrf_exempt
def create_message(request):

    data = json.loads(request.body.decode('utf8').replace("'", '"'))
    serializer = WebhookSerializer(data=data[0])
    if serializer.is_valid():
        create_notification(webhook=serializer.validated_data)
    else:
        return HttpResponse(
            serializer.errors,
            content_type='aplication/json',
            headers={'Access-Control-Allow-Origin': '*'},
            status=400
        )
    return HttpResponse(
        content_type='text/plain',
        headers={'Access-Control-Allow-Origin': '*'},
        status=200
    )