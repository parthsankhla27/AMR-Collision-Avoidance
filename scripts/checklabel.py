import os

base = r"C:\Users\parth\Desktop\Docs\GRAD DOCS\Spring 25\MMAE 500 Data Driven Modelling\Project\AMR_Collision_Project\datasets"

# This script iterates through the dataset directory structure to read
# the class IDs from YOLO format label files (.txt).
# It's useful for verifying label consistency or understanding the initial
# class IDs present in datasets before combining or relabeling.

for object_class in os.listdir(base):
    for split in ['train', 'valid', 'test']:
        labels_dir = os.path.join(base, object_class, split, 'labels')
        if os.path.exists(labels_dir):
            for label_file in os.listdir(labels_dir):
                if label_file.endswith('.txt'):
                    file_path = os.path.join(labels_dir, label_file)
                    with open(file_path, 'r') as f:
                        lines = f.readlines()
                        for line in lines:
                            class_id = line.split()[0]
                            print(f"{object_class} ({split}): Class ID = {class_id}")
