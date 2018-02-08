import shutil,os,re

#create a regex that matches files with american date format

date_pattern=re.compile(r"""^.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)
