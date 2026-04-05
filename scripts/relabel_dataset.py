import os

#core relabelling script
# This script reassigns class IDs in YOLO format label files based on
# a provided mapping from object names to desired integer class IDs.

def reassign_labels(folder_path, new_class_id):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith('.txt'):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                new_lines = []
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) >= 5:
                        parts[0] = str(new_class_id)
                        new_lines.append(' '.join(parts))
                with open(file_path, 'w') as f:
                    f.write('\n'.join(new_lines))

# Main execution loop
if __name__ == "__main__":
    base = r"C:/Users/parth/Desktop/Docs/GRAD DOCS/Spring 25/MMAE 500 Data Driven Modelling/Project/AMR_Collision_Project/datasets"
    # Mapping for object class names
    object_classes = {
        "cardboard_box": 0,
        "pallet": 1,
        "shelf": 2,
        "safety_cone": 3,
        "forklift": 4,
    }

# Loop through each object folder and relabel
    for object_name, class_id in object_classes.items():
        for split in ['train', 'valid', 'test']:
            labels_path = os.path.join(base, object_name, split, 'labels')
            if os.path.exists(labels_path):
                print(f"Relabeling {labels_path} to class {class_id}")
                reassign_labels(labels_path, class_id)
            else:
                print(f"Warning: Path not found {labels_path}, skipping.")

    print("Relabeling complete for all VALID splits!")
