Django REST API CRUD Demo

A beginner-friendly REST API project built using Django and Django REST Framework (DRF). This project demonstrates fundamental REST API concepts through a simple blog post CRUD application.

Features

Create blog posts.

Retrieve a list of posts.

Retrieve individual posts.

Update existing posts using PUT.

Partially update posts using PATCH.

Delete existing posts.

Serializer-based data validation.

Technologies Used

Python

Django

Django REST Framework

HTTPie (API testing)

SQLite

API Endpoints

HTTP Method

Endpoint

Description

GET

/blogpost/

Retrieve all posts

POST

/blogpost/

Create a new post

GET

/blogpost/<id>/

Retrieve a specific post

PUT

/blogpost/<id>/

Fully update a post

PATCH

/blogpost/<id>/

Partially update a post

DELETE

/blogpost/<id>/

Delete a post
