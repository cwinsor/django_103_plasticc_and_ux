# these are instructions to start the web app, pipe logs to file and background/disown the process so it continues running after exit
# also see setup_linux.sh
#
# 
# foo=$(date +%y%m%d_%H%M%S)
# python starchaser/manage.py runserver 0.0.0.0:8000  2>&1 | tee -a logfile_$foo
# <ctrl-Z> to suspend it
# jobs
# bg 1
# disown

