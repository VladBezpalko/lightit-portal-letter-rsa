from rest_framework import serializers

from letter.models import Letter


class CreateLetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('message', )


class LetterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Letter
        fields = ('message', 'response')
        read_only_fields = ('message', )
