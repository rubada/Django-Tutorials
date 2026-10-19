# Email Configuration for Password Reset
# Password reset involves two stages:

# 1. Development Stage
# In development, you don’t need to send real emails — you just want to see
# what would be sent.
# Add this to settings.py:
"""
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
"""
# With the console backend, Django prints the entire email (headers, subject,
# body, reset link) directly to your runserver terminal.
# Copy the reset link from the console to test the flow.

# Note on Reset Links in Console
# When Django prints password reset emails to the console, long URLs may be
# wrapped using quoted‑printable encoding. This can insert a "=" at the end of
# a line, which browsers interpret as "%3D".

# Example (wrapped link):
# http://127.0.0.1:8000/accounts/reset/MQ/dckxwp-d8846e11e008b7d25489c09b17985c=
# f4/
# This stray "= or %3D" makes the token invalid.

# Always copy the full URL as one continuous string, removing any line breaks
# or "=" characters.

# 2. Production: Real SMTP Delivery
# To enable password reset emails in production, you must configure Django
# with a real email service instead of the console backend.

# a. Configure Email Backend
# In production, switch to an SMTP backend or a transactional email provider
# (e.g., SendGrid, Amazon SES, Gmail).

# In the settings.py add:
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
"""

# b. Set SMTP Credentials
# Provide Django with the correct server, port, and authentication details.

# Example: SendGrid
# In the settings.py add:
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'  # often not a real email
EMAIL_HOST_PASSWORD = 'SG.xxxxxxxxxxxxxxxxxx'  # your secret API key
DEFAULT_FROM_EMAIL = 'noreply@yourdomain.com'
"""

# Example: Gmail if you want to test the email configuration:
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'youraddress@gmail.com'
EMAIL_HOST_PASSWORD = 'your-16-char-app-password'
DEFAULT_FROM_EMAIL = 'youraddress@gmail.com'
"""

# Important Notes:

# EMAIL_HOST_USER: Often an API key username, not a real email address.

# EMAIL_HOST_PASSWORD: Your secret API key or app password.

# DEFAULT_FROM_EMAIL: The sender address users see (commonly
# noreply@yourdomain.com).

# Security best practice: Store credentials in a .env file and load them with
# a library like django-environ.

# 📺 For more on .env setup, see Intuidemy tutorials:
# https://youtube.com/shorts/Ohw86eJxY7s
# https://youtube.com/shorts/nQhtFbuzVRg

# Add the following settings to enable console email (for development) and
# SMTP email (for production) using .env file:
# In settings.py:

"""
import environ          # Install the package: pip install django-environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

DEBUG = env.bool('DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = env('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')
"""

# ✅ With these configurations in settings.py, Django will send real password
# reset emails in production stage.
