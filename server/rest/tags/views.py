from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from tags.models import Tag
from tags.serializers import TagSerializer

class JSONResponse (HttpResponse):
	"""
	An HttpResponse that renders its content to JSON
	"""

	def __init__ (self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs ['content_type'] = 'application/json'
		super (JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def tag_list (request):
	"""
	List all tags, or push a new tag
	"""
	if request.method == 'GET':
		tags = Tag.objects.all()
		serializer = TagSerializer (tags, many=True)
		return JSONResponse (serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = TagSerializer (data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse (serializer.data, status=201)
		return JSONResponse (serializer.errors, status=400)

@csrf_exempt
def tag_detail (request, pk):
	"""
	Retrieve, update or delete a tag.
	"""
	try:
		tag = Tag.objects.get (pk=pk)
	except Tag.DoesNotExist:
		return HttpResponse (status=404)

	if request.method == 'GET':
		serializer = TagSerializer (tag)
		return JSONResponse (serializer.data)

	if request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = TagSerializer (tag, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse (serializer.data)
		return JSONResponse (serializer.errors, status=400)

	elif request.method == 'DELETE':
		tag.delete()
		return HttpResponse(status=204)