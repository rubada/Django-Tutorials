from django.shortcuts import render

from .models import Posts


def posts_page(request):
    emp_data = Posts.objects.all()
    return render(
        request,
        "posts/posts_display.html",
        {"emp_data": emp_data},
    )
