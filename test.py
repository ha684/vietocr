import os
import random
import glob

import os
import random
import glob
import shutil

def create_annotation_files(data_root, train_annotation, valid_annotation, split_ratio=0.8):
    image_files = glob.glob(os.path.join(data_root, '*.jpg'))
    random.shuffle(image_files)
    
    split_index = int(len(image_files) * split_ratio)
    train_files = image_files[:split_index]
    valid_files = image_files[split_index:]
    
    def write_annotation_file(image_files, annotation_file):
        with open(annotation_file, 'w', encoding='utf-8') as f:
            for img_file in image_files:
                txt_file = img_file.replace('.jpg', '.txt')
                if os.path.exists(txt_file):
                    with open(txt_file, 'r', encoding='utf-8') as txt_f:
                        text = txt_f.read().strip()
                    
                    # Get folder name and image name
                    img_name = os.path.basename(img_file)
                    folder_name = os.path.basename(os.path.dirname(img_file))
                    
                    # New image name with folder name as prefix
                    new_img_name = f"{folder_name}-{img_name}"
                    new_img_path = os.path.join(data_root, new_img_name)
                    
                    # Rename the image file
                    os.rename(img_file, new_img_path)
                    
                    # Write to the annotation file
                    f.write(f'{new_img_path}\t{text}\n')
                    
                    # Delete the individual text file after using it
                    os.remove(txt_file)
    
    write_annotation_file(train_files, train_annotation)
    write_annotation_file(valid_files, valid_annotation)

# Paths to the data directories and annotation files
data_root = r'D:\Data\image_vi_00\vi_00'
train_annotation = r'D:\Data\image_vi_00\train_annotation.txt'
valid_annotation =r'D:\Data\image_vi_00\valid_annotation.txt'

# Create the annotation files
create_annotation_files(data_root, train_annotation, valid_annotation, split_ratio=0.8)

