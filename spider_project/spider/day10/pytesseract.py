import pytesseract
from PIL import Image

img=Image.open('test.jpg')

res=pytesseract.image_to_string(img)
print(res)