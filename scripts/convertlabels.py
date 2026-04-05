import os

# Converts different bounding box formats (rotated 4-point, standard 4-value)
# into a consistent standard YOLO format (center_x, center_y, width, height).
def convert_rotated_to_yolo(parts):
    """Convert 4‑point rotated bbox to YOLOv8 center/width/height."""
    cls = parts[0]
    coords = list(map(float, parts[1:]))
    xs = coords[0::2]
    ys = coords[1::2]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    x_center = (xmin + xmax) / 2
    y_center = (ymin + ymax) / 2
    width    = xmax - xmin
    height   = ymax - ymin
    return f"{cls} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}"

def convert_bbox_line(parts):
    """Re‑format an existing 4‑value YOLO bbox line (center/size)."""
    cls = parts[0]
    x_center, y_center, w, h = map(float, parts[1:])
    return f"{cls} {x_center:.6f} {y_center:.6f} {w:.6f} {h:.6f}"

def process_label_file(path):
    lines = [l.strip() for l in open(path) if l.strip()]
    out = []
    for line in lines:
        parts = line.split()
        n = len(parts) - 1
        if n == 8:
            out.append(convert_rotated_to_yolo(parts))
        elif n == 4:
            out.append(convert_bbox_line(parts))
        else:
            print(f"Skipping unexpected format in {path}: {line}")
    if out:
        open(path, 'w').write('\n'.join(out))

def process_folder(label_dir):
    for root, _, files in os.walk(label_dir):
        for f in files:
            if f.endswith('.txt'):
                process_label_file(os.path.join(root, f))

if __name__ == "__main__":
    
    base = r"C:/Users/parth/Desktop/Docs/GRAD DOCS/Spring 25/MMAE 500 Data Driven Modelling/Project/AMR_Collision_Project/datasets"
    
    objects = ["cardboard_box", "pallet", "shelf", "safety_cone", "forklift"]
    splits  = ["train", "valid", "test"] 

    for obj in objects:
        for split in splits:
            lbl_dir = os.path.join(base, obj, split, "labels")
            if os.path.isdir(lbl_dir):
                print(f"Processing {obj}/{split}/labels …")
                process_folder(lbl_dir)

    print("All label files converted to YOLOv8 bbox format.")
