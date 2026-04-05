import os

labels_path = r"C:\Users\parth\Desktop\Docs\GRAD DOCS\Spring 25\MMAE 500 Data Driven Modelling\Project\AMR_Collision_Project\datasets\labels\train"

classes_found = set()

for label_file in os.listdir(labels_path):
    if label_file.endswith('.txt'):
        with open(os.path.join(labels_path, label_file), 'r') as f:
            lines = f.readlines()
            for line in lines:
                class_id = int(line.split()[0])
                classes_found.add(class_id)

print("Classes found:", sorted(classes_found))
