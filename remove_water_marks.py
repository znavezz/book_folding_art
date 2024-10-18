from PIL import Image
import numpy as np
import os
import sys
import time

def webp_to_png(input_path, output_path):
    # Open the webp image
    image = Image.open(input_path).convert('RGBA')
    
    # Convert image to numpy array
    data = np.array(image)
    
    # Change non-black pixels to white, but be more forgiving for dark colors
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            r, g, b, a = data[y, x]
            if a > 0:  # Check if the pixel is not transparent
                if not (r < 50 and g < 50 and b < 50):  # If the pixel is not very dark
                    data[y, x] = [255, 255, 255, a]
    
    # Convert numpy array back to image
    output_image = Image.fromarray(data)
    
    # Save the PNG file
    output_image.save(output_path)
    print("Processing complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_webp_path>")
        sys.exit(1)

    input_webp_path = sys.argv[1]
    output_png_path = os.path.splitext(input_webp_path)[0] + '.png'

    webp_to_png(input_webp_path, output_png_path)
    print(f"Processed PNG saved to {output_png_path}")
