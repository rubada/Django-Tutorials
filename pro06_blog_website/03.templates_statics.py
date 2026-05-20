# Create the templates folder.
# Configuration in settings.py:
# Search for the TEMPLATES section, and update the 'DIRS' array to include
# your templates folder.

# The "templates" folder has the following pages:
# 1. "base.html" is a parent template that contains the common HTML
# structure shared across all pages. It typically includes:

# - DOCTYPE, <html>, <head>, <body> tags
# - Navigation bar (header)
# - CSS/JavaScript links
# - Footer
# - Block placeholders where child templates insert their unique content.

# 2. "homepage.html"
# 3. "blog.html"

# Create the static folder, which stores the static assets that don't change
# (CSS files, JavaScript files, images, fonts).
# Configuration in settings.py:
# Update the static files configuration at the bottom of 'settings.py'.

# The "static" folder has the following folders:
# "css" folder contains the "css" files.
# "js" folder contains the "js" files.
# "img" folder contains the image files.
# Other static folders can be created if needed.


# Django template commands:

# Those {% ... %} commands are specific to Django's Template Language (DTL).

# Django-specific syntax includes:

# {% ... %} - Template tags (logic)
# {{ ... }} - Variables (output)
# {% comment %} ... {% endcomment %} - Comments
# {% load %}, {% extends %}, {% block %}, {% if %}, {% for %}, etc.
