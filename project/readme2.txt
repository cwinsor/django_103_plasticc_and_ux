
Procedure:

This is the steps to deploy the application.  It is adapted from "Django Fundamentals" By Reindert-Jan Ekker (https://app.pluralsight.com/library/courses/django-fundamentals-update/table-of-contents)

It assumes you already identified target customer, designed and verified wireframes, and have a database schema and site layout.  Database schema is at bottom of this file.

+==========================

0) Create a virtual environment using pip and requirements.txt.

1) Use Django to auto-generate a Project
	django-admin startproject starchaser
	cd starchaser
	python manage.py runserver

2) Within Django, create a project and project-app
	python manage.py startapp app_gameplay
	edit settings.py to add app_gameplay to the INSTALLED_APPS list

3) Create Model classes and run migration
	class PlasticcObject(models.Model):  <from schema spec...>
	python manage.py makemigrations
	python manage.py migrate
----> test for migration

4) Register Models with the Admin interface
	in admin.py - add:

		from .models import PlasticcObject, PlasticcSample, GameplayMove
		admin.site.register(PlasticcObject)
		admin.site.register(PlasticcSample)
		admin.site.register(GameplayMove)

4) Create superuser account
	python manage.py createsuperuser
	visit /admin to confirm, add some elements of data using "admin"
---> test there should be an admin account, and should be able to add elements

5) Add _str_ method to the Models
best practice:

fmt = '{}'
# fmt_f = '{:5.2f}'
fmt_f = '{:.2f}'
fmt_obj = '{:8}'
fmt_is = '{:1}'
fmt_i3 = '{:3}'

    def __str__(self):
        msg = '{}'
        msg += ' object_id ' + fmt_obj
        msg += ' mjd ' + fmt
        msg += ' passband ' + fmt_is
        msg += ' flux ' + fmt_f
        msg += ' f_err ' + fmt_f
        msg += ' detected ' + fmt

        return msg.format(
            self.id,
            self.object.object_id,
            self.mjd,
            self.passband,
            self.flux,
            self.flux_err,
            self.detected)



6) Exercise the model API using python:
	python manage.py shell   <------- note not directly running python
	>>> from app_gameplay.models import PlasticcObject, PlasticcSample
	>>> PlasticcObject.objects.all()
	>>> x = PlasticcObject.objects.get(pk=1)
	>>> x
		<PlasticcObject: PlasticcObject object (1)>
	>>> ob.id
		1
	>>> ob.save()


7) create a new "app" called "app_player"
	python manage.py startapp app_player
	make a folder "templates"
	and within that an app folder "app_player"

	create a home.html
	create a views.py

8) extend the user model to add a "total score" attribute
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone

9) add temporary code in the view to extract data for the home page
list of games this user (player's status)
list of users (leaderboard)

    rounds_this_player = GameplayRound.objects.filter(player=request.user)
    rounds_this_player_list = list(rounds_this_player)

    leader_board = User.objects.all()
    leader_board_list = list(leader_board)

    return render(request, "app_player/home.html",
                  {'rounds': rounds_this_player_list,
                   'leader_board': leader_board_list}
                  )

10) move the model-specific logic into the model
https://app.pluralsight.com/course-player?clipId=2a19bcef-0aae-45f7-9cfb-bb6ed672c3c4
to do this:
  a) create a custom queryset class (derive from QuerySet class")
     this will represent a collection of objects from the database
     can call "filter" and "exclude" on it
     e.g. an object that represents all game objects...
  b) within that QuerySet create a method "all_games" or whatever
  c) within the **Games** class, assign "object = GamesQuerySet.as_manager()"
     that over-rides the default "objects" (examples of use earlier).  Whoh!

11a) static content:  establish folder for CSS, javascript, images.
Use django markup in .html to refer to these

11b) use template inheritance to "extend" and re-use html
decouple static templates from our app - putting everything at a top-level in the Project.
this is identified in settings.py "TEMPLATES" -> DIRS
STATICFILES_DIRS - list of static files
as identified at https://app.pluralsight.com/course-player?clipId=d87db3e0-e7b0-479d-ad70-41e2bd2a78da

12 name your URLs in url.py

13 add @login_required before the methods in views.py
is_authenticated = if statement in a view or template
login_required - decorate entire view function
redirect to named URL
---> test - all pages should require login

14 create a login page, use build-in view classes and login template, and configuration
https://app.pluralsight.com/course-player?clipId=f05d370f-6e7f-4a8f-9840-a1066943a313
redirect login to our home page - this is done in settings.py LOGIN_REDIRECT_URL

same for logout

