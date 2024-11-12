import os
import random

# Directories where the images and labels are stored (absolute paths for your system)
images_dir = r'C:\Users\User\Downloads\images (3)'
labels_dir = r'C:\Users\User\Downloads\labels (2)'

# Get the list of all images
image_files = sorted(os.listdir(images_dir))
label_files = sorted(os.listdir(labels_dir))

# Ensure that the number of images and labels match
assert len(image_files) == len(label_files)

# Pair the images with their corresponding labels (use just the filenames)
paired_files = list(zip(image_files, label_files))

# Shuffle the dataset to randomize the file order
random.shuffle(paired_files)

# Split the dataset into 80% training and 20% validation
split_idx = int(len(paired_files) * 0.8)
train_files = paired_files[:split_idx]
val_files = paired_files[split_idx:]

# Create train.txt and val.txt with relative paths
with open('train.txt', 'w') as train_file, open('val.txt', 'w') as val_file:
    for img_file, lbl_file in train_files:
        train_file.write(f"./images/{img_file}\n")  # Writing relative path for images
    for img_file, lbl_file in val_files:
        val_file.write(f"./images/{img_file}\n")  # Writing relative path for images
