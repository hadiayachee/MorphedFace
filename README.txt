This project will output a morphed image face developed from two face images given by the user.
Please install the packages listed in MorphedFace-dynamic/requirements.txt file
Please install shape_predictor_68_face_landmarks.dat  from the following github link
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
and then add it into MorphedFace-dynamic/tools/ 
Please add the path of first image into the variable img_path_one found in MorphedFace-dynamic/main.py
Please add the path of the second image into the variable img_path_two in MorphedFace-dynamic/main.py
You can edit the variable alpha, between 0 and 1, in MorphedFace-dynamic/main.py to change the output image.
If you choose the value zero then the algorithm will output the first image without any change.
If you choose the value one, then the algorithm will output the second image without any change.
In order to run the algorithm, please make sure you read and applied the previous lines, then open your terminal and type 'python main.py' or 'python3 main.py' and enjoy the magic.