# Forms:
# In Django, Forms are a powerful toolset designed to handle user input. While
# you could technically write raw HTML <form> tags and manually parse the data
# in your views, Django Forms automate the heavy lifting—specifically
# rendering, validation, and security.

# Think of a Django Form as a bridge between the raw data a user types into a
# browser and the structured data your Python backend needs.

# Core Responsibilities
# 1. Rendering HTML: Instead of writing every <input> and <label> manually,
# you define a form class in Python, and Django generates the HTML for you.

# 2. Validation: It ensures the data matches your requirements (e.g., an email
# field actually contains an @ symbol, or a password is long enough).

# 3. Data Cleaning: It converts string input from the browser into Python
# objects, like converting "2026-04-22" into a datetime.date object.

# 4. Security: It automatically handles CSRF (Cross-Site Request Forgery)
# tokens to protect your site from malicious attacks.

# Now, we will discuss two types of forms in Django:
# 1. forms.Form
# 2. forms.ModelForm

# 1. forms.Form is used when when there is no database involved, you just want
# to process, find data, etc., without saving it in the database, such as:
# a. Contact form — sends an email, nothing saved to DB.
# b. Search / Filter Forms.
# c. Login / Authentication Forms
# d. Multi-Step Forms, when you collect data across multiple steps before
# saving it to database.
# Example:
# Step 1 — personal info
'''class PersonalInfoForm(forms.Form):
    first_name = forms.CharField()
    last_name  = forms.CharField()
    age        = forms.IntegerField()'''

# Step 2 — preferences
'''class PreferencesForm(forms.Form):
    language = forms.ChoiceField(choices=[...])
    timezone = forms.ChoiceField(choices=[...])'''

# Final step — combine and save to DB

# And in many other cases where storing the data in your database isn’t
# necessary.

# 2. forms.ModelForm is used whenever your form maps directly to a database
# model and you want to save the data to the database, such as:
# a. Creating a New Record:
# The most common use case a form that creates a new row in the database.
# b. Editing an Existing Record:
# Pass the existing instance to pre-fill the form with current data.
# c. Registering a User:
# User registration maps directly to the User model.
# d. Updating a User Profile:
# When a user updates their profile information.

# And in many other cases where storing the data in your database is
# necessary.

# Both "forms.Form" and "forms.ModelForm" share the same foundation in
# Django’s form system, but we’ll focus on "forms.ModelForm" because it
# directly integrates with models and is the most practical way to learn CRUD
# operations (Create, Read, Update, Delete) in development.
