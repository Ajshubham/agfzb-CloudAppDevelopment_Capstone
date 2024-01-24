from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    # path('static-template/', static_template_view, name='static_template'),
    # path for about view
    path(route='about/', view=views.about, name='about'),
    # path for contact us view
    path(route='contact/', view=views.contact, name='contact'),
    # path for registration

    # path for login
    path(route='login/', view=views.login_request, name='login'),
    # path for logout
    path(route='logout/', view=views.logout_request, name='logout'),    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'djangoapp:about' %}">About Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:contact' %}">Contact Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:index' %}">Dealerships</a>
            </div>
        </div>
    </nav>
    <form action="{% url 'djangoapp:registration' %}" method="POST">
        <div class="container">
          <h1>Sign Up</h1>
          <hr>
          <label for="username"><b>User Name</b></label>
          <input type="text" placeholder="Enter User Name: " name="username" required>
          <label for="firstname"><b>First Name</b></label>
          <input type="text" placeholder="Enter First Name: " name="firstname" required>
          <label for="lastname"><b>Last Name</b></label>
          <input type="text" placeholder="Enter Last Name: " name="lastname" required>
          <label for="psw"><b>Password</b></label>
          <input type="password" placeholder="Enter Password: " name="psw" required>
          <div>
              {% csrf_token %}
              <button class="button" type="submit">Sign Up</button>
          </div>
        </div>
      </form>    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'djangoapp:about' %}">About Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:contact' %}">Contact Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:index' %}">Dealerships</a>
            </div>
        </div>
    </nav>
    <form action="{% url 'djangoapp:registration' %}" method="POST">
        <div class="container">
          <h1>Sign Up</h1>
          <hr>
          <label for="username"><b>User Name</b></label>
          <input type="text" placeholder="Enter User Name: " name="username" required>
          <label for="firstname"><b>First Name</b></label>
          <input type="text" placeholder="Enter First Name: " name="firstname" required>
          <label for="lastname"><b>Last Name</b></label>
          <input type="text" placeholder="Enter Last Name: " name="lastname" required>
          <label for="psw"><b>Password</b></label>
          <input type="password" placeholder="Enter Password: " name="psw" required>
          <div>
              {% csrf_token %}
              <button class="button" type="submit">Sign Up</button>
          </div>
        </div>
      </form>    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'djangoapp:about' %}">About Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:contact' %}">Contact Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:index' %}">Dealerships</a>
            </div>
        </div>
    </nav>
    <form action="{% url 'djangoapp:registration' %}" method="POST">
        <div class="container">
          <h1>Sign Up</h1>
          <hr>
          <label for="username"><b>User Name</b></label>
          <input type="text" placeholder="Enter User Name: " name="username" required>
          <label for="firstname"><b>First Name</b></label>
          <input type="text" placeholder="Enter First Name: " name="firstname" required>
          <label for="lastname"><b>Last Name</b></label>
          <input type="text" placeholder="Enter Last Name: " name="lastname" required>
          <label for="psw"><b>Password</b></label>
          <input type="password" placeholder="Enter Password: " name="psw" required>
          <div>
              {% csrf_token %}
              <button class="button" type="submit">Sign Up</button>
          </div>
        </div>
      </form>    <nav class="navbar navbar-light bg-light">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="{% url 'djangoapp:about' %}">About Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:contact' %}">Contact Us</a>
                  <a class="navbar-brand" href="{% url 'djangoapp:index' %}">Dealerships</a>
            </div>
        </div>
    </nav>
    <form action="{% url 'djangoapp:registration' %}" method="POST">
        <div class="container">
          <h1>Sign Up</h1>
          <hr>
          <label for="username"><b>User Name</b></label>
          <input type="text" placeholder="Enter User Name: " name="username" required>
          <label for="firstname"><b>First Name</b></label>
          <input type="text" placeholder="Enter First Name: " name="firstname" required>
          <label for="lastname"><b>Last Name</b></label>
          <input type="text" placeholder="Enter Last Name: " name="lastname" required>
          <label for="psw"><b>Password</b></label>
          <input type="password" placeholder="Enter Password: " name="psw" required>
          <div>
              {% csrf_token %}
              <button class="button" type="submit">Sign Up</button>
          </div>
        </div>
      </form>
      hj


      <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% load static %}
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
    <body>
    <!--Add a registration form here -->
    </body>
</html><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% load static %}
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
    <body>
    <!--Add a registration form here -->
    </body>
</html>ddddddd<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    {% load static %}
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
    <body>
    <!--Add a registration form here -->
    </body>
</html>
    # path for home
    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)