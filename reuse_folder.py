import time
import os

def imageFolder(reuse_last_folder):
    start_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    image_folder = '/home/pi/lapse_project/lapse_{:s}'.format(start_time)
    
    if reuse_last_folder:
        print("Attempting to reuse previous image save directory")
        lapse_folders = []
        for f in os.listdir('/home/pi/lapse_project/'):
            if os.path.isdir(f) and 'lapse' in f:
                lapse_folders.append(f)
        lapse_folders.sort()
        if len(lapse_folders) > 0:
            image_folder = '/home/pi/lapse_project/' + lapse_folders[-1]
        else:
            print("Previous image save directory not found, using timestamp")
    else:
        print("Not attempting to reuse previous image save directory")
    print("Image save directory being used is:")
    print(image_folder)
    return(image_folder)
