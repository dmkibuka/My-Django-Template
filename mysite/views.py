from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from .forms import ContactForm

def home_page(request):
    context = {
        "page_title":"My Family | Welcome",
        "brand_name":"Mysite",
        "page_header":"Family Cover your page.",
        "cover_intro":"Cover is a one-page template for building simple and beautiful home pages. Download, edit the text, and add your own fullscreen background photo to make it your own."
    }
    if request.user.is_authenticated:
        context["premium_content"] = "YEAHHHHHH"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "page_title":"About Us",
        "content":" Welcome to the about page."
    }
    return render(request, "about_page.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "page_title":"Contact Us",
        "page_header":" We Love to hear from you",
        "street_adress": "476 Farmington Ave",
        "city": "hartford",
        "state": "ct",
        "zipcode": "06105",
        "phone1": "(255) 555-5555",
        "phone2": "(355) 666-6666",
        "email1": "joedones@email.com",
        "email2": "eventpiters@myemail.com",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact_page.html", context)
