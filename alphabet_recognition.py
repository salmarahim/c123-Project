#Importing all the important models and install them if not installed on your device




#Fetching the data
X = np.load('image.npz')['arr_0']
y = pd.read_csv("labels.csv")["labels"]



#Splitting the data  with train_size=3500, test_size=500 and scaling it 

#scaling the features


#Fitting the training data into the model


#Calculating the accuracy of the model




# #Starting the camera

# print("camera started")

   # Capture frame-by-frame

    # # Our operations on the frame come here
   

    # #Drawing a box in the center of the video
   




    # #To only consider the area inside the box for detecting the digit
    # #roi = Region Of Interest
  


    # #Converting cv2 image to pil format


    # # convert to grayscale image - 'L' format means each pixel is 
    # # represented by a single value from 0 to 255



    # #invert the image
    # image_bw_resized_inverted = PIL.ImageOps.invert(image_bw_resized)
    # pixel_filter = 20
    # #converting to scalar quantity
    # min_pixel = np.percentile(image_bw_resized_inverted, pixel_filter)
    # #using clip to limit the values between 0,255
    # image_bw_resized_inverted_scaled = np.clip(image_bw_resized_inverted-min_pixel, 0, 255)
    # max_pixel = np.max(image_bw_resized_inverted)
    # #converting into an array
    # image_bw_resized_inverted_scaled = np.asarray(image_bw_resized_inverted_scaled)/max_pixel
    # #creating a test sample and making a prediction
    # test_sample = np.array(image_bw_resized_inverted_scaled).reshape(1,784)
    # test_pred = clf.predict(test_sample)
    # print("Predicted class is: ", test_pred)

#     # Display the resulting frame
#    



# # When everything done, release the capture


