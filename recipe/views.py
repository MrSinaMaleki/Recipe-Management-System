from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipe.models import Recipe
from recipe.serializer import RecipeSerializer


# Create your views here.

def index(request):
    return render(request, 'home.html', {})


@api_view(['GET'])
def recipe_list(request):
    post = Recipe.objects.all()
    serializer = RecipeSerializer(post, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def recipe_create(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
