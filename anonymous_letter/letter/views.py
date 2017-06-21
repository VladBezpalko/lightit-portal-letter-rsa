from rest_framework import viewsets

from letter.models import Letter
from letter.serializers import CreateLetterSerializer, LetterSerializer


class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    lookup_field = 'codeword'

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLetterSerializer

        return LetterSerializer
