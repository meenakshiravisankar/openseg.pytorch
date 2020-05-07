import os
from shutil import copy

dataset_path = "/home/ubuntu/meenakshir/semantic-segmentation/datasets/idd"
train_path = "train_1.lst"
val_path = "val_1.lst"

train_dir = "/home/ubuntu/meenakshir/semantic-segmentation/datasets/idd/cityscapes/train"
val_dir = "/home/ubuntu/meenakshir/semantic-segmentation/datasets/idd/cityscapes/val"

train_file = open(train_path)
train_img_dir = os.path.join(train_dir, "image")
train_lbl_dir = os.path.join(train_dir, "label")
if not os.path.exists(train_img_dir):
    os.makedirs(train_img_dir)
if not os.path.exists(train_lbl_dir):
    os.makedirs(train_lbl_dir)

for path in train_file:
    paths = path.strip('\n').split(' ')
    img_path, lbl_path = paths[0], paths[-1]
    # save image
    base_dir, img_name = os.path.split(img_path)
    base_dir = os.path.split(base_dir)[1]
    img_name = str(base_dir)+img_name

    img_path = os.path.join(dataset_path, img_path)
    dst_path = os.path.join(train_img_dir, img_name)
    copy(img_path, dst_path)
    # save label
    base_dir, lbl_name = os.path.split(lbl_path)
    base_dir = os.path.split(base_dir)[1]
    lbl_name = str(base_dir)+lbl_name.replace("level3",'')
    
    lbl_path = os.path.join(dataset_path, lbl_path)
    dst_path = os.path.join(train_lbl_dir, lbl_name)
    copy(lbl_path, dst_path)

val_file = open(val_path)
val_img_dir = os.path.join(val_dir, "image")
val_lbl_dir = os.path.join(val_dir, "label")
if not os.path.exists(val_img_dir):
    os.makedirs(val_img_dir)
if not os.path.exists(val_lbl_dir):
    os.makedirs(val_lbl_dir)

for path in val_file:
    paths = path.strip('\n').split(' ')
    img_path, lbl_path = paths[0], paths[-1]
    # save image
    base_dir, img_name = os.path.split(img_path)
    base_dir = os.path.split(base_dir)[1]
    img_name = str(base_dir)+img_name
    
    img_path = os.path.join(dataset_path, img_path)
    dst_path = os.path.join(val_img_dir, img_name)
    copy(img_path, dst_path)
    # save label
    base_dir, lbl_name = os.path.split(lbl_path)
    base_dir = os.path.split(base_dir)[1]
    lbl_name = str(base_dir)+lbl_name.replace("level3",'')
    
    lbl_path = os.path.join(dataset_path, lbl_path)
    dst_path = os.path.join(val_lbl_dir, lbl_name)
    copy(lbl_path, dst_path)