15 Create our own Form using ModelForm
Procedure is add a ModelForm class, add a View function, render with a Template.
https://app.pluralsight.com/course-player?clipId=5ba2f661-dcc1-40ad-b5e7-93c1a13498ba
To do this:
create a form based on a model... (derive from ModelForm).  This is done in forms.py
create a view function that renders the template.  This does a return render (.html) is in views.py
create the template (.html) that render the form... i.e.   {{ form }} and submit button.  This is in blah.html
add the url map to the view function in urls.py
to get to the page - add a link to your homepage

16 add form submit handling and CSRF protection
Procedure is to discern GET vs POST, validate user input, show validation errors, redirect on success.
https://app.pluralsight.com/course-player?clipId=98f0ce7f-bb5e-4970-bd7c-6509c3211205

always perform server-side validation of user input - this is becuase client-side form validation can easily be edited
also - always add the <CSRF> (Cross Site Request Forgery).  When Django displays a form the Django server creates a special token, and the browser needs to send the token back when we submit the form.

----> test for CSRF.  This needs to be done on every post URL.

----> test for server-side validation of POST.  What that means is that a rogue user cannot 

----> test - the user authentication should take advantage of some base infrastructure

----> test - server-side input validation (individual fields) - for each field the server disallows invalid values.  THIS SHOULD BE PART OF INFRASTRUCTURE AROUND MODEL.  MANUAL CHECK IS REQUIRED FOR ANY FIELDS THAT ARE FREEFORM OR NOT CONSTRAINED IN MODEL DEFINITION.
----> test - server-side input validation (relationships) - for each combination of fields the server enforces relationships.  This is entirely hand-coded.
 
17 Create our own Form without ModelForm.  View that takes an argument.
https://app.pluralsight.com/course-player?clipId=9504e04d-c886-4555-9ca8-2fc646a4f432


17 Hooking the TensorFlow model into Django web app:
Four aproaches:

Offline:  run the classifier on the entire dataset in advance and store classification results in the database.  This avoids delays in displaying the pages so a good approach if the model is slow.  It does require data be available in advance.  

Realtime classification: run the classifier on demand (when serving the page).  This will work if the model is fast (sub-second) as it will preclude page load.

Classify in pre-fetch:  run the classifier when serving pages, but start that classification early (when item has been selected but before results are needed).  The goal is the classification results would be available by the time they are needed.

Relatime classification with dynamic loadeing of page:  run the classifier on demand, but display the page first without the classification, then update the page when the classification becomes available.


18)
Logging
https://docs.djangoproject.com/en/3.0/topics/logging/
in settings.py
#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
        #'level': 'WARNING',
    },
}

in code
    import logging
    logger = logging.getLogger(__name__)
    logger.debug("here")


19) "Tensorflow Serving"
https://www.youtube.com/watch?v=T_afaArR0E8


xxxxxxxxxxxxxxxxxxxxxxxxxx
<br>
{% for x in evals_btrotta.columns %}
{% for y in evals_btrotta.index %}
x={{ x }}
{% endfor %}

test123= {{ evals_btrotta.loc['0','star00'] }}

https://django-pandas.readthedocs.io/en/latest/#


+===============
Database schema for Star Chaser App

download PLAsTiCC dataset from Kaggle
Save into dedicated folder and unzip.

We will use Django Models to specify our database schema, and create "migration" scripts to implement the tables and relations.  We will start by using the out-of-the-box database to get the application running.  Once working we will move to Postgres and the larger dataset.  This should just involve pointing Django to Postgres, re-running the migrate script, and using pg-admin to import the data.

SCHEMA (PLAsTiCC):

Metadata: PlasticcObject
object_id (int32) = primary key
ra    (float32) = right ascension
decl  (float32) = declination
gal_l (float32) = galactic longitude
gal_b (float32) = galactic latitude
ddf   (boolean) = indicator of Deep Drilling Field (will have low measure of flux error).
hostgal_specz (float32) = spectroscopic redshift of host galaxy = accurate measure of redshift
hostgal_photoz (float32) = photometric redshift of host galaxy = proxy for specz and less accurate
hostgal_photoz_err (float32) = uncertainty in hostgal_photoz 
distmod (float32) = distance calculated from hostgal_photoz
MWEBV (float32) = measure of extinction of light for object in Milky Way galaxy 
target (int8) = class of object

Timeseries: PlasticcSample
object_id (foreign key to PlasticcObject)
mjd (float64) = Modified Julian Date
passband (int8) = one of [0,1,2,3,4,5]
flux (float32) = measure of intensity at the passband
flux_err (floaat32) = uncertainty on the measurement of flux
detected (boolean) = indicator the brightness is significant relative to threshold

SCHEMA (Gameplay)

GameplayMove:
object_id (foreign key to PlasticcObject)
star_name (string)
bet_1 = small int
...


