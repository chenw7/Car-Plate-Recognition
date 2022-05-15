# Car-Plate-Recognition

Before you can execute the code, there are a few programs/applications and program extensions that need to be installed on your computer: 
1. python (high-level programming language)
2. anaconda (allows for data science package installation in python)
3. homebrew (package manager for macOS)
4. pip (package installer for python)

Here are the steps to follow in order to correctly set up your computer to run the hand-tracking program.

1. Firstly, python must be installed. However, we don't have to directly install it from the python website. Instead, we can install python and pip, quickly and efficiently, both with homebrew.

2. To install homebrew, open your terminal and type in the following command.

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    Further instructions will be provided in your terminal to assist you in installing homebrew. 

3. To check if homebrew is installed correctly, type the following command into your terminal.
 
        brew help
    
    If an error does not appear, that means homebrew has been successfully installed and you are ready for the next steps.
    If an error appears, repeat step 2 and make sure you followed the instructions provided in your terminal correctly.
    
4. Once homebrew has been installed, we can install both python and pip with entering the following command into your terminal.
 
        brew install python
    
    This command installs the latest version of python, pip, and necessary packages for set up all for you without you needing to do anything. Simply sit back and 
    wait for homebrew to finish installing all the programs and packages for you.
    
5. To test out if python has been correctly installed, type the following command into your terminal.

        python3
    
    If an error does not appear, python has successfully been installed!
    If an error does appear, repeat steps 3-4.

6. Now that python has been installed, it's time to install anaconda which will allow for data science packages to be imported into python. Use the following link to install the latest version of anaconda.

    https://www.anaconda.com/products/individual
    
    Follow the instructions provided by the anaconda installation package and install anaconda on your computer.

7. To check if anaconda has been installed properly, open the anaconda application. The interface should say anaconda navigator and have various options of what IDE to launch.

    If anaconda does not open, reinstall the application (possibly with a different version).

8. Once anaconda has been installed, launch jupyter notebook and a new tab on your browser will be opened. It should look similar to the picture below.
<img width="1145" alt="Screen Shot 2022-03-09 at 8 35 13 AM" src="https://user-images.githubusercontent.com/91576538/157349691-ad95c212-6de1-4f2c-8c7b-139b2470e00b.png">
    
9. Select the location in which you would like to store your python files. Once you have reached the folder/location you would like to store your file, create a new jupyter notebook (On the top left corner, click new, and then click python3). <img width="1156" alt="Screen Shot 2022-03-09 at 9 02 40 AM" src="https://user-images.githubusercontent.com/91576538/157352417-4922dbff-ef54-40de-a57d-6ef63fe3ee02.png">

10. Once your notebook has been created, click on the link below to see the source code to the car plate recognition program (explanations to the code are included as comments in the source code).

      https://github.com/chenw7/Car-Plate-Recognition/blob/main/License%20Plate%20Recognition.py
        
11. Install the necessary libraries to run the program using pip (in your terminal). Enter the following commands in your terminal.

        pip install opencv-python==3.4.8.29
       
        pip install opencv-contrib-python==3.4.8.29
        
        pip install numpy
        
        pip install matplotlib
        
        pip install imutils
        
        pip install easyocr
        
12. Now that all necessary libraries and accessories for the program have been installed, check whether they have been installed correctly by typing the following command into jupyter notebook and executing the command (execute the command by clicking command+enter).

        import cv2
        from matplotlib import pyplot as plt
        import numpy as np
        import imutils
        import easyocr
        
       If an error message does not appear, you can proceed onto the next step.
        
13. Copy the code (provided in step 10) into jupyter notebook and pay attention to line 14. 
<img width="401" alt="Screen Shot 2022-05-15 at 3 41 01 PM" src="https://user-images.githubusercontent.com/91576538/168462504-a3ac8d19-fb2b-4f8c-952f-fffe6d4409a0.png">

The line contains a reference to an image named "plate1.jpg" which should be stored in the same folder as your program (as demonstrated in the following).

<img width="256" alt="Screen Shot 2022-05-15 at 3 43 58 PM" src="https://user-images.githubusercontent.com/91576538/168462606-22ed843f-f781-4978-8756-2d99e4f7b81b.png">

Modify line 14 as needed and that will essentially be the only change you will need to make to the code provided.


14. Now that you have stored the images in the same folder as the program and initialized the program as needed, execute the program. The license plate should be identified and images of the license plate should be displayed (grayscale image of car, noise-reduced car image, cropped out license plate...).

15. If errors regarding cv2 or any of the other modules still exist, search for solutions on stackoverflow (most solutions to your problems can be found).

Output:

In my example, I used the following image as my license plate.

![plate1](https://user-images.githubusercontent.com/91576538/168462633-e1b05a56-05bf-4eeb-b7bb-32a56a980fce.jpeg)

After the execution of the program, here are the images that were printed.
<img width="348" alt="Screen Shot 2022-05-15 at 3 46 32 PM" src="https://user-images.githubusercontent.com/91576538/168462752-46dd5c5c-56f9-4ad9-8814-a0b17f2987b1.png">

<img width="342" alt="Screen Shot 2022-05-15 at 3 46 40 PM" src="https://user-images.githubusercontent.com/91576538/168462754-00e7cd73-c82d-4d3b-a38c-1cdb60ab1c0a.png">

<img width="343" alt="Screen Shot 2022-05-15 at 3 47 02 PM" src="https://user-images.githubusercontent.com/91576538/168462758-70ae0bf9-9604-4ea6-9018-c21153c2dd02.png">

<img width="377" alt="Screen Shot 2022-05-15 at 3 47 08 PM" src="https://user-images.githubusercontent.com/91576538/168462760-ad1f8e3b-c654-4091-af27-f1a73e325653.png">

<img width="340" alt="Screen Shot 2022-05-15 at 3 47 15 PM" src="https://user-images.githubusercontent.com/91576538/168462762-3f21d02c-7e9a-43b5-8496-aec150668be4.png">
