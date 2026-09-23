from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load input image into NumPy array
img = np.array(Image.open("sample.jpg"))
N = 8

# 1. Downsample using striding (every N-th pixel)
downsampled = img[::N, ::N, :]

# 2. Re-expand back to original dimensions using np.repeat
pixelated = np.repeat(np.repeat(downsampled, N, axis=0), N, axis=1)

# 3. Calculate percentage reductions
dim_reduction = (1 - (1 / N)) * 100
mem_savings = (1 - (downsampled.nbytes / img.nbytes)) * 100

# Print results
print(f"--- DOWNSAMPLING ANALYSIS (N = {N}) ---")
print(f"Original Shape :   {img.shape} | Memory:   {img.nbytes:,} bytes")
print(
    f"Downsampled Shape :   {downsampled.shape} | Memory:   {downsampled.nbytes:,} bytes"
)
print(
    f"Re-expanded Shape :   {pixelated.shape} | Visual:   Blocky Pixelation"
)
print(f"Dimension Reduction:   {dim_reduction:.2f}% reduction per axis")
print(f"Memory Savings :   {mem_savings:.2f}% data reduction")

# 4. Display Matplotlib figure output
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title(f"Original ({img.shape[1]}x{img.shape[0]})")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(downsampled)
plt.title(f"Downsampled ({downsampled.shape[1]}x{downsampled.shape[0]})")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(pixelated)
plt.title(f"Re-expanded Pixelated ({pixelated.shape[1]}x{pixelated.shape[0]})")
plt.axis("off")

plt.tight_layout()
plt.show()