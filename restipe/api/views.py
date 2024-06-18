from django.http import JsonResponse, HttpResponse
import json
from django.db.models import Q
from .models import Recipe

# Create your views here.
def root(request):
    if request.method == "GET":
        return list(request)
    elif request.method == "POST":
        return create(request)
    return HttpResponse(status=405)

def single(request, id):
    if request.method == "GET":
        return get(request,id)
    elif request.method == "PUT":
        return update(request,id)
    elif request.method == "DELETE":
        return delete(request,id)
    return HttpResponse(status=405)


def create(request):
    body = json.loads(request.body.decode('utf-8'))
    # not the best, too copy-pasted
    if "title" not in body: return HttpResponse(status=400) 
    if "description" not in body:return HttpResponse(status=400) 
    if "ingredients" not in body: return HttpResponse(status=400) 
    if "instructions" not in body:return HttpResponse(status=400) 
    if "category" not in body: return HttpResponse(status=400) 
    
    r = Recipe(title=body["title"], description=body["description"],ingredients="\n".join(body["ingredients"]),instructions="\n".join(body["instructions"]),category=body["category"])
    r.save()

    return HttpResponse(status=200)




def list(request):
    recepies = Recipe.objects.order_by("id")
    output = {}
    for recepie in recepies:
        output[recepie.id] = recepie.title
    return JsonResponse(output)

def get(request,id):
    try:
        r = Recipe.objects.get(id=id)
        output = {
            "title":r.title,
            "description":r.description,
            "ingredients":r.ingredients,
            "instructions":r.instructions,
            "category":r.category,
        }

        return JsonResponse(output)
    except:
        return HttpResponse(status=400)

def update(request,id):
    body = json.loads(request.body.decode('utf-8'))
    try:
        r = Recipe.objects.get(id=id)
        if "title" in body: r.title = body["title"]
        if "description" in body: r.description = body["description"]
        if "ingredients" in body: r.ingredients = body["ingredients"]
        if "instructions" in body: r.instructions = body["instructions"]
        if "category" in body: r.category = body["category"] 
        r.save()
        return HttpResponse()
    except:
        return HttpResponse(status=400)


def delete(request,id):
    try:
        r = Recipe.objects.get(id=id)
        r.delete()
        return HttpResponse()
    except:
        return HttpResponse(status=400)

def search(request):
    q = request.GET.get('q', '')
    recepies = Recipe.objects.filter(Q(category__startswith=q) | Q(title__startswith=q))
    output = {}
    for recepie in recepies:
        output[recepie.id] = recepie.title
    return JsonResponse(output)