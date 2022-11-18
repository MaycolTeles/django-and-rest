"""
Module containing the serializer classes.
"""

from typing import Any

from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


JSON = dict[str, Any]


class SnippetSerializer(serializers.ModelSerializer):
    """
    Serializer to the Snippet Class.

    This class serializes and deserializes the snippet instances into representations,
    such as JSON.
    """
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
