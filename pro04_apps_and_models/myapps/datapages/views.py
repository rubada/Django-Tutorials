from django.shortcuts import render


def data_page_view(request):
    # Create a data lists:

    employees_data = [
        {"name": "John", "role": "Manager"},
        {"name": "Sara", "role": "Sales"},
        {"name": "Mike", "role": "Marketing"},
    ]

    products_data = [
        "Laptop",
        "Smartphone",
        "Headphones",
        "Camera"
    ]

    # The context should be a dictionary:
    context = {
        "employees": employees_data,
        "products": products_data,
    }
    return render(request, "datapages/information.html", context=context)
