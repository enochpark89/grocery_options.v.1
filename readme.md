# Grocery_options.v.1

- Leveraging Django, I will create an app that stores grocery data from different supermarket companies. In the front-end, user can use CRUD functions to create, read, update, and delete data stored in mySQL DB. 

# Development progress

## Initiate Virtual Environment
In bash:
cd grocery_options
source scripts/activate
cd grocery_options_v1

20220719 by Enoch Park.
1. Create a Github repo.
2. Link it to the file location of the project. (instructions are in github)
3. Install Python
4. Install pip (usually comes in package with python)
5. Create a Virtual Environment(VE) with venv.
```bash
py -m venv grocery_options
```
6. Once grocery_options folder is created, run Scripts\activate.bat to initiate VE.
- Change the current directory to grocery_options, run the scripts.
```bash
cd grocery_options
source Scripts/activate
```
- When you see (<project name>), you are in the VE. 

7. Install Django inside VE.
```bash
py -m pip install Django
```
- Confirm installation by checking the version.
```bash
django-admin --version
```

8. Using Django-admin, start a project.
```bash
# I know it is repetitive but I used the same name. (doesn't take period(.))
django-admin startproject grocery_options_v1
```
start project file trees:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
Explanation to each file:
https://docs.djangoproject.com/en/4.0/intro/tutorial01/

9. Run the local server to test its functionality. (Make sure your cd is in the project folder you just created)
```bash
cd grocery_options_v1
py manage.py runserver
```
- You should see the default page with the header "The install worked successfully! Congratulations!"

10. Create App. 
- In a nutshell, each web page works like an app.
- We are going to create an app called "groceryitems"
```bash
py manage.py startapp groceryitems
```
- As a result, a sub folder called "groceryitems" is created.

*Tree-like file structure would be good. I might need linux bash"

11. Create views

    Steps:
    1. views.py can return http response such as HTML documents.
    ```py
    from django.shortcuts import render
    from django.http import HttpResponse

    def index(request):
        return HttpResponse("Hello world!")
    ```

    2. urls.py is where url is routed to views.py
    *urls.py needs to be created within the same folder as view.py*

    urls.py:
    ```py
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```

    3. Root URL needs to be configured to route users to the subpage or the rootpage. 
    - I decided to route users to the root page since I am not putting anything there yet.
    <root>/urls.py
    ```py
    from django.contrib import admin
    from django.urls import include, path

    urlpatterns = [
        path('', include('groceryitems.urls')),
        path('admin/', admin.site.urls),
    ]

    ```

    Flow of executions:
    clients request -> Root -> groceryitems.urls -> views.index -> HTTPresponse "hello world" is generated and sent back.

12. Return HTTP template instead of string.

    - Since the routing is complete, you just need to change views.py to get template.

    Steps:
    1. Create HTML template
    - path: <app name>/templates/index.html:
    (it has to be in templates folder because it is just where Django framework is designed to look for templates.)
    ```html
    <!DOCTYPE html>
    <html>
    <body>

    <h1>Grocery options v.1</h1>
    <p>Welcome to grocery options where you can compare grocery prices from multiple supermarket companies.</p>

    </body>
    </html>
    ```
    2. Update view.py to render HTML template instead of a string

    views.py:
    ```py
    from django.http import HttpResponse
    from django.template import loader

    def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
    ```
    3. Change settings.py to apply changes in the app. 

    add new apps under settings.py
    <project name>/settings.py
    ```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'groceryitems.apps.GroceryitemsConfig'
    ]
    ```

    4. Migrate changes made in the settings.
    ```bash
    py manage.py migrate
    ```

    5. Check whether the template will show when the server is requested.'

- Learned how to import static.css and external css from outside source like mvp.css

