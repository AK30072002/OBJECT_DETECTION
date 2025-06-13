**SENSOR FUSION**

**Introduction**
	HII ALL, In this project , I used two sensor reading they are camera & ultrasonic  to detect real time object with distance using more than one sensor for more accuracy then it is called as sensor fusion.

**Requirements**
	*RASPBERRY PI 5
	*ARDUINO NANO
	*ROBOFLOW ACCOUNT
	*GOOGLE COLAB ACCOUNT
	*RPI 5 CAMERA
	*ULTRASONIC SENSOR
	*JUMPER WIRES
	*HDMI TO MINI HDMI CABLE
	*TYPE – C ADAPTER
	
**DATASET COLLECTION :**
	I used a pendrive as my object I add the path of the image pendrive #sample img 1.jpg & #pendrive sample img 2.jpg
Then a video sample - #pendrive (object).mp4
Here is the link for full data set image - #data_set_pendrive_detection
This all image should be upload in the roboflow workspace and then it should be annotated and make as a dataset for Machine Learning for model yolov8
And training should done in the colab
These code are in the file I attach in repository - #roboflow and google colab step by guide.txt
After this step guide you will have .pt file which is the trained model for object detection. I attach file in repository - #pendrive.pt

**CODE FOR NANO**
	In nano we measure the distance using ultrasonic sensor and transmit it to the rpi5 using i2c. you may have doubt like why we are using nano for measure the distance but ultrasonic sensor uses 5V as logic while rpi5 uses 3.3V as logic, so we need logic converter I don’t have it so I go with this….

I have each part each code and final code
1-	nano to rpi5 using i2c - #nano_to_rpi5.ino
2-	ultrasonic sensor interface with nano - #ultrasonic nano.ino
3-	over all code - #ultrasonic_and_i2c.ino

pin connection refer the code or mail me or contact me using the link provided in BIO.

**CODE FOR RPI 5**
	In rpi 5 we implement object detection with distance similar for nano we have separate code each of this
1->  camera test - #camera test in rpi5.py
2-> distance from the nano - #distance getting from nano.py
3-> object detection without distance - #object detection without distance.py
4-> overall code - #overall code.py

pin connection refer the code or mail me or contact me using the link provided in BIO.

**OUTPUT :**
	The output is taken as video I attach file in repository - #output video_1.mp4 & #output video_2.mp4

**RESULT :**
	The output will display the object detection with the distance with is known to be sensor fusion.


**THANK YOU 
IF YOU HAVE ANY DOUBT CONTACT ME
(CHECK IN MY BIO)**

