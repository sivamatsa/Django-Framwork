
installation --

pip install django

if not:  change path for pip

import django

dir(django)
['VERSION', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'get_version', 'setup', 'utils']

django.get_version()
'3.1.2'


django-admin--version

for project

django-admin startproject project name

  editors :

  sublime
  visual studio
  pycharm
  atom  ..etc



init.py : packages
settings.py : all apps info , database
url.py : all urls browsers related
wsgi: web server gateway interface
manage.py: uses:--
            interface between dproj and command prompt
            we can run our server
            exicute db connections
            able open shell
            create app also
            
python manage.py runserver
http://127.0.0.1:8000/ -- localhost:8000

to change port number ---=> python manage.py runserver 8888



App Creation :

    python manage.py startapp appname
                OR
    django-admin startapp appname

Migration:
    tables in the form of classes
    its a interface bn classes and tables

    Migrate: its a conversion

init:

admin: classes name admin register

app: contains all app realted info
models:contains all classes - db tables
tests: testing purpose
views: contains all logics --its heart for db


HTTP requests and HTTP responces
================================
get - post

get : url
post : request from html

responce ; based on user request it will provide  responce

url ;
    static url:
    Dynamic url:

===========================================
        task:
            home/satheesh/22/M

            hi this is satheesh and my age is 33 and my gender is M
            ===================================
