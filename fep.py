import cv2 as cv
import freetype
import numpy as np

# Load an image as a blank canvas
image = np.zeros((400, 600, 3), dtype=np.uint8)

# Specify the text to display (Amharic)
amharic_text = "ሰላም እንደምን አልነበረንም"

# Choose a FreeType font
# font_path = "/System/Library/Fonts/Arial Unicode.ttf"  # Replace with an appropriate Amharic font path
font_path = "fonts/absy.ttf"
font_size = 20

face = freetype.Face(font_path)
face.set_char_size(font_size * 64)

# Create an OpenCV image with the Amharic text using FreeType
pos = (50, 200)
for char in amharic_text:
    face.load_char(char)
    bitmap = face.glyph.bitmap
    image[pos[1]:pos[1] + bitmap.rows, pos[0]:pos[0] + bitmap.width] |= np.array(bitmap.buffer, np.uint8).reshape(
        bitmap.rows, bitmap.width, -1)[:, :, 0]

    pos = (pos[0] + face.glyph.advance.x // 64, pos[1])

# Display the image
cv.imshow("Amharic Text", image)
cv.waitKey(0)
cv.destroyAllWindows()
