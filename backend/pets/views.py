from django.http import JsonResponse
from .models import Pet

def listar_pets(request):
    pets = Pet.objects.all().values()
    return JsonResponse(list(pets), safe=False)

def listar_por_status(request, status_pet):
    pets = Pet.objects.filter(status=status_pet).values()
    return JsonResponse(list(pets), safe=False)