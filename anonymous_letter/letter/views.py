from django.conf import settings
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from letter.models import Letter
from letter.serializers import CreateLetterSerializer, LetterSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    lookup_field = 'codeword'

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLetterSerializer

        return LetterSerializer


class GetPubKeyView(APIView):
    """
    This view can be deleted - then pubkey must be set on frontend
    """

    def get(self, request, *args, **kwargs):
        return Response(settings.BOSS_PUBKEY)
