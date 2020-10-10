
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




To create tables we use orm

ORM(object relational mapping)
---------------------------
using shell -- :
  create
  update
  read
  delete

  insert:
    python manage.py shell
======================================
python create manage.py create superuser

To create super user
we must





python manage.py makemigrations

python manage.py migrate

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py createsuperuser
Username (leave blank to use 'matsasiva'):
Email address: sivaaim12345@gmail.com
Password:
Password (again):
The password is too similar to the username.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.


Microsoft Windows [Version 10.0.18363.1082]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py makemigrations
No changes detected

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py createsuperuser
Username (leave blank to use 'matsasiva'):
Email address: sivaaim12345@gmail.com
Password:
Password (again):
The password is too similar to the username.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 16:15:28
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[10/Oct/2020 16:15:53] "GET /admin/ HTTP/1.1" 302 0
[10/Oct/2020 16:15:54] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2194
[10/Oct/2020 16:15:54] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/login.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[10/Oct/2020 16:15:55] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 16:15:55] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
Not Found: /favicon.ico
[10/Oct/2020 16:15:55] "GET /favicon.ico HTTP/1.1" 404 2417
[10/Oct/2020 16:16:09] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[10/Oct/2020 16:16:09] "GET /admin/ HTTP/1.1" 200 3310
[10/Oct/2020 16:16:09] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 16:16:09] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[10/Oct/2020 16:16:09] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[10/Oct/2020 16:16:09] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[10/Oct/2020 16:17:00] "GET /admin/auth/user/ HTTP/1.1" 200 7846
[10/Oct/2020 16:17:00] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:17:00] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6263
[10/Oct/2020 16:17:00] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[10/Oct/2020 16:17:01] "GET /static/admin/js/actions.js HTTP/1.1" 200 6783
[10/Oct/2020 16:17:01] "GET /static/admin/js/core.js HTTP/1.1" 200 5418
[10/Oct/2020 16:17:01] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 6078
[10/Oct/2020 16:17:01] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[10/Oct/2020 16:17:01] "GET /static/admin/js/urlify.js HTTP/1.1" 200 8632
[10/Oct/2020 16:17:01] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[10/Oct/2020 16:17:01] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
[10/Oct/2020 16:17:01] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[10/Oct/2020 16:17:01] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[10/Oct/2020 16:17:01] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[10/Oct/2020 16:17:01] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 200 1097
[10/Oct/2020 16:17:35] "GET /admin/auth/user/add/ HTTP/1.1" 200 6859
[10/Oct/2020 16:17:35] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
[10/Oct/2020 16:17:35] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:17:35] "GET /static/admin/css/forms.css HTTP/1.1" 200 8423
[10/Oct/2020 16:17:35] "GET /static/admin/css/widgets.css HTTP/1.1" 200 10592
[10/Oct/2020 16:17:35] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[10/Oct/2020 16:17:52] "POST /admin/auth/user/add/ HTTP/1.1" 200 7113
[10/Oct/2020 16:17:52] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:18:28] "POST /admin/auth/user/add/ HTTP/1.1" 200 7033
[10/Oct/2020 16:18:28] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:18:48] "POST /admin/auth/user/add/ HTTP/1.1" 200 7097
[10/Oct/2020 16:18:48] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:19:11] "POST /admin/auth/user/add/ HTTP/1.1" 302 0
[10/Oct/2020 16:19:11] "GET /admin/auth/user/2/change/ HTTP/1.1" 200 15160
[10/Oct/2020 16:19:11] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:19:11] "GET /static/admin/js/calendar.js HTTP/1.1" 200 7788
[10/Oct/2020 16:19:11] "GET /static/admin/js/SelectBox.js HTTP/1.1" 200 4257
[10/Oct/2020 16:19:11] "GET /static/admin/js/SelectFilter2.js HTTP/1.1" 200 12350
[10/Oct/2020 16:19:11] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19750
[10/Oct/2020 16:19:12] "GET /static/admin/img/selector-icons.svg HTTP/1.1" 200 3291
[10/Oct/2020 16:19:12] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
[10/Oct/2020 16:19:12] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
[10/Oct/2020 16:22:33] "POST /admin/auth/user/2/change/ HTTP/1.1" 200 15414
[10/Oct/2020 16:22:33] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:23:12] "POST /admin/auth/user/2/change/ HTTP/1.1" 302 0
[10/Oct/2020 16:23:12] "GET /admin/auth/user/ HTTP/1.1" 200 8464
[10/Oct/2020 16:23:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Covid19\models.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 16:35:27
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py makemigrations
Migrations for 'Covid19':
  Covid19\migrations\0001_initial.py
    - Create model Patients

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py migrate
Operations to perform:
  Apply all migrations: Covid19, admin, auth, contenttypes, sessions
Running migrations:
  Applying Covid19.0001_initial... OK

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>





Microsoft Windows [Version 10.0.18363.1082]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py makemigrations
No changes detected

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py createsuperuser
Username (leave blank to use 'matsasiva'):
Email address: sivaaim12345@gmail.com
Password:
Password (again):
The password is too similar to the username.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 16:15:28
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[10/Oct/2020 16:15:53] "GET /admin/ HTTP/1.1" 302 0
[10/Oct/2020 16:15:54] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2194
[10/Oct/2020 16:15:54] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/login.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[10/Oct/2020 16:15:54] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[10/Oct/2020 16:15:55] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 16:15:55] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
Not Found: /favicon.ico
[10/Oct/2020 16:15:55] "GET /favicon.ico HTTP/1.1" 404 2417
[10/Oct/2020 16:16:09] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[10/Oct/2020 16:16:09] "GET /admin/ HTTP/1.1" 200 3310
[10/Oct/2020 16:16:09] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 16:16:09] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[10/Oct/2020 16:16:09] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[10/Oct/2020 16:16:09] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[10/Oct/2020 16:17:00] "GET /admin/auth/user/ HTTP/1.1" 200 7846
[10/Oct/2020 16:17:00] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:17:00] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6263
[10/Oct/2020 16:17:00] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[10/Oct/2020 16:17:01] "GET /static/admin/js/actions.js HTTP/1.1" 200 6783
[10/Oct/2020 16:17:01] "GET /static/admin/js/core.js HTTP/1.1" 200 5418
[10/Oct/2020 16:17:01] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 6078
[10/Oct/2020 16:17:01] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[10/Oct/2020 16:17:01] "GET /static/admin/js/urlify.js HTTP/1.1" 200 8632
[10/Oct/2020 16:17:01] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[10/Oct/2020 16:17:01] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
[10/Oct/2020 16:17:01] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[10/Oct/2020 16:17:01] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[10/Oct/2020 16:17:01] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[10/Oct/2020 16:17:01] "GET /static/admin/img/sorting-icons.svg HTTP/1.1" 200 1097
[10/Oct/2020 16:17:35] "GET /admin/auth/user/add/ HTTP/1.1" 200 6859
[10/Oct/2020 16:17:35] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
[10/Oct/2020 16:17:35] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:17:35] "GET /static/admin/css/forms.css HTTP/1.1" 200 8423
[10/Oct/2020 16:17:35] "GET /static/admin/css/widgets.css HTTP/1.1" 200 10592
[10/Oct/2020 16:17:35] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[10/Oct/2020 16:17:52] "POST /admin/auth/user/add/ HTTP/1.1" 200 7113
[10/Oct/2020 16:17:52] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:18:28] "POST /admin/auth/user/add/ HTTP/1.1" 200 7033
[10/Oct/2020 16:18:28] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:18:48] "POST /admin/auth/user/add/ HTTP/1.1" 200 7097
[10/Oct/2020 16:18:48] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:19:11] "POST /admin/auth/user/add/ HTTP/1.1" 302 0
[10/Oct/2020 16:19:11] "GET /admin/auth/user/2/change/ HTTP/1.1" 200 15160
[10/Oct/2020 16:19:11] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:19:11] "GET /static/admin/js/calendar.js HTTP/1.1" 200 7788
[10/Oct/2020 16:19:11] "GET /static/admin/js/SelectBox.js HTTP/1.1" 200 4257
[10/Oct/2020 16:19:11] "GET /static/admin/js/SelectFilter2.js HTTP/1.1" 200 12350
[10/Oct/2020 16:19:11] "GET /static/admin/js/admin/DateTimeShortcuts.js HTTP/1.1" 200 19750
[10/Oct/2020 16:19:12] "GET /static/admin/img/selector-icons.svg HTTP/1.1" 200 3291
[10/Oct/2020 16:19:12] "GET /static/admin/img/icon-clock.svg HTTP/1.1" 200 677
[10/Oct/2020 16:19:12] "GET /static/admin/img/icon-calendar.svg HTTP/1.1" 200 1086
[10/Oct/2020 16:22:33] "POST /admin/auth/user/2/change/ HTTP/1.1" 200 15414
[10/Oct/2020 16:22:33] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 16:23:12] "POST /admin/auth/user/2/change/ HTTP/1.1" 302 0
[10/Oct/2020 16:23:12] "GET /admin/auth/user/ HTTP/1.1" 200 8464
[10/Oct/2020 16:23:12] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Covid19\models.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 16:35:27
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py makemigrations
Migrations for 'Covid19':
  Covid19\migrations\0001_initial.py
    - Create model Patients

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py migrate
Operations to perform:
  Apply all migrations: Covid19, admin, auth, contenttypes, sessions
