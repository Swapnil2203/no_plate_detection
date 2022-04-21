import cv2
import os
from detect_box_yolo import detect_box
import os, io
from symtable import Symbol
from unicodedata import digit
import re
from google.cloud import vision
from google.cloud.vision import types
import googletrans
from googletrans import *


def draw_roi(frame, rois, color_box):
    for roi in rois:
        cv2.rectangle(frame, (roi[0], roi[1]), (roi[2], roi[3]), color_box, thickness=2)
            
        # cv2.putText(frame, str(roi[4]), (roi[0] +30 , roi[1] - 2), cv2.FONT_HERSHEY_SIMPLEX,
        #                 1, (255, 0, 255), 2, lineType=cv2.LINE_AA)

        x,y,w,h = roi[0],roi[1],roi[2],roi[3]
        cropped_img=frame[y:h, x:w]
        success, encoded_image = cv2.imencode('.jpg', cropped_img)
        roi_image = encoded_image.tobytes()

         #the JSON file 
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'static-subject-343913-2bc5fd3da2ab.json'


        image = vision.types.Image(content=roi_image)
        client = vision.ImageAnnotatorClient()

        response = client.document_text_detection(image=image)

        my_text=""
        for r in response.text_annotations:
            my_text = my_text + r.description
            break
    


        # clean_text = re.sub('[\W_]+', '', my_text)


        translator = googletrans.Translator()
        translate = translator.translate(my_text, dest = 'en')
        translated_text = translate.text
        print("Translated_text",translated_text)



    return frame,my_text

def call_fun(path):
    print("Path: ",path)
    # path="E:/Resoluteai_tasks/Android_app/Number_plate_detection/Backend/test.jpg"
    color_box = (140,101,211)
    img=cv2.imread(path)
    rois = detect_box(img, 0.1)
    print("ROIS:  IS :::  ",rois)
    final_image,text=draw_roi(img, rois, color_box)
    # text = pytesseract.image_to_string(img)
    # print("Final_image: ",final_image)
    path ='./'
    # cv2.imshow("output", img)
    filename = 'result.jpg'
    print(path+filename)
    cv2.imwrite(path+filename,final_image)
    return text