13. Create a Model.

    - You can use sqlLite if you are doing this for the first time. Django app comes with internal sqlLite.
    - If you want to try connecting to your mySQL DB, please follow below

        *How do you connect to mySQL DB?*
        Reference:
        https://www.javatpoint.com/how-to-connect-mysql-to-django

        Steps:
        1. Prerequisite: 
        - MySQL server 5.7 is installed
        - Python 3.0+ is installed.

        If you already installed mySQL, check the installation by getting the version.
        (skipped)

    Use SQLite DB

    *How do you create a Table(Model)?*

    Steps:
    1. Create a model
    <app name>/models.py
    ```py
    class Groceryitems(models.Model):
    post_date = models.DateField()
    company_name = models.CharField(max_length=30)
    price = models.IntegerField()
    condition = models.CharField(max_length=30)
    brand_name = models.CharField(max_length=30)
    item_name = models.CharField(max_length=50)
    ```

    2. MakeMigration
    - Once change is made on the model, you have to makemigrations
    ```
    py manage.py makemigrations groceryitems
    ```
    (Django creates a file with any new changese and stores the file in the /migrations/ folder)

    3. Migration
    - py manage.py migrate will create and execute SQL statement, based on the content of the new file in the migration folder. 
    ```py
    py manage.py migrate

    ```

14. Add Record using Shell

Open Powershell Shell
```py
py manage.py shell

```
Run below
```py
# Get models from groceryitems
from groceryitems.models import Groceryitems
# Now you can call objects inside the groceryitems model.
Groceryitems.objects.all()
# It returns a QuerySet
```
*What is a queryset?*
- A QuerySet is a collection of data from a database.

*How do you add data?*
You can create a data
```
item = Groceryitems(post_date="2022-07-20", company_name="Ralphs", price="3", condition="2 for three", brand_name="none", item_name="Jumbo Avocado")
item.save()
```

- Check whether the data is inputted correctly or not.
```py
# Output values of the objects.
Groceryitems.objects.all().values()
```
15. User template displaying the data. 

	Steps:

	a. Create a template that takes the data and display to FE.
	members/templates/index.html:
	```html
	<!DOCTYPE html>
	<html>
	<head>
		<link rel="stylesheet" href="https://unpkg.com/mvp.css">
		{% load static %}
		<link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
	</head>
	<body>
		<h1>Grocery Items</h1>

		<table border="1">
		<tr>
			<th>ID</th>
			<th>Post Date</th>
			<th>Company Name</th>
			<th>Price</th>
			<th>Description</th>
			<th>Brand Name</th>
			<th>Item Name</th>
		</tr>
		{% for item in items %}
		<tr>
		<td>{{ item.id }}</td>
		<td>{{ item.post_date }}</td>
		<td>{{ item.company_name }}</td>
		<td>$ {{ item.price }}</td>
		<td>{{ item.condition }}</td>
		<td>{{ item.brand_name }}</td>
		<td>{{ item.item_name }}</td>
		</tr>
		{% endfor %}
		</table>

	</body>
	</html>
	```

	- This template will iterate the items QuerySet you receive and present data.

	b. Modify the View
	```py
	from django.db import models

	"""
	Columns
	- Date of offer: postdate
	- Supermarket company name: company_name
	- Price: price
	- Condition: deal
	- Brand: brand_name
	- Item name: item_name

	"""

	class Groceryitems(models.Model):
	  post_date = models.DateField()
	  company_name = models.CharField(max_length=30)
	  price = models.IntegerField()
	  condition = models.CharField(max_length=30)
	  brand_name = models.CharField(max_length=30)
	  item_name = models.CharField(max_length=50)

	```

	- Then, users can view data with the column header.

16. Create Add Record button and POST handler

	Steps:

	a. Create an Add button in the index.html template.
	```html
		<div>
			<a href="add/"><button type="button">Add</button></a>
		</div>
	```

	b. Create an Add template.
	```html

	  post_date = models.DateField()
	  company_name = models.CharField(max_length=30)
	  price = models.IntegerField()
	  condition = models.CharField(max_length=30)
	  brand_name = models.CharField(max_length=30)
	  item_name = models.CharField(max_length=50)

	<h1>Add item</h1>

	<form action="addrecord/" method="post">
		{% csrf_token %}
		Post Date:<br>
		<input name="post_date">
		<br><br>
		
		Company name:<br>
		<input name="company_name">
		<br><br>
		
		Price:<br>
		<input name="price">
		<br><br>
		
		Description:<br>
		<input name="condition">
		<br><br>
		
		Brand Name:<br>
		<input name="brand_name">
		<br><br>	
		
		Item Name:<br>
		<input name="item_name">
		<br><br>	

		<input type="submit" value="Submit">
	</form>
	```
	c. Modify View to render add.html template when button is clicked.

	- Create a method called add that renders add template.
	view.py
	```py
	def add(request):
	  template = loader.get_template('add.html')
	  return HttpResponse(template.render({}, request))
	```

	d. Change url.py to route users to views.add method when clicked.

	```py
	from django.urls import path
	from . import views

	urlpatterns = [
	  path('', views.index, name='index'),
	  path('add/', views.add, name='add'),
	]
	```

	e. Add more url that handles POST request

	urls.py
	```py
	from django.urls import path
	from . import views

	urlpatterns = [
	  path('', views.index, name='index'),
	  path('add/', views.add, name='add'),
	  path('add/addrecord/', views.addrecord, name='addrecord'),
	]
	```

	f. Modify views to add addrecord that handles the POST request.

	views.py
	```py
	def addrecord(request):
	  x = request.POST['first']
	  y = request.POST['last']
	  member = Members(firstname=x, lastname=y)
	  member.save()
	  return HttpResponseRedirect(reverse('index'))
	```

