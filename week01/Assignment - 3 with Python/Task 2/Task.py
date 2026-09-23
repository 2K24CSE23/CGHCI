import numpy as np

# 1. Create a 300x400x3 matrix filled with zeros
image = np.zeros((300, 400, 3), dtype=np.uint8)

# 2. Fill the four quadrants using basic slicing
# Top-Left: Pure Red
image[0:150, 0:200] = [255, 0, 0]

# Top-Right: Pure Green
image[0:150, 200:400] = [0, 255, 0]

# Bottom-Left: Pure Blue
image[150:300, 0:200] = [0, 0, 255]

# Bottom-Right: White
image[150:300, 200:400] = [255, 255, 255]

# 3. Print matrix properties
kb_size = image.nbytes / 1024

print("--- SYNTHETIC MATRIX METRICS ---")
print(f"Array Shape (H, W, C) : {image.shape}")
print(f"Data Type : {image.dtype}")
print(f"Total Elements : {image.size:,} values")
print(f"Memory Footprint : {image.nbytes:,} bytes ({kb_size:.2f} KB)")