
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

4) Register Models with the Admin interface
	in admin.py - add:

		from .models import PlasticcObject, PlasticcSample, GameplayMove
		admin.site.register(PlasticcObject)
		admin.site.register(PlasticcSample)
		admin.site.register(GameplayMove)

4) Create superuser account
	python manage.py createsuperuser
	visit /admin to confirm, add some elements of data using "admin"

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

10) move the model-specific logic into the model - as advised at https://app.pluralsight.com/course-player?clipId=2a19bcef-0aae-45f7-9cfb-bb6ed672c3c4
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

14 create a login page, use build-in view classes and login template, and configuration
https://app.pluralsight.com/course-player?clipId=f05d370f-6e7f-4a8f-9840-a1066943a313
redirect login to our home page - this is done in settings.py LOGIN_REDIRECT_URL

same for logout

15 Forms  (add a ModelForm class, add a View function, render with a Template)
https://app.pluralsight.com/course-player?clipId=5ba2f661-dcc1-40ad-b5e7-93c1a13498ba
create a form based on a model... (derive from ModelForm)






is_authenticated
login_required
redirection and name URLs



 


+===============
Database schema

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


