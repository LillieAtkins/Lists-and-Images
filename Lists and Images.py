"""
CS101
HW8
Lillie Atkins
Lab X
November 15, 2017
"""

def power(L, exponent):
    """
    Takes a list of numbers and returns a new list with every item increased to the power of the exponent integer provided.
    """
    return [item**exponent for item in L]

def average(L):
    """
    Takes a list of numbers and finds the average of it.
    """
    s = 0                    #need to define s before I can use it later
    for i in range(len(L)):  #if using indexing for s then need the iterater to have do with indexing as in the range(len(L))
        s = s + L[i]
    return s/len(L)


def pigLatin(s):
    """
    Takes a string and returns a new string with every word converted to pig latin.
    """
    L = s.split(" ")
    newL = []
    for item in L:
        if len(item) <= 1:
            newL.append(item)
        elif item[0] in 'aeiou' or item[0] in 'AEIOU':  #use python keyword in to check if item[0] is any other these letters instead of having to write a bunch of if item[0] == a ... statements
            newL.append(item +'yay')
        else:
            newL.append(item[1:] + item[0] + 'ay')
    return ' '.join(newL)                              #punctuation_for_joining_with.join(list name or ["actual", "list", "items"]


from PIL import Image

def grayscale(image):
    """
    Takes in an image and returns a grayscale (black and white) version.
    """
    newImage = image.copy()
    pixels = newImage.load()
    minX, minY, width, height = image.getbbox()
    for y in range(height):
        for x in range(width):
            rgb = pixels[x,y]
            avg = int((rgb[0] + rgb[1] + rgb[1])/3)
            pixels[x,y] = (avg, avg, avg)
    return newImage

def mirror(image):
    """
    Takes an image and returns another image that has the left side reflected across the center line onto the right side.
    """
    newImage = image.copy()
    pixels = newImage.load()
    minX, minY, width, height = image.getbbox()
    for y in range(height):
        #for x in range(width):
            #rgb = pixels[x,y]
        for x in range(width//2, width):
            pixels[x,y] = pixels[(width-1)-x, y]
    return newImage

def sepia(image):
    """
    Takes in an image and returns a sepia version of the image.
    """
    newImage = image.copy()
    pixels = newImage.load()
    minX, minY, width, height = image.getbbox()
    for y in range(height):
        for x in range(width):
            rgb = pixels[x,y]
            avg = int((rgb[0] + rgb[1] + rgb[1])/3)
            if avg <= 62:
                pixels[x,y] = (int(1.1*avg), avg, int(0.9*avg))
            elif avg <= 192:
                pixels[x,y] = (int(1.15*avg), avg, int(0.85*avg))
            else:
                pixels[x,y] = (int(1.08*avg), avg, int(0.93*avg))
            if pixels[x,y][0] > 255:
                pixels[x,y][0] = 255
    return newImage

def grayscaleWeighted(image, redWeight, greenWeight, blueWeight):
    """
    Takes in an image as well as decimal weights for each of the following color channels and returns a grayscale (black and white) version with a weighted average of these channels.
    """
    newImage = image.copy()
    pixels = newImage.load()
    minX, minY, width, height = image.getbbox()
    for y in range(height):
        for x in range(width):
            rgb = pixels[x,y]
            Wavg = int(rgb[0]*redWeight + rgb[1]*greenWeight + rgb[1]*blueWeight)
            pixels[x,y] = (Wavg, Wavg, Wavg)
    return newImage


def fourUp(image):
    """
    Takes in an image and returns a image that has four 1/4 sized versions of the original in it.
    """
    newImage = image.copy()                        #create a new image
    pixels = newImage.load()                       #loads this into a grid
    minX, minY, width, height = image.getbbox()    
    for y in range(0, height, 2):                  #the third number in the range() means skip by that much
        for x in range(0, width, 2):
            rgb = pixels[x,y]                      #this loads the pixels at every skipped number so 0, 2, 4, 6...
            pixels[x/2,y/2] = pixels[x, y]         #this compiles the pixels as if they were 0, 1, 2 that's why you divide so the pixels end up next to each other
    for y in range(0, height//2):                  
        for x in range (width//2, width):          #for the top left corner
            pixels[x,y] = pixels[x-width//2, y]    #copy the top right corner picture (the small image you have already created)
    for y in range(height//2, height):
        for x in range(0, width//2):               #for the bottom right corner
            pixels[x,y] = pixels[x, y-height//2]   #copy the top right corner picture (the small image you have already created)
        for x in range (width//2, width):          #for the bottom left corner
            pixels[x,y] = pixels[x-width//2, y-height//2]   #copy the top right corner picture (the small image you have already created)
    return newImage