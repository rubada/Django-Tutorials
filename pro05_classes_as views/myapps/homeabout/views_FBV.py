from django.shortcuts import render


def home_page_view(request):
    return render(request, "homepage.html")


def about_page_view(request):
    page_context = {
        "name": "Ruba Dabbas",
        "about_page": "we will learn about Django",
    }
    return render(
        request,
        "about.html",
        context=page_context
    )
