from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from api.tracker.models import Entries, Protocol
from django.core import serializers

from api.tracker.serializers import GetProtocolEntriesByUserSerializer
from api.tracker.services.protocol import get_entries_by_user


# Create your views here.


@csrf_exempt
@api_view(("GET",))
@permission_classes((AllowAny,))
def test(request: Request) -> HttpResponse:
    protocol_exercise = Protocol.objects.get(id="2").exercises.all()
    print(protocol_exercise)
    for exercise in protocol_exercise:
        print(
            exercise.name,
            exercise.get_entries_by_user("201faaa9-b5c2-43b7-9840-43211723ff00"),
        )

    # entries = Entries.objects.filter(user_id="201faaa9-b5c2-43b7-9840-43211723ff00", exercise_id="1")

    # json = serializers.serialize("json", protocol_exercise)
    return HttpResponse(status=status.HTTP_200_OK)


@csrf_exempt
@api_view(("GET",))
@permission_classes((IsAuthenticated,))
def get_protocol_entries_by_user(request: Request):
    """
    Get all entries for a user and a protocol
    :param request: UserId (not required), ProtocolId (required), DateFrom (required), DateTo (required)
    :return: list of entries
    """

    request_data = request.data.copy()
    request_data["UserId"] = request.user.id.__str__()
    serializer = GetProtocolEntriesByUserSerializer(data=request_data)
    if serializer.is_valid(raise_exception=True):
        try:
            entries = get_entries_by_user(**serializer.validated_data)
            entries_json = serializers.serialize('json', entries)
            return HttpResponse(entries_json, content_type='application/json', status=status.HTTP_200_OK)
        except ValueError:
            return Response(
                "User or protocol not found", status=status.HTTP_404_NOT_FOUND
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_user_protocols(request: Request):
    pass
