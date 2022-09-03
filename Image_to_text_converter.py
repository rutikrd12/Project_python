from PIL import Image
import pytesseract
import numpy

tesseract_path= input("enter the tesseract path:")
inupt_path=input("enter file path:")

pytesseract.tesseract_cmd = tesseract_path

img = Image.open(inupt_path)

text = pytesseract.image_to_string(img)

f=open(inupt_path+'.txt','a',encoding='utf-8')

f.write(text)

f.close()

print("File Successfuly converted to text...")



