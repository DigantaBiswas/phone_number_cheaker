import os, shutil,glob,sys

def organization(given_path):
    
    os.chdir(given_path)
    audio_folder=given_path+'\Audio'
    video_folder=given_path+'\Videos'
    EXE_folder=given_path+'\EXE'
    pictures_folder=given_path+'\Pictures'
    documents_folder=given_path+'\Documents'
    source_files=os.listdir(given_path)

    
    if os.path.exists(given_path+'Audio'):
        print('Audio file is there')
    else:
        print('Creating folder')
        try:
            os.makedirs('Audio')
        except IOError:
            print ('already exists')

    if os.path.exists(given_path+'Documents'):
        print('Documents file is there')
    else:
        print('Creating folder')
        try:
            os.makedirs('documents')
        except IOError:
            print ('already exists')
            
    if os.path.exists(given_path+'Videos'):
        print('Videos file is there')
    else:
        print('Creating folder')
        try:
            os.makedirs('Videos')
        except IOError:
            print ('already exists')
        
    if os.path.exists(given_path+'EXE'):
        print('EXE file is there')
    else:
        print('Creating folder')
        try:
            os.makedirs('EXE')
        except IOError:
            print ('already exists')

    if os.path.exists(given_path+'Pictures'):
        print('EXE file is there')
    else:
        print('Creating folder')
        try:
            os.makedirs('Pictures')
        except IOError:
            print ('already exists')
        
        
    for file in source_files:
        if file.endswith('.mp3'):
            shutil.move(os.path.join(given_path,file),os.path.join(audio_folder,file))
        elif file.endswith('.mp4' or '.avi' or '.wmv' or '.flv'):
            shutil.move(os.path.join(given_path,file),os.path.join(video_folder,file))
        elif file.endswith('.exe' or '.zip' or '.rar' or '.jar'):
            shutil.move(os.path.join(given_path,file),os.path.join(EXE_folder,file))
        elif file.endswith('.jpg' or '.png'):
            shutil.move(os.path.join(given_path,file),os.path.join(pictures_folder,file))
        elif file.endswith('.txt' or '.pdf' or '.ppt' or '.docx'):
            shutil.move(os.path.join(given_path,file),os.path.join(documents_folder,file))
        else:
            print('No matchable iteams found')
            
def take_path():
    print('Enter the  folder path you wanna organize')
    entered_path=input()
    organization(entered_path)

take_path()
