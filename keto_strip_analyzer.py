import cv2 as cv
import numpy as np

# Set the path to the ketostrip image
image_path = 'path/to/your/image.png'

def hex_to_hsv(hex_color):
    hex_color = hex_color.lstrip('#')
    rgb_color = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    bgr_color = rgb_color[::-1]
    hsv_color = cv.cvtColor(np.uint8([[bgr_color]]), cv.COLOR_BGR2HSV)[0][0]
    return hsv_color

colors_hsv = {
    "negative": hex_to_hsv("#fabd98"),  
    "0.5 mmol/L - Trace amounts": hex_to_hsv("#f7a98d"),  
    "1.5 mmol/L - Small amounts": hex_to_hsv("#f1848e"),  
    "4.0 mmol/L - Moderate amounts": hex_to_hsv("#ca5973"),  
    "8.0 mmol/L - Large amounts": hex_to_hsv("#963964"),  
    "16.0 mmol/L - Large amounts": hex_to_hsv("#772958"),  
}

image = cv.imread(image_path)

hsv_image = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# Mask values that are too white (reflections)
value_threshold = 150
mask = hsv_image[:, :, 2] < value_threshold

masked_hsv_image = np.zeros_like(hsv_image)
masked_hsv_image[mask] = hsv_image[mask]

masked_bgr_image = cv.cvtColor(masked_hsv_image, cv.COLOR_HSV2BGR)

# Display the masked image
cv.imshow('Masked Image', masked_bgr_image)

# Calculate the average HSV color of the non-excluded part of the image
average_hsv = np.mean(masked_hsv_image[mask], axis=0)
average_bgr = cv.cvtColor(np.uint8([[average_hsv]]), cv.COLOR_HSV2BGR)[0][0]

# Create an image to display the average color
average_color_image = np.full((100, 100, 3), average_bgr, dtype=np.uint8)
cv.imshow('Original Image', image)
cv.imshow('Average Color', average_color_image)
cv.waitKey(0)
cv.destroyAllWindows()

def find_closest_color(average_hsv, colors_hsv):
    closest_color = None
    min_distance = float('inf')

    for color_name, hsv_value in colors_hsv.items():
        distance = np.linalg.norm(average_hsv - hsv_value)
        if distance < min_distance:
            min_distance = distance
            closest_color = color_name

    return closest_color

# Find the closest color
closest_color = find_closest_color(average_hsv, colors_hsv)
print(f"Estimation: {closest_color}")

