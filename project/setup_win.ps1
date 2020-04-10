################################################
# activate the virtual environment
# if the pymote_env does not exist - create it

if (-NOT (Test-Path '.\pymote_env\Scripts\activate' -PathType Leaf)) {

    " "
    "did not find pymote_env\Scripts\activate - creating virtualenv now..."

    # confirm at least we have python with pip
    python --version
    python -m pip --version

    # add virtualenv to global libraries
    python -m pip install virtualenv

    # create an empty virtualenv
    python -m virtualenv pymote_env --no-site-packages
    }

# activate the virtualenv
.\pymote_env\Scripts\activate

# get the libraries specified in requirements.txt
pip install -r requirements.txt



################################################
# add current directory to PATH (so libraries can be found)

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot
$Env:PYTHONPATH=$ENV:PYTHONPATH + ';'

$Env:PYTHONPATH=$ENV:PYTHONPATH + $PSScriptRoot
$Env:PYTHONPATH=$ENV:PYTHONPATH + '/lib;'


#################################################
# to start vs-code
" "
"to start visual studio code:"
"cd starchaser; code -n ."

#################################################
# to run the web application
" "
"to run the application:"
"cd starchaser; python manage.py runserver 8001"
"URLs are:"
"  http://127.0.0.1:8001 (user login)"
"  http://127.0.0.1:8001/admin/ (admin login)"
"  accounts are:"
"    alice   abc (no admin)"
"    cwinsor abc (admin)"
" "
