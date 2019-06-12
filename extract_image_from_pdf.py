
import PyPDF2
from PIL import Image
import os

def extract_image(filename):
    savedir = filename[:-4].replace("pdf", "image") + "/"
    os.makedirs(savedir, exist_ok=True)


    input1 = PyPDF2.PdfFileReader(open(filename, "rb"))
    for k in range(input1.numPages):
      page0 = input1.getPage(k)

      if '/XObject' in page0['/Resources']:
          xObject = page0['/Resources']['/XObject'].getObject()

          for obj in xObject:
              if xObject[obj]['/Subtype'] == '/Image':
                  size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                  data = xObject[obj].getData()
                  if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                      mode = "RGB"
                  else:
                      mode = "P"

                  if '/Filter' in xObject[obj]:
                      if xObject[obj]['/Filter'] == '/FlateDecode':
                          img = Image.frombytes(mode, size, data)
                          img.save(savedir + obj[1:] + ".png")
                      elif xObject[obj]['/Filter'] == '/DCTDecode':
                          img = open(savedir + obj[1:] + ".jpg", "wb")
                          img.write(data)
                          img.close()
                      elif xObject[obj]['/Filter'] == '/JPXDecode':
                          img = open(savedir + obj[1:] + ".jp2", "wb")
                          img.write(data)
                          img.close()
                      elif xObject[obj]['/Filter'] == '/CCITTFaxDecode':
                          img = open(savedir + obj[1:] + ".tiff", "wb")
                          img.write(data)
                          img.close()
                  else:
                      img = Image.frombytes(mode, size, data)
                      img.save(obj[1:] + ".png")
      else:
          pass
          # print("No image found.")