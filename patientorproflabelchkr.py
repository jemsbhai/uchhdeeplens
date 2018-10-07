import boto3
import sys



bucket='uchealthhacks'
##photo='labeltest.jpg'

photo = sys.argv[1]

client=boto3.client('rekognition')


response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})

                    
textDetections=response['TextDetections']
##print (response)
##print ('Matching faces')
for text in textDetections:
        print ('Detected text:' + text['DetectedText'])
        if text['DetectedText'].lower() == "participant" :
            print ("patient detected!")
            break
        if "San Diego" in text['DetectedText']:
            print ("doctor detected!")
            break
        if "xxxx" in text['DetectedText']:
            print ("visitor detected!")
            break
        

        
##        print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
##        print ('Id: {}'.format(text['Id']))
##        if 'ParentId' in text:
##            print ('Parent Id: {}'.format(text['ParentId']))
##        print ('Type:' + text['Type'])


print ("done")
