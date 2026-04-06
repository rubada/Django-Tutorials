# Class-Based Views (CBVs):

# Function-based views (FBVs) are simpler and explicit, while class-based
# views (CBVs) are more reusable and structured, why?
# Function-based views lack the means of inheritance, meaning developers
# must repeat the same code in each view. That violates the coding general
# rule DRY (Don’t Repeat Yourself).

# FBVs are ideal for small, straightforward logic, whereas CBVs shine in
# larger projects where inheritance and built-in generic views reduce
# duplication.

# For example:
# If the webpages share a similar layout and logic, but differ in data
# source (model/queryset) or minor context. Using a CBV is a better approach,
# instead of creating multiple FBVs and/or multiple applications.

# Main Categories of Built-in CBVs:
# 1. Simple Views
# - View → Base class for all CBVs.
# - TemplateView → Renders a template with optional context.
# - RedirectView → Redirects to a given URL.

# 2. Generic Display Views
# - DetailView → Displays a single object.
# - ListView → Displays a list of objects.

# 3. Generic Editing Views
# - FormView → Displays and processes a form.
# - CreateView → Creates a new object (model instance).
# - UpdateView → Updates an existing object.
# - DeleteView → Deletes an object.

# 4. Generic Date Views
# - ArchiveIndexView → Displays a list of objects by date.
# - YearArchiveView → Groups objects by year.
# - MonthArchiveView → Groups objects by month.
# - WeekArchiveView → Groups objects by week.
# - DayArchiveView → Groups objects by day.
# - TodayArchiveView → Displays objects for the current day.
# - DateDetailView → Displays a single object for a specific date
