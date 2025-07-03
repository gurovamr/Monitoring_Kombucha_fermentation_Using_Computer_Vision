import os
import random
import cv2

# === CONFIGURATION ===
folder_path = 'data/Experiment_6/exp6_cam0'  

# ROI coordinates you want to visualize (from previous step)
roi_x, roi_y = 700, 450
roi_w, roi_h =  3000, 1500  

# Scale percent
scale_percent = 10  # 10% of original size

def get_random_image(folder):
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp'))]
    if not images:
        raise ValueError("No images found in the folder.")
    return os.path.join(folder, random.choice(images))

def resize_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    return cv2.resize(image, (width, height))

def show_scaled_image_with_scaled_roi(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return

    # Scale image
    scaled_image = resize_image(image, scale_percent)

    # Scale down ROI
    sf = scale_percent / 100.0
    x1 = int(roi_x * sf)
    y1 = int(roi_y * sf)
    x2 = int((roi_x + roi_w) * sf)
    y2 = int((roi_y + roi_h) * sf)

    image_with_rect = scaled_image.copy()
    cv2.rectangle(image_with_rect, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow("Scaled ROI Preview", image_with_rect)
    print(f"Showing image (scaled): {image_path}")
    print(f"Rectangle (scaled) drawn at (x={x1}, y={y1}, w={x2 - x1}, h={y2 - y1})")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    random_image_path = get_random_image(folder_path)
    show_scaled_image_with_scaled_roi(random_image_path)