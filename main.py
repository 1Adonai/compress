from PIL import Image
import os
import test as progress_bar
import time
import sys


path = os.getcwd()
path_orig = path + "/img"
file_list = os.listdir(path=path_orig)
target_size_kb = 400
i = 0
def compress_image(file_list, path_orig, target_size_kb):
    i = 0
    for image_file in file_list:
        input_path = os.path.join(path_orig,image_file)
        image = Image.open(input_path)
        quality = 85
        i += 1
        sys.stdout.write("\rProcessing image {}/{}".format(i, len(file_list)))
        sys.stdout.flush()
        while os.path.getsize(input_path) > target_size_kb * 1024:
            image.save(input_path, 'JPEG', quality=quality, optimize=True, progressive=True)
            quality -= 5
            
            
        image.close()

        
    
compress_image(file_list, path_orig, target_size_kb)
