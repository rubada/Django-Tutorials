from django.db import models

# Primary Keys and Foreign Keys:
# - A Primary Key is a unique identifier for each record in a table.
# - Django automatically creates Primary Keys (pk) as id
# (auto-incrementing integer)
# - Every model has a primary key
# - Must be unique for each row
# - Used to identify and fetch specific records
# - Custom Primary Key can be created as follows:


class Post(models.Model):
    # Custom PK name
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)


# Foreign Keys (FK):
# - A Foreign Key creates a relationship between two tables. It references the
# Primary Key of another table.
# - Purpose: Link records from one table to another (one-to-many relationship)

class Author(models.Model):
    name = models.CharField(max_length=100)


class PostModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # author_id will store the id of the Author (FK)

# on_delete Options:

# CASCADE - Delete posts when author is deleted
# PROTECT - Prevent author deletion if posts exist
# SET_NULL - Set author to NULL (requires null=True)
# SET_DEFAULT - Set to default value


# Example:
class Author(models.Model):
    id = 1  # Primary Key
    name = "Alice"


class Post2(models.Model):
    id = 10  # Primary Key
    title = "Django Guide"
    author_id = 1  # Foreign Key (points to Author.id)

# One Author can have many Posts
# Many Posts point to one Author (one-to-many) or (many-to-one), from Parent's
# perspective, or from Child's perspective respectively.
# One-to-Many:	1 Author → Many Posts	Author's side
# Many-to-One:	Many Posts → 1 Author	Post's side
