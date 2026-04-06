from django.views.generic import TemplateView


class DataPageView(TemplateView):
    template_name = "datapages/information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Add your custom data
        context["employees"] = [
            {"name": "John", "role": "Manager"},
            {"name": "Sara", "role": "Sales"},
            {"name": "Mike", "role": "Marketing"},
        ]

        context["products"] = [
            "Laptop",
            "Smartphone",
            "Headphones",
            "Camera"
        ]

        return context
