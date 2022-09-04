print()
print("...............PDF TO TEXT CONVERTER...............")
print("                                                   ")

import PyPDF2
import os

try:
    file = input('Enter the pdf file location:')
except:
    print("Please enter the currect file path")
    
doc=PyPDF2.PdfFileReader(file)

pages=doc.getNumPages()

print()
if pages == 0:
    print("Number of pages in file:",pages)
    print()
    print(pages,"pages converting to text...", )
else:
    print("Number of pages in file:",pages)
    print()
    print(pages,"pages converting to text...", )


output_file_name = os.path.splitext(file)[0]

for i in range(pages):

    curr_page=doc.getPage(i)
    
    text=curr_page.extractText()
    
    f=open(output_file_name+'.txt','a',encoding='utf-8')
    
    f.write(text)
    
    f.close()

print("File Successfully converted to text...")    
    