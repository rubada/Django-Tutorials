from django.db import migrations, models
from django.utils.text import slugify


def generate_unique_slugs(apps, schema_editor):
    """Generate unique slugs for existing posts"""
    Post = apps.get_model('blog_core', 'Post')
    seen_slugs = set()

    for post in Post.objects.all():
        # Replace 'title' with the field you want to slugify
        base_slug = slugify(post.title)
        slug = base_slug

        # The counter in the while loop ensures uniqueness and only adds a
        # number when there is a duplicate title:
        counter = 1
        while slug in seen_slugs or Post.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1

        seen_slugs.add(slug)
        post.slug = slug
        post.save()


class Migration(migrations.Migration):

    dependencies = [
        ('blog_core',
         '0002_remove_post_first_name_remove_post_last_name_and_more'),
    ]

    operations = [
        # Step 1: Add slug column as non-unique first
        migrations.AddField(
            model_name='post',
            name='slug',
            # unique=False temporarily
            field=models.SlugField(blank=True, null=True, unique=False),
        ),
        # Step 2: Populate slugs for existing rows by running the RunPython
        migrations.RunPython(
            generate_unique_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
        # Step 3: Now enforce unique=True
        migrations.AlterField(
            model_name='post',
            name='slug',
            # final state
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]


# The orignal generated class:
# class Migration(migrations.Migration):

#     dependencies = [
#         ('blog_core',
#          '0002_remove_post_first_name_remove_post_last_name_and_more'),
#     ]

#     operations = [
#         migrations.AddField(
#             model_name='post',
#             name='slug',
#             field=models.SlugField(blank=True, null=True, unique=True),
#         ),
#     ]
