from django.conf import settings
from rest_framework.decorators import detail_route
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, RetrieveModelMixin
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from letter.models import Letter
from letter.permissions import IsAdmin
from letter.serializers import CreateLetterSerializer, LetterSerializer


class LetterViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,
                    GenericViewSet):
    queryset = Letter.objects.all()
    lookup_field = 'codeword'

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLetterSerializer

        return LetterSerializer

    @detail_route(methods=['POST'])  # permission_classes=[IsAdmin]
    def respond(self, request, codeword=None):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class GetPubKeyView(APIView):
    """
    This view can be deleted - then pubkey must be set on frontend
    """

    def get(self, request, *args, **kwargs):
        return Response(settings.BOSS_PUBKEY)
