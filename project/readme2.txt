
Procedure:
This is adapted from "Django Fundamentals" By Reindert-Jan Ekker (https://app.pluralsight.com/library/courses/django-fundamentals-update/table-of-contents)


0) Create a virtual environment using pip and requirements.txt.

1) Use Django to auto-generate a Project
	django-admin startproject starchaser
	cd starchaser
	python manage.py runserver

2) Within Django, create an App
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


2) Move/clean up so files/format are in the correct places.

3) Create Model classes (schema) and populate a few entries by hand.



https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone


xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


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
bet_13


To