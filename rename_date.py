import shutil,os,re

#create a regex that matches files with american date format

date_pattern=re.compile(r"""^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""", re.VERBOSE)

#TODO: Loop over the files in warking directory
for amer_file_name in os.listdir('.'):
    mo =date_pattern.search(amer_file_name)
    #skip files without a date
    
#TODO:Skip files without date
    if mo==None:
        continue
#TODO:Get the different parts of the file name
    before_part=mo.group(1)
    month_part=mo.group(2)
    day_part=mo.group(4)
    year_part=mo.group(5)
    after_part=mo.group(8)
#TODO:From  the European styel filename

    euro_file_name=before_part+day_part+'-'+month_part+'-'+year_part+after_part
    
#TODO: Get the full absolute file
    abs_working_dir=os.path.abspath('.')
    amer_file_name=os.path.join(abs_working_dir,amer_file_name)
    euro_file_name=os.path.join(abs_working_dir, euro_file_name)
#TODO: Rename files
    print('Renaming "%s" to "%s"...'%(amer_file_name,euro_file_name))
    shutil.move(amer_file_name,euro_file_name)
