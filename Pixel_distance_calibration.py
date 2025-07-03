import cv2

# ——— USER SETUP ———
SIDE_IMAGE = "data/Experiment_6/exp6_cam1/exp6_cam1_cropped_14d/cam1_05-07_15-00.jpg"   # your side-view photo 
REAL_HEIGHT_MM = 95.0               # your best guess of the vertical span in millimeters


points = []
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point {len(points)}: (x={x}, y={y})")
        if len(points) == 2:
            cv2.line(display_img, points[0], points[1], (0,255,0), 2)
            cv2.imshow(window_name, display_img)

# Load the image
img = cv2.imread(SIDE_IMAGE)
if img is None:
    raise RuntimeError(f"Could not open {SIDE_IMAGE}")

# Create a resizable window
window_name = "click two points"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

# Resize window to 50% of image dimensions
h, w = img.shape[:2]
cv2.resizeWindow(window_name, w//4, h//4)

# Make a copy for drawing the line
display_img = img.copy()

print("Click the TOP point of your known segment, then the BOTTOM point.")
cv2.setMouseCallback(window_name, on_click)
cv2.imshow(window_name, display_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(points) != 2:
    raise RuntimeError("You must click exactly two points.")

# Compute pixel distance and scale
(y1, y2) = points[0][1], points[1][1]
delta_px = abs(y2 - y1)
px_per_mm = delta_px / REAL_HEIGHT_MM

print(f"\nPixel distance = {delta_px:.1f} px")
print(f"Real height    = {REAL_HEIGHT_MM:.1f} mm")
print(f"→ SIDE_SCALE_PX_PER_MM = {px_per_mm:.3f} px/mm")

