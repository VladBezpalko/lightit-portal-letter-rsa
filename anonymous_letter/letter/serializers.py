from rest_framework import serializers

from letter.models import Letter


class CreateLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('message', 'codeword')


class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('message', 'answer', 'codeword')
        read_only_fields = ('message', 'codeword')
