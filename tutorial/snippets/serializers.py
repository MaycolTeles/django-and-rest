"""
Module containing the serializer classes.
"""

from typing import Any

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


JSON = dict[str, Any]


class SnippetSerializer(serializers.Serializer):
    """
    Serializer to the Snippet Class.

    This class serializes and deserializes the snippet instances into representations,
    such as JSON.
    """
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data: JSON) -> Snippet:
        """
        Method to create a new snippet of code.

        This method implements the REST interface.

        Parameters
        ----------
        validated_data : JSON
            The JSON received from the API.

        Returns
        -------
        Snippet
            The recently created Snippet instance.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance: Snippet, validated_data: JSON) -> Snippet:
        """
        Method to update the Snippet based on the validated_data (both received as argument).

        This method implements the REST interface.

        Implementation: This method updates the field if it was received. If not, keeps the former value.

        Parameters
        ----------
        instace : Snippet
            The Snippet to be updated.

        validated_data : JSON
            The JSON received in the API containing data to update the Snippet.

        Returns
        -------
        Snippet
            The updated Snippet.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)

        instance.save()
        return instance
