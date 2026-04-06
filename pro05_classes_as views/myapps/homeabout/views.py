from django.views.generic import TemplateView


# TemplateView is a built-in class-based generic view used to render a
# specific template with optional context data. It’s best suited for static
# or simple pages that don’t require complex logic or form handling.

# - Purpose: Renders an HTML template with context variables.
# - Base Class: Inherits from Django’s View class.
# - Template Specification: You define the template using the template_name
# attribute.
# - Context Handling: You can override get_context_data() method to pass extra
# data into the template.

# - Best Use Cases:
# - WebPages with static or simple dynamic context (e.g., About, Terms, Privacy
# Policy), WebPages that only need GET requests.
# - Simple informational webpages without forms, authentication (where POST
# requests are used), or heavy database queries.
# GET requests, such as getting the context, return the HTML.
# POST requests are used when the client (browser, API consumer, etc.) wants to
# send data to the server, such as login forms (username + password),
# uploading a file, etc.

class HomePageView(TemplateView):
    template_name = "homepage.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "Ruba Dabbas"
        context["about_page"] = "we will learn about Django"
        return context
