from PIL import Image
import numpy as np
import os
import sys

def invert_black_white(input_path, output_path):
    # Open the image
    image = Image.open(input_path).convert('RGBA')
    
    # Convert image to numpy array
    data = np.array(image)
    
    # Invert black and white colors
    for y in range(data.shape[0]):
        for x in range(data.shape[1]):
            r, g, b, a = data[y, x]
            if a > 0:  # Check if the pixel is not transparent
                if r < 50 and g < 50 and b < 50:  # If the pixel is dark (black)
                    data[y, x] = [255, 255, 255, a]  # Change to white
                elif r > 200 and g > 200 and b > 200:  # If the pixel is light (white)
                    data[y, x] = [0, 0, 0, a]  # Change to black
    
    # Convert numpy array back to image
    output_image = Image.fromarray(data)
    
    # Save the output image
    output_image.save(output_path)
    print("Inversion complete.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = os.path.splitext(input_image_path)[0] + '_inverted.png'

    invert_black_white(input_image_path, output_image_path)
    print(f"Inverted image saved to {output_image_path}")
