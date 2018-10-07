import sys
import io
from google.cloud import vision
from google.cloud.vision import types


"""Detects text in the file."""
path = sys.argv[1]



client = vision.ImageAnnotatorClient()

with io.open(path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)

response = client.text_detection(image=image)
texts = response.text_annotations
print('Texts:')

for text in texts:
    print('\n"{}"'.format(text.description))

    if "Participant" in text.description:
        print ("patient found!")
        break

    if "Future" in text.description:
        print ("visitor found!")
        break
    
    if "Mentor" in text.description:
        print ("Nurse found!")
        break

    if "SanDiego" in text.description:
        print ("Physician found!")
        break

    
    
    
    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in text.bounding_poly.vertices])

    ##print('bounds: {}'.format(','.join(vertices)))

print ("done")


