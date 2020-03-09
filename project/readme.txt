This git implements a web-application using Django backend with PostgreSQL.  It's designed as a game where the user is challenged to predict whether a star will explode (i.e. become a super-Nova) or remain stable.

The dataset originates from the Photometric LSST Astronomical Time Series Classification Challenge (PLAsTiCC) (1) which was prepared in anticipation of "first light" for the  Large Synoptic Survey Telescope (LSST) (2).  The LSST endeavors to study transient objects, stars that vary in brightness over time.  Examples of transients are super-novas, pulsars, binary stars, and lensing.

LSST will be evaluating the southern hemisphere, about 37 billion stars and galaxies.  It is expected about 10 million (one in a thousand) stars will be in transition.  To find these anomolies the telescope will capture 20 Terabytes of data each night. The goal is to process the data, and within 60 minutes of observation, notify other astronomers of newly detected events.  It is a staggering proposition!

From this we endeavour to make a game.

(1) https://arxiv.org/abs/1810.00001
(2) https://www.lsst.org/

+===================
First step is UX/UI design.  This is a very important topic area, and one where I have zero background.  Here are two courses that helped a lot to understnad what is involved, and understand tools/process.

What is involved:
pluralsight: Getting Started in UX Design By Kurt Krumme <----------- strongly recommend (41 minutes)
https://app.pluralsight.com/library/courses/getting-started-ux-design/table-of-contents

pluralsight: UX Design Creating Wireframes By Susan Simkins <----------- (1 hour 30 minutes)
https://app.pluralsight.com/library/courses/ux-design-creating-wireframes/table-of-contents


+=================================
<the following template came from Krumme
GOALS:
RESEARCH:
DESIGN:
TEST:

+====================
material/fodder...

In this competition you will be working to classify stars in the nighttime sky.  You'll be given a list of stars that have gone Supernova (have exploded) and will be asked to identify what kind of SuperNova it was.  You'll be assisted by K.Boone and B. Trotta - top researchers in Astronomy and Machine Learning.  Their recommendation engines use the latest A.I. from Google, Microsoft and the Open Source Community and will help you win.  Your challenge is to combine the raw data with the recommendations from the AI experts to determine what kind of SuperNova it was.  

You'll be competing against your peers who have access to the same data and tools.  It's a winner-take-all competition with leaderboard.

Good Luck !

+==============================
Metrics:
https://arxiv.org/abs/1809.11145

The organizers chose probabilistic classification as the metric.  This means the model must assign a likelihood score for each of the class values. This is different than the more typical MAP (maximum a-priori) classification where the model predicts most likely class value.  The reason is that lesser-probable classes might warrent investigation if that class is interesting.  As stated in the paper "an object with even a moderate probability of being of a very rare class could be worth the risk (of further investigation)".  In other words - probabilistic classification provides richer data to help guide further study of individual objects.

To make this tractable for the average user - we pose this as a "betting game" where they have $100 and must place your bets on the N classes of star.  They are free to go "all in" on one class, or spready the money around.  When the user pushes "score" the "winning" class is revealed, and the user receives points based on how much they placed in that category.

.... <too much don't include>
The user is provided with predictions from two top Machine Learning algorithms for this competition - 


+========================================
INFO - Astronomy of Transients
Details on the dataset, with introduction to the field of time-series (transient) astronomy is provided in data_note.pdf that comes with the Kaggle dataset https://www.kaggle.com/c/PLAsTiCC-2018/data.
In summary:
The data is time-series measurements of intensity (flux) from stars.  Flux is measured at 6 frequency bands.  At most once meaurement per band is taken every two weeks however measurements are aperiodic due to schedule and weather, and there may even be monthlong gaps if the object is not visible due seasonal position of objet in the sky. 
Difference imaging is used - the intensity measured on a particular night is compared to a prior measurement and the difference is reported.  Thus a star that is unchanging would record a flux of zero, and a star changing in flux would record a positive or negative value.  The manner in which the flux changes (it's frequency composition, rate of change, and duration of change) are indicators as to the type of event that is occurring.  There are 15 classes of objects in the dataset, 14 of which are reflected in the training data.

Behavior can be roughly categorized as aperiodic (one-time), periodic (repeating at a specific period), and episotic (repeating at a non-periodic interval). Examples are (respectively) supernova, pulsar, and <???>.

Red-shift is a property whereby more distant objects are observed to have a shifted, and broadened, frequency spectrum.

Stars in the our our Milky-way galaxy can be individually observed.  Stars in other galaxies are not measured individually, rather are measured using the above difference technique, where the contribution of the galaxy is considered 'background' and contribution from the transient is represented as the difference.

3) The Data

Metadata Table:
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

Time-series Table:
object_id (int32 and foreign key to Metadata table)
mjd (float64) = Modified Julian Date
passband (int8) = one of [0,1,2,3,4,5]
flux (float32) = measure of intensity at the passband
flux_err (floaat32) = uncertainty on the measurement of flux
detected (boolean) = indicator the brightness is significant relative to threshold

Note:
Milky-way objects are identified  


CREATING DATA FOR THE GAME:
For the game we only need a small subset of the data, but we want to understand what we're including.
Questions:
How many object in the training set?
How many data points in the training set?
How many objects in training set are galactic (Milky-Way)?  [redshift=0]
How many objects in training set are galactic AND are DDF ?
THEN -
With that galactic+DDF subset - what is the distribution (count) of classes ?








+========================================
Dataset
timeseries table =  measurments of "flux" (intensity) for one of 6 frequency bands.  Samples are taken aperiodically.  There is a foreign key to Object Identifier.
Object identifier table = object ID and 


and astronomy.    At any time there are billions of stars, and many of them are competing against an Artifical Intelligence Machine  Machine Learning Models using the latest algorithms (Kiras/Tensorflow/LGBoosting) developed by the top Kagglers (B.Trotta,  leaderboard  (ref.  models availa  The game pits you against two models from the Kaggle competition.  The models, develpoed using the latest machine learning techniques and top leaderboard champions, predict what class to which the star belongs.  Your challenge is to meet or beat the models !

UI/UX Design:
https://uxdesignmastery.com/5-free-ux-design-tools-in-2018-that-are-actually-free/

https://careerfoundry.com/en/blog/ui-design/essential-tools-for-ui-designers-a-beginners-guide/
pencilproject - mozilla
mockflow - web-based <-----------
wireframe.cc
fluidui
mockups <----------

https://medium.theuxblog.com/11-best-prototyping-tools-for-ui-ux-designers-how-to-choose-the-right-one-c5dc69720c47
invision

https://app.pluralsight.com/library/courses/getting-started-ux-design/table-of-contents  <--------



Key references:
https://www.nature.com/articles/nature11643


Smartt, S. Cosmic explosions in the young Universe. Nature 491, 205-206 (2012). https://doi.org/10.1038/nature11643