17. Create delete buttons on each row of data.

a. You can add delete button next to each row so that users can delete at will when they want to delete. 

<app>/urls.py:
```html
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://unpkg.com/mvp.css">
    {% load static %}
    <link rel="stylesheet" type="text/css" href="{% static 'styles.css' %}">
</head>
<body>
    <h1>Grocery Items</h1>
    <div>
        <a href="add/"><button type="button">Add</button></a>
    </div>
    <table border="1">
    <tr>
        <th>ID</th>
        <th>Post Date</th>
        <th>Company Name</th>
        <th>Price</th>
        <th>Description</th>
        <th>Brand Name</th>
        <th>Item Name</th>
        <th>Remove Button</th>
    </tr>
    {% for item in items %}
    <tr>
    <td>{{ item.id }}</td>
    <td>{{ item.post_date }}</td>
    <td>{{ item.company_name }}</td>
    <td>$ {{ item.price }}</td>
    <td>{{ item.condition }}</td>
    <td>{{ item.brand_name }}</td>
    <td>{{ item.item_name }}</td>
    <td><a href="delete/{{ x.id }}">delete</a></td>

    </tr>
    {% endfor %}
    </table>

</body>
</html>
```

b. Create a method to delete record.

<app>/views.py:
```py
......
def delete(request, id):
  member = Members.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
```

c. create url that handles delete item.

<app>/urls.py
```py

from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  # delete request with id as a parameter gets sent to views.delete method.
  path('delete/<int:id>', views.delete, name='delete'),
]
```

18. Create an update function

- To update a record, we need the ID of the record.
- We need a template with an interface that let us change the value. 

a. Update the template to route the user to update the item.

members/templates/index.html:
```html
<td>
	<a href="update/{{ item.id }}">
		<button class="updateButton">Update</button>
	</a>
</td>
```

b. Update view.py by creating a update method that handles updating of an item. 

<app>.views.py
```py
......

def update(request, id):
  item = Groceryitems.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'item': item,
  }
  return HttpResponse(template.render(context, request))
```
*What does the above code do?*
1. Gets the id as an argument.
2. Uses the id to locate the correct record in the groceryitems table.
3. loads a template called update.html.
4. Creates an object containing the item.
5. Sends the object to the template.
6. Outputs the HTML that is rendered by the template.

c. Create a new template called update.html
<app>/templates/update.html
```html
<h1>Update member</h1>

<form action="updaterecord/{{ mymember.id }}" method="post">
{% csrf_token %}
First Name:<br>
<input name="first" value="{{ mymember.firstname }}">
<br><br>
Last Name:<br>
<input name="last" value="{{ mymember.lastname }}">
<br><br>
<input type="submit" value="Submit">
</form>
```

d. update urls.py to receive a POST request with the ID

- Make app accept the url with "/update/:id"
<app>.url.py
```py
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
]
```

- Create another url that handles POST request.
```py
from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('add/', views.add, name='add'),
  path('add/addrecord/', views.addrecord, name='addrecord'),
  path('delete/<int:id>', views.delete, name='delete'),
  path('update/<int:id>', views.update, name='update'),
  path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
]
```
- Will handle POST request sent to "update/updaterecord/:id with views.updaterecord method.

e. Create a updaterecord handler.
views.py
```py
  
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Members.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('index'))
```

19. 