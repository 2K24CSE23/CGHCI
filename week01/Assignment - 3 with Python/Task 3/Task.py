from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 1. Load image into NumPy array
img = Image.open("sample.jpg")
img_array = np.array(img)

# 2. Extract 2D intensity grids (Axis 2 slicing)
r_2d = img_array[:, :, 0]
g_2d = img_array[:, :, 1]
b_2d = img_array[:, :, 2]

# 3. Construct 3D color arrays with zeroed-out inactive channels
red_only = np.zeros_like(img_array)
red_only[:, :, 0] = r_2d

green_only = np.zeros_like(img_array)
green_only[:, :, 1] = g_2d

blue_only = np.zeros_like(img_array)
blue_only[:, :, 2] = b_2d

# Print metrics matching sample output format
print("--- CHANNEL EXTRACTION SUMMARY ---")
print(f"Original Image Shape :  {img_array.shape}")
print(f"Red Channel 2D Shape :  {r_2d.shape} | Mean Intensity:  {r_2d.mean():.2f}")
print(f"Green Channel 2D Shape:  {g_2d.shape} | Mean Intensity:  {g_2d.mean():.2f}")
print(f"Blue Channel 2D Shape :  {b_2d.shape} | Mean Intensity:  {b_2d.mean():.2f}")
print("Display Window :  Matplotlib 2x3 Subplot Grid Rendered.")

# 4. Display 2x3 subplot layout using matplotlib
plt.figure(figsize=(12, 6))

# Top Row: 3D Color Images
plt.subplot(2, 3, 1)
plt.imshow(red_only)
plt.title("Red-Only")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(green_only)
plt.title("Green-Only")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blue_only)
plt.title("Blue-Only")
plt.axis("off")

# Bottom Row: 2D Grayscale Maps
plt.subplot(2, 3, 4)
plt.imshow(r_2d, cmap="gray")
plt.title("Red Grayscale")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(g_2d, cmap="gray")
plt.title("Green Grayscale")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(b_2d, cmap="gray")
plt.title("Blue Grayscale")
plt.axis("off")

plt.tight_layout()
plt.show()