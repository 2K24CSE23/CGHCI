##### This assignment is done by me(Ahtsham, 2K24/CSE/23) and not by AI.

# Here we are getting user inputs
w = int(input("Enter horizontal resolution (pixels): "))
h = int(input("Enter vertical resolution (pixels): "))
d = float(input("Enter physical diagonal size (inches): "))

# 2. Calculations
total_pixels = w * h

# Aspect ratio (using continuous subtraction/modulo logic to find GCD without math library)
a, b = w, h
while b:
    a, b = b, a % b
gcd = a

aspect_w = w // gcd
aspect_h = h // gcd

# Screen DPI calculation (using ** 0.5 for square root)
diagonal_px = (w**2 + h**2) ** 0.5
dpi = diagonal_px / d

# 3. Classify display density
if dpi < 100:
    category = "Low Density (Standard Monitor)"
elif 100 <= dpi <= 200:
    category = "Medium Density (HD Display)"
else:
    category = "Mobile"

# Display output using f strings
print("\n--- DISPLAY METRICS ANALYSIS ---")
print(f"Total Pixel Count : {total_pixels:,} pixels")
print(f"Aspect Ratio      : {aspect_w}:{aspect_h}")
print(f"Calculated DPI    : {round(dpi, 2)} DPI")
print(f"Density Category  : {category}")