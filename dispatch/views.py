from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .models import Client, Message
from .serializers import ClientSerializer, MessageSerializer


@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def login(request):
    new_client = Client.objects.create()
    serializer = ClientSerializer(new_client)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def get_clients(request):
    serializer = ClientSerializer(Client.objects.all(), many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)


@api_view(['GET'])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def get_client(request):
    serializer = ClientSerializer(Client.objects.get(identity=request.query_params.get("identity")))
    return JsonResponse(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def send_message(request):
    author = Client.objects.get(identity=request.data.get("author"))
    # return Response(f'{request.data.get("password")}, {author.password}')
    # return Response(f'{request.data.get("password")}, {author.password}, {not request.data.get("password") is author.password}')
    if request.data.get("password") != author.password:
        return JsonResponse("authentication failed", status=status.HTTP_401_UNAUTHORIZED, safe=False)
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
    return JsonResponse(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST, safe=False)


@api_view(['POST'])
@csrf_exempt
@permission_classes((permissions.AllowAny,))
def get_messages(request):
    addressee = Client.objects.get(identity=request.data.get('addressee'))
    if request.data.get("password") != addressee.password:
        return JsonResponse("authentication failed", status=status.HTTP_401_UNAUTHORIZED)
    serializer = MessageSerializer(Message.get_all_for_client(addressee), many=True)
    return JsonResponse(serializer.data, status=status.HTTP_200_OK, safe=False)