Running migrations:
  Applying Covid19.0001_initial... OK

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py shell
Python 3.6.8 (tags/v3.6.8:3c6b436a57, Dec 24 2018, 00:16:47) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from Covid19.models import Patients
>>> data = Patients(P_name="sivaji",P_age=20,P_email="cseceo@gmail.com"
...
KeyboardInterrupt
>>> data = Patients(P_name="sivaji",P_age=20,P_email="cseceo@gmail.com")
>>> data.save()
>>> data = Patients.objects.create(P_name = "prasanna" , P_age=32,P_email="nomail@gmail.com")
>>> data= Patients.objects.all()
>>> data
<QuerySet [<Patients: sivaji>, <Patients: Ravi>, <Patients: sajjan>, <Patients: prasanna>]>
>>> data= Patients.objects.values("P_age")
>>> data
<QuerySet [{'P_age': 20}, {'P_age': 37}, {'P_age': 21}, {'P_age': 32}]>
>>> data= Patients.objects.values("P_email")
>>> data
<QuerySet [{'P_email': 'cseceo@gmail.com'}, {'P_email': 'ravi@gmail.com'}, {'P_email': 'email.email@gmail.com'}, {'P_email': 'nomail@gmail.com'}]>
>>> data= Patients.objects.list("P_email")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'list'
>>> data= Patients.objects.values_list("P_email")
>>> data
<QuerySet [('cseceo@gmail.com',), ('ravi@gmail.com',), ('email.email@gmail.com',), ('nomail@gmail.com',)]>
>>> data= Patients.objects.values_list("P_name")
>>> data
<QuerySet [('sivaji',), ('Ravi',), ('sajjan',), ('prasanna',)]>
>>> data = Patients.objects.get(P_age=20)
>>> data
<Patients: sivaji>
>>> data = Patients.objects.filter(P_age=20)
>>> data
<QuerySet [<Patients: sivaji>]>
>>> data = Patients.objects.filter(P_age=20)
>>> data
<QuerySet [<Patients: sivaji>, <Patients: sad>]>
>>> data=Patients.objects.values('P_age')
>>> data
<QuerySet [{'P_age': 20}, {'P_age': 37}, {'P_age': 21}, {'P_age': 32}, {'P_age': 20}]>
>>> data=Patients.objects.values('P_age').get(P_name="siva")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\db\models\query.py", line 431, in get
    self.model._meta.object_name
Covid19.models.Patients.DoesNotExist: Patients matching query does not exist.
>>> data=Patients.objects.values('P_age').get(P_name="sivaji")
>>> data
{'P_age': 20}
>>> data=Patients.objects.first()
>>> data
<Patients: sivaji>
>>> data=Patients.objects.last()
>>> data
<Patients: sad>
>>> data=Patients.objects.second()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'Manager' object has no attribute 'second'
>>> data= Patients.objects.order_by("P_name")
>>> data
<QuerySet [<Patients: Ravi>, <Patients: prasanna>, <Patients: sad>, <Patients: sajjan>, <Patients: sivaji>]>
>>> data= Patients.objects.order_by("P_age")
>>> data
<QuerySet [<Patients: sivaji>, <Patients: sad>, <Patients: sajjan>, <Patients: prasanna>, <Patients: Ravi>]>
>>> data = Patients.objects.all()[0]
>>> data
<Patients: sivaji>
>>> data = Patients.objects.all()[5]
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\db\models\query.py", line 325, in __getitem__
    return qs._result_cache[0]
IndexError: list index out of range
>>> data = Patients.objects.all()[3]
>>> data
<Patients: prasanna>
>>> data = Patients.objects.all().update(P_age=20)
>>> data
5
>>> data = Patients.objects.all()
>>> data
<QuerySet [<Patients: sivaji>, <Patients: Ravi>, <Patients: sajjan>, <Patients: prasanna>, <Patients: sad>]>
>>> data= Patients.objects.order_by("P_age")
>>> data
<QuerySet [<Patients: sivaji>, <Patients: Ravi>, <Patients: sajjan>, <Patients: prasanna>, <Patients: sad>]>
>>> data= Patients.objects.order_by("P_age")
>>> data=Patients.objects.values('P_age').get(P_name="sivaji")
>>> data
{'P_age': 20}
>>> data=Patients.objects.values('P_age').get(P_name="sad")
>>> data
{'P_age': 20}
>>> data=Patients.objects.values('P_age').get(P_name="prasanna")
>>> data
{'P_age': 20}
>>> data = Patients.objects.create(P_name="prasanna",p_age=20,P_email="pra@dm.com"
...
KeyboardInterrupt
>>> data = Patients.objects.filter(P_age=20)
>>> data
<QuerySet [<Patients: sivaji>, <Patients: Ravi>, <Patients: sajjan>, <Patients: prasanna>, <Patients: sad>]>
>>> data.P_age=20
>>> data=Patients.objects.values('P_age')
>>> data
<QuerySet [{'P_age': 20}, {'P_age': 20}, {'P_age': 20}, {'P_age': 20}, {'P_age': 20}]>
>>> data.P_age=24
>>> data
<QuerySet [{'P_age': 20}, {'P_age': 20}, {'P_age': 20}, {'P_age': 20}, {'P_age': 20}]>
>>> data=Patients.objects.values('P_age')
>>> data=Patients.objects.filter(P_age=20)
>>> data
<QuerySet [<Patients: sivaji>, <Patients: Ravi>, <Patients: sajjan>, <Patients: prasanna>, <Patients: sad>]>
>>> data.save()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'save'
>>> data.update(P_age=22)
5
>>> data.update(P_age=20)
0
>>> data = Patients.objects.filter(P_age=26).delete
>>> data
<bound method QuerySet.delete of <QuerySet [<Patients: sad>]>>
>>>


Microsoft Windows [Version 10.0.18363.1082]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 17:02:05
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
Not Found: /
[10/Oct/2020 17:02:20] "GET / HTTP/1.1" 404 2366
Not Found: /favicon.ico
[10/Oct/2020 17:02:20] "GET /favicon.ico HTTP/1.1" 404 2417
[10/Oct/2020 17:02:33] "GET /admin/ HTTP/1.1" 302 0
[10/Oct/2020 17:02:33] "GET /admin/login/?next=/admin/ HTTP/1.1" 200 2194
[10/Oct/2020 17:02:34] "GET /static/admin/css/base.css HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/css/nav_sidebar.css HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/css/login.css HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/css/responsive.css HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/js/nav_sidebar.js HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/css/fonts.css HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 17:02:34] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 17:02:49] "POST /admin/login/?next=/admin/ HTTP/1.1" 302 0
[10/Oct/2020 17:02:49] "GET /admin/ HTTP/1.1" 200 4567
[10/Oct/2020 17:02:49] "GET /static/admin/css/dashboard.css HTTP/1.1" 200 380
[10/Oct/2020 17:02:49] "GET /static/admin/img/icon-addlink.svg HTTP/1.1" 200 331
[10/Oct/2020 17:02:49] "GET /static/admin/img/icon-changelink.svg HTTP/1.1" 200 380
[10/Oct/2020 17:02:49] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 304 0
[10/Oct/2020 17:03:06] "GET /admin/auth/group/ HTTP/1.1" 200 5272
[10/Oct/2020 17:03:06] "GET /static/admin/css/changelists.css HTTP/1.1" 200 6263
[10/Oct/2020 17:03:06] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:03:06] "GET /static/admin/js/jquery.init.js HTTP/1.1" 200 347
[10/Oct/2020 17:03:06] "GET /static/admin/js/vendor/jquery/jquery.js HTTP/1.1" 200 287630
[10/Oct/2020 17:03:06] "GET /static/admin/js/core.js HTTP/1.1" 200 5418
[10/Oct/2020 17:03:06] "GET /static/admin/js/admin/RelatedObjectLookups.js HTTP/1.1" 200 6078
[10/Oct/2020 17:03:06] "GET /static/admin/js/actions.js HTTP/1.1" 200 6783
[10/Oct/2020 17:03:06] "GET /static/admin/js/urlify.js HTTP/1.1" 200 8632
[10/Oct/2020 17:03:07] "GET /static/admin/js/prepopulate.js HTTP/1.1" 200 1531
[10/Oct/2020 17:03:07] "GET /static/admin/js/vendor/xregexp/xregexp.js HTTP/1.1" 200 232381
[10/Oct/2020 17:03:07] "GET /static/admin/img/search.svg HTTP/1.1" 200 458
[10/Oct/2020 17:03:07] "GET /static/admin/img/tooltag-add.svg HTTP/1.1" 200 331
[10/Oct/2020 17:03:12] "GET /admin/ HTTP/1.1" 200 4567
[10/Oct/2020 17:03:16] "GET /admin/Covid19/patients/ HTTP/1.1" 200 6112
[10/Oct/2020 17:03:16] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:03:32] "GET /admin/Covid19/patients/add/ HTTP/1.1" 200 6595
[10/Oct/2020 17:03:32] "GET /static/admin/css/forms.css HTTP/1.1" 200 8423
[10/Oct/2020 17:03:32] "GET /static/admin/js/prepopulate_init.js HTTP/1.1" 200 492
[10/Oct/2020 17:03:32] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:03:32] "GET /static/admin/css/widgets.css HTTP/1.1" 200 10592
[10/Oct/2020 17:03:32] "GET /static/admin/js/change_form.js HTTP/1.1" 200 606
[10/Oct/2020 17:04:00] "POST /admin/Covid19/patients/add/ HTTP/1.1" 302 0
[10/Oct/2020 17:04:00] "GET /admin/Covid19/patients/ HTTP/1.1" 200 6521
[10/Oct/2020 17:04:00] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:04:00] "GET /static/admin/img/icon-yes.svg HTTP/1.1" 200 436
[10/Oct/2020 17:04:04] "GET /admin/Covid19/patients/add/ HTTP/1.1" 200 6595
[10/Oct/2020 17:04:04] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:04:39] "POST /admin/Covid19/patients/add/ HTTP/1.1" 302 0
[10/Oct/2020 17:04:39] "GET /admin/Covid19/patients/ HTTP/1.1" 200 6732
[10/Oct/2020 17:04:39] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:07:08] "GET /admin/Covid19/patients/ HTTP/1.1" 200 6740
[10/Oct/2020 17:07:09] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:16:13] "GET /admin/Covid19/patients/add/ HTTP/1.1" 200 6595
[10/Oct/2020 17:16:13] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:16:34] "POST /admin/Covid19/patients/add/ HTTP/1.1" 302 0
[10/Oct/2020 17:16:34] "GET /admin/Covid19/patients/ HTTP/1.1" 200 7146
[10/Oct/2020 17:16:34] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:40:06] "GET /admin/Covid19/ HTTP/1.1" 200 2752
[10/Oct/2020 17:40:11] "GET /admin/Covid19/patients/add/ HTTP/1.1" 200 6595
[10/Oct/2020 17:40:11] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:40:33] "POST /admin/Covid19/patients/add/ HTTP/1.1" 302 0
[10/Oct/2020 17:40:33] "GET /admin/Covid19/patients/ HTTP/1.1" 200 7356
[10/Oct/2020 17:40:33] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:40:55] "GET /admin/Covid19/ HTTP/1.1" 200 2752
[10/Oct/2020 17:40:58] "GET /admin/Covid19/patients/ HTTP/1.1" 200 7154
[10/Oct/2020 17:40:58] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
Not Found: /
[10/Oct/2020 17:41:05] "GET / HTTP/1.1" 404 2366
[10/Oct/2020 17:41:10] "GET /admin/Covid19/patients/ HTTP/1.1" 200 7154
[10/Oct/2020 17:41:33] "GET /admin/Covid19/patients/5/change/ HTTP/1.1" 200 6847
[10/Oct/2020 17:41:33] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
[10/Oct/2020 17:41:39] "POST /admin/Covid19/patients/5/change/ HTTP/1.1" 302 0
[10/Oct/2020 17:41:39] "GET /admin/Covid19/patients/ HTTP/1.1" 200 7356
[10/Oct/2020 17:41:39] "GET /admin/jsi18n/ HTTP/1.1" 200 3187
C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Covid19\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 17:58:32
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Covid19\views.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
October 10, 2020 - 18:00:59
Django version 3.1.2, using settings 'Corona.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Corona\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\threading.py", line 916, in _bootstrap_inner
    self.run()
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\autoreload.py", line 53, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\management\commands\runserver.py", line 118, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\management\base.py", line 396, in check
    databases=databases,
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\registry.py", line 70, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 408, in check
    for pattern in self.url_patterns:
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 589, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 582, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
  File "<frozen importlib._bootstrap_external>", line 781, in get_code
  File "<frozen importlib._bootstrap_external>", line 741, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Corona\urls.py", line 26
    path('welcome/',views.welcome,name="welcome"),
       ^
