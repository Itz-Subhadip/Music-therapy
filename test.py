import cv2
#import tensorflow as tf
from deepface import DeepFace
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Start
def result(request):
   return render(request,'result.html',{'dominant_emotion1': result1.get('dominant_emotion'),'dominant_emotion2': result2.get('dominant_emotion')})
   

def test(request):
   cap = cv2.VideoCapture(0)
   i=0
   global result1
   while (i!=100):
    # Capture frame-by-frame
    ret, frame1 = cap.read()
    
    # Pre-process the frame for the model
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (48, 48))
    gray = gray / 255.0
    # Display the resulting frame
    cv2.imshow('Webcam', frame1)
    i=i+1
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
   cap.release()
   cv2.destroyAllWindows()
   result = DeepFace.analyze(frame1)
#print(result)
   result1=result
   print(result.get('dominant_emotion'))

   return render(request, 'emotion1.html',{'dominant_emotion': result.get('dominant_emotion')})
#test()

def test2(request):
   cap = cv2.VideoCapture(0)
   i=0
   global result2
   while (i!=100):
    # Capture frame-by-frame
    ret, frame2 = cap.read()
    
    # Pre-process the frame for the model
    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (48, 48))
    gray = gray / 255.0
    # Display the resulting frame
    cv2.imshow('Webcam', frame2)
    i=i+1
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
   cap.release()
   cv2.destroyAllWindows()
   result = DeepFace.analyze(frame2)
#print(result)
   result2=result
   return render(request, 'emotion2.html',{'dominant_emotion': result.get('dominant_emotion')})
