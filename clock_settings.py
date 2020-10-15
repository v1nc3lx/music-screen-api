### Clock settings

## General settings

msa_address = "localhost"
msa_port = "8080"

# Location of log file to write in addition to printing to screen. Comment out to disable
log_file = "~/msa-clock.log"

# One of ERROR, WARNING, INFO, DEBUG (in order of least to most verbose)
log_level = "INFO"

text_color = '#bef'
font_attr = 'font: 28pt'

# Clock timeout : how many secs you want the clock "on" after stopping playing your speaker and before turning it off. set 'clock_timeout' to -1 if you want endless timeout
clock_timeout = -1

# clock backgroud
background = "black.png"

# show date
display_date = True

#  '' for default Pi Setting
# Locales must be installed in your Pi.. to check what is installed
# locale -a
# to install locales
# sudo dpkg-reconfigure locales
date_locale = 'it_IT.UTF-8'
