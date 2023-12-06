from django.http import JsonResponse
# Create your views here.

def api_view(request, *args, **kwargs):
    return JsonResponse({"message":"Oombillaaa"})