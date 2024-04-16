# image.py
# Name: Zaphod Beeblebrox (Harsh Shah, Ian Cunningham, and Elizabeth Stapleton)
# email: shahh4@mail.uc.edu, stapleet@mail.uc.edu, cunninig@mail.uc.edu
# Assignment Number: Final Project
# Due Date: 04/23/2024
# Course/Section: IS4010-002
# Semester/Year: Spring 2024
# Brief Description of the assignment: This shows a very very good picture of us
# Anything else that's relevant: Used worked done in class and ChatGPT as a reference. 
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO
 
 
def load_image( filename ) :
    '''
        Load an image file from disk
        @param: filename The file to load
        @return: the image object or None if error occurred
    '''
    try:
        myimage = Image.open(filename)
    except:
        #If I get here, an exception has occurred
        # 'Eat' the exception
        return None # give up and return nothing
    myimage.load()
    return myimage