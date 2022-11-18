"""
Module containing all the views.
"""

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Snippet
from .serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request: HttpRequest) -> JsonResponse:
    """
    Function to list all the snippets of code.

    Parameters
    ----------
    request : HttpRequest
        A Django HTTP Request class model, containing all the request data.

    Returns
    --------
    JsonResponse
        A Django JSON Response class model, containing all the response data.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=request_data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        serializer.save()
        return JsonResponse(serializer.data, status=201)


@csrf_exempt
def snippet_detail(request: HttpRequest, pk: int) -> HttpResponse | JsonResponse:
    """
    Method to show the details of a single snippet of code.

    Parameters
    ----------
    request : HttpRequest
        A Django HTTP Request model, containing all the request data.

    pk : int
        The desired snippet primary key, to find it in the database.

    Returns
    --------
    HttpResponse | JsonResponse
        A Django HTTP/JSON Response model, containing all the response data.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    if request.method == 'PUT':
        request_data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=request_data)

        if not serializer.is_valid():
            return JsonResponse(serializer.errors, status=400)

        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
