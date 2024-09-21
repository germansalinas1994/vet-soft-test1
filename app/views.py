from django.shortcuts import get_object_or_404, redirect, render, reverse

from .models import (
    Breed,
    CityEnum,
    Client,
    Medicine,
    Pet,
    Product,
    Provider,
    Speciality,
    Vet,
)


def home(request):
    """"Esta funcion mostrará el home"""
    return render(request, "home.html")


def clients_repository(request):
    """"Esta funcion mostrará los clientes cargados"""
    clients = Client.objects.all()
    return render(request, "clients/repository.html", {"clients": clients})


def clients_form(request, id=None):
    """"Esta funcion guarda un cliente nuevo"""
    ciudades = CityEnum.choices
    if request.method == "POST":
        client_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if client_id == "":
            saved, errors = Client.save_client(request.POST)
        else:
            client = get_object_or_404(Client, pk=client_id)
            saved,errors = client.update_client(request.POST)

        if saved:
            return redirect(reverse("clients_repo"))

        return render(
            request, "clients/form.html", {"errors": errors, "client": request.POST, "ciudades": ciudades},
        )

    client = None
    if id is not None:
        client = get_object_or_404(Client, pk=id)

    return render(request, "clients/form.html", {"client": client, "ciudades": ciudades})


def clients_delete(request):
    """"Esta funcion elimina un cliente según un ID"""
    client_id = request.POST.get("client_id")
    client = get_object_or_404(Client, pk=int(client_id))
    client.delete()

    return redirect(reverse("clients_repo"))


def vets_repository(request):
    """"Esta funcion mostrará los veterinarios cargados"""
    vets = Vet.objects.all()
    return render(request, "vets/repository.html", {"vets": vets})



def vets_form(request, id=None):
    """"Esta funcion guarda un veterinario nuevo"""
    specialities = Speciality.choices

    if request.method == "POST":
        vet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if vet_id == "":
            saved, errors = Vet.save_vet(request.POST)
        else:
            vet = get_object_or_404(Vet, pk=vet_id)
            saved,errors = vet.update_vet(request.POST)

        if saved:
            return redirect(reverse("vets_repo"))

        return render(
            request, "vets/form.html", {"errors": errors, "vet": request.POST, "specialities": specialities},
        )

    vet = None
    if id is not None:
        vet = get_object_or_404(Vet, pk=id)


    return render(request, "vets/form.html", {"vet": vet, "specialities": specialities})

def vets_delete(request):
    """"Esta funcion elimina un veterinario según un ID"""
    vet_id = request.POST.get("vet_id")
    vet = get_object_or_404(Vet, pk=int(vet_id))
    vet.delete()

    return redirect(reverse("vets_repo"))

def providers_repository(request):
    """"Esta funcion mostrará los proveedores cargados"""
    providers = Provider.objects.all()
    return render(request, "providers/repository.html", {"providers": providers})

def providers_form(request, id=None):
    """"Esta funcion guarda un proveedor nuevo"""
    if request.method == "POST":
        provider_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if provider_id == "":
            saved, errors = Provider.save_provider(request.POST)
        else:
            provider = get_object_or_404(Provider, pk=provider_id)
            provider.update_provider(request.POST)

        if saved:
            return redirect(reverse("providers_repo"))

        return render(
            request, "providers/form.html", {"errors": errors, "provider": request.POST},
        )

    provider = None
    if id is not None:
        provider = get_object_or_404(Provider, pk=id)

    return render(request, "providers/form.html", {"provider": provider})

def providers_delete(request):
    """"Esta funcion elimina un proveedor según un ID"""
    provider_id = request.POST.get("provider_id")
    provider = get_object_or_404(Provider, pk=int(provider_id))
    provider.delete()

    return redirect(reverse("providers_repo"))



#Views Pets

def pets_repository(request):
    """"Esta funcion mostrará las mascotas cargadas"""
    pets = Pet.objects.all()
    return render(request, "pets/repository.html", {"pets": pets})



def pets_form(request, id=None):
    """"Esta funcion guarda una mascota nueva"""
    breeds = Breed.choices


    if request.method == "POST":
        pet_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if pet_id == "":
            saved, errors = Pet.save_pet(request.POST)
        else:
            pet = get_object_or_404(Pet, pk=pet_id)
            saved,errors = pet.update_pet(request.POST)

        if saved:
            return redirect(reverse("pets_repo"))

        return render(
            request, "pets/form.html", {"errors": errors, "pet": request.POST, "breeds": breeds},
        )

    pet = None
    if id is not None:
        pet = get_object_or_404(Pet, pk=id)

    return render(request, "pets/form.html", {"pet": pet, "breeds": breeds})

def pets_delete(request):
    """"Esta funcion elimina una mascota según un ID"""
    pet_id = request.POST.get("pet_id")
    pet = get_object_or_404(Pet, pk=int(pet_id))
    pet.delete()

    return redirect(reverse("pets_repo"))


def medicines_repository(request):
    """"Esta funcion mostrará las medicinas cargadas"""
    medicines = Medicine.objects.all()
    return render(request, "medicines/repository.html", {"medicines": medicines})


def medicines_form(request, id=None):
    """"Esta funcion guarda una medicina nueva"""
    if request.method == "POST":
        medicine_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if medicine_id == "":
            saved, errors = Medicine.save_medicine(request.POST)
        else:
            medicine = get_object_or_404(Medicine, pk=medicine_id)
            saved, errors = medicine.update_medicine(request.POST)

        if saved:
            return redirect(reverse("medicines_repo"))

        return render(
            request, "medicines/form.html", {"errors": errors, "medicine": request.POST},
        )

    medicine = None
    if id is not None:
        medicine = get_object_or_404(Medicine, pk=id)

    return render(request, "medicines/form.html", {"medicine": medicine})


def medicines_delete(request):
    """"Esta funcion elimina una medicina según un ID"""
    medicine_id = request.POST.get("medicine_id")
    medicine = get_object_or_404(Medicine, pk=int(medicine_id))
    medicine.delete()

    return redirect(reverse("medicines_repo"))




def products_repository(request):
    """"Esta funcion mostrará los productos cargados"""
    products = Product.objects.all()
    return render(request, "products/repository.html", {"products": products})

def products_form(request, id=None):
    """"Esta funcion guarda un producto nuevo"""
    if request.method == "POST":
        product_id = request.POST.get("id", "")
        errors = {}
        saved = True

        if product_id == "":
            saved, errors = Product.save_product(request.POST)
        else:
            product = get_object_or_404(Product, pk=product_id)
            product.update_product(request.POST)

        if saved:
            return redirect(reverse("products_repo"))

        return render(
            request, "products/form.html", {"errors": errors, "product": request.POST},
        )

    product = None
    if id is not None:
        product = get_object_or_404(Product, pk=id)

    return render(request, "products/form.html", {"product": product})


def products_delete(request):
    """"Esta funcion elimina un producto según un ID"""
    product_id = request.POST.get("product_id")
    product = get_object_or_404(Product, pk=int(product_id))
    product.delete()

    return redirect(reverse("products_repo"))
