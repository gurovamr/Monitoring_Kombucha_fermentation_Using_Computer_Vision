import os
import cv2

# === CONFIGURATION ===
folder_path = 'data/Experiment_6/exp6_cam0'  # Source folder
output_folder = os.path.join(folder_path, 'exp6_cam0_cropped_small')  # Output folder

# ROI coordinates
roi_x, roi_y = 700, 450
roi_w, roi_h =  3000, 1500 

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process all valid image files
for filename in os.listdir(folder_path):
    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        continue

    input_path = os.path.join(folder_path, filename)
    image = cv2.imread(input_path)

    if image is None:
        print(f"Skipping unreadable image: {filename}")
        continue

    h, w = image.shape[:2]

    # Ensure ROI is within image bounds
    x1 = min(roi_x, w - 1)
    y1 = min(roi_y, h - 1)
    x2 = min(x1 + roi_w, w)
    y2 = min(y1 + roi_h, h)

    cropped = image[y1:y2, x1:x2]
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, cropped)

    print(f"Cropped and saved: {output_path}")
