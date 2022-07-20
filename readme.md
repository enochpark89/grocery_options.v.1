# Grocery_options.v.1

- Leveraging Django, I will create an app that stores grocery data from different supermarket companies. In the front-end, user can use CRUD functions to create, read, update, and delete data stored in mySQL DB. 

# Development progress

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