SyntaxError: invalid syntax

C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Corona\urls.py changed, reloading.
Watching for file changes with StatReloader
Performing system checks...

Exception in thread django-main-thread:
Traceback (most recent call last):
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\threading.py", line 916, in _bootstrap_inner
    self.run()
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\autoreload.py", line 53, in wrapper
    fn(*args, **kwargs)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\management\commands\runserver.py", line 118, in inner_run
    self.check(display_num_errors=True)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\management\base.py", line 396, in check
    databases=databases,
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\registry.py", line 70, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\urls.py", line 13, in check_url_config
    return check_resolver(resolver)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\core\checks\urls.py", line 23, in check_resolver
    return check_method()
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 408, in check
    for pattern in self.url_patterns:
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 589, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\utils\functional.py", line 48, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\site-packages\django\urls\resolvers.py", line 582, in urlconf_module
    return import_module(self.urlconf_name)
  File "C:\Users\Matsa Siva\AppData\Local\Programs\Python\Python36\lib\importlib\__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 994, in _gcd_import
  File "<frozen importlib._bootstrap>", line 971, in _find_and_load
  File "<frozen importlib._bootstrap>", line 955, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 665, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 674, in exec_module
  File "<frozen importlib._bootstrap_external>", line 781, in get_code
  File "<frozen importlib._bootstrap_external>", line 741, in source_to_code
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "C:\Users\Matsa Siva\Desktop\Django-Framwork\DjangoProjects\Corona\Corona\urls.py", line 26
    path('welcome/',views.welcome,name="welcome"),
       ^
SyntaxError: invalid syntax


                                   
