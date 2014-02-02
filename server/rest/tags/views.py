from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tags.models import Tag
from tags.serializers import TagSerializer


@api_view (['GET', 'POST'])
def tag_list(request, format=None):
	"""
	List all tags, or push a new tag
	"""
	if request.method == 'GET':
		tags = Tag.objects.all()
		serializer = TagSerializer (tags, many=True)
		return Response (serializer.data)

	elif request.method == 'POST':
		serializer = TagSerializer (data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data, status=status.HTTP_201_CREATED)
		return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view (['GET', 'PUT', 'DELETE'])
def tag_detail (request, pk, format=None):
	"""
	Retrieve, update or delete a tag.
	"""
	try:
		tag = Tag.objects.get (pk=pk)
	except Tag.DoesNotExist:
		return Response (status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = TagSerializer (tag)
		return Response (serializer.data)

	if request.method == 'PUT':
		serializer = TagSerializer (tag, data=request.DATA)
		if serializer.is_valid():
			serializer.save()
			return Response (serializer.data)
		return Resposne (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		tag.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)