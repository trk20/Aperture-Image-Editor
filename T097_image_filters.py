from Cimpl import*
from unit_testing import check_equal
import numpy
import matplotlib.pyplot as plt
from simple_Cimpl_filters import grayscale


def three_tone(image, color1:str, color2:str, color3:str) -> Image :
    """
    Muneer Bhola (101117746)
    Function definition for the "Three Tone" filter
    """
    new_image = copy(image)
    lst1 = ["black", "white", "blood", "green", "blood", "lemon", "cyan", "magenta", "gray"]
    lst2 = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(0,255,255),(255,0,255),(128,128,128)]
    temp1 = color1
    temp2 = color2
    temp3 = color3
    length_lst = len(lst1)
    
    for i in range(length_lst):
        if color1 == lst1[i]:
            temp1 =lst2[i] 
        if color2 == lst1[i]:
            temp2 =lst2[i]
        if color3 == lst1[i]:
            temp3 =lst2[i]
    for pixel in new_image:
        x,y,(r,g,b) = pixel
        color = get_color(new_image,x,y)
        brightness = (color[0] + color[1] + color[2]) // 3 
        if 0 <= brightness <= 84:
            r1, g1, b1 = temp1
            #pixel_color = create_color(r1, g1, b1)
            set_color(new_image, x, y, create_color(r1,g1,b1))
        elif 85 <= brightness <= 170:
            r1, g1, b1 = temp2
            #pixel_color = create_color(r1, g1, b1)
            set_color(new_image, x, y, create_color(r1,g1,b1))
        else:
            r1, g1, b1 = temp3
            #pixel_color = create_color(r1, g1, b1)
            set_color(new_image, x, y, create_color(r1,g1,b1))
    return new_image


#1-Filter Function
def extreme_contrast(image: Image) -> Image:

    """
    Lubna aboshaeir 101187928

    Returns a copy of the image given in which the contarts between the pixels has been maximized. In other words, a copy of the image will be returned with the brightest and darest colours possbile.

    file = choose_file()
    image = load_image(file)
    >>> image = extreme_contrast(image)
    >>> show (image)
    """

    image_new = copy(image)

    for pixel in image_new:
        x,y,(r,g,b) = pixel
        red, green, blue = (r,g,b)

        if red <= 127:
            red = 0
        else:
            red = 225

        if green > 127:
            green =225
        else:
            green = 0

        if blue > 127:
            blue = 255
        else:
            blue = 0

        new_colour_image = create_color(red,gren,blue)
        set_color(image_new,x,y,new_colour_image)
    return image_new

def sepia(image:Image)->Image:
    #Junayd DeMone
    #101186381    
    '''
    returns an image with a sepia tint apllied
    >>>sepia(load_image('p2-original.png'))
    sepia tinted image
    '''
    new_image = grayscale(image)
    height= get_height(image)
    width= get_width(image)
    new_image2= copy(new_image)

    for x in range(width):
        for y in range(height):
            c = get_color(new_image2,x,y)
            r,g,b = c
            if g < 63 :
                cc= create_color(r*1.1,g,b*0.9)
                set_color(new_image2,x,y,cc)
            if 63 <= g <= 191 :
                cc= create_color(r*1.15,g,b*0.85)
                set_color(new_image2,x,y,cc)
            if 191 < g :
                cc= create_color(r*1.08,g,b*0.93)
                set_color(new_image2,x,y,cc)
    return new_image2


def posterize(image: Image) -> Image:
    """
   Group 097
   Contributors: Timothy (101187187)
   March 10th, 2021
   
   Returns a single image with pixel r, g, and b values taken from three input pictures
   
   >>>combine(red_image, blue_image, green_image)
   Returns combined image
    """ 
    
    posterized_image = create_image(get_width(image),get_height(image)) #creates new image with same width and height of the red image
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        r = _adjust_component(r - r % (255/4) - 32)
        g = _adjust_component(g - g % (255/4) - 32)
        b = _adjust_component(b - b % (255/4) - 32)
        new_color = create_color(r,g,b)
        set_color (posterized_image, x, y, new_color) 
    return posterized_image

def detect_edges(original_image: Image, threshold) -> Image:
    """
    Muneer 101117746
    returns the image so that it appears like a pencil sketch, by changing 
    the pixel's colors to black or white depending on the brightness.

    >>>detect_edges(Image, 1)
    """
    edge_filter = copy(original_image)
    height = get_height(edge_filter)
    width = get_width(edge_filter)
    white = create_color(255, 255, 255)
    black = create_color(0, 0, 0)
    for x in range(width):
        set_color(edge_filter, x, height -1, white)
        for y in range(height-1):
            r1,g1,b1 = get_color(original_image, x, y)
            r2,g2,b2 = get_color(original_image, x, y+1)

            brightness_top = (r1 + g1 + b1)// 3
            brightness_bottom = (r2 + g2 + b2) //3 
            difference = (brightness_top - brightness_bottom)
            if difference > threshold:
                set_color(edge_filter, x, y, black)
            else:
                set_color(edge_filter, x, y, white)
    return edge_filter

def filter_draw(image: Image, curveColor: str,  point_list: list = None):
    """
    Group 097
    Contributors: Timothy (101187187)
    March 27th, 2021
    
    Given an image and a curve color, outputs an image with an interpolated 
    curve on it as well as a list of tuples containing all intersections 
    with the image borders
    
    >>>filter_draw(image,"black")
    Uses user inputed points to draw a black curve on the image
    
    >>>filter_draw(image,"blood", [(1,2),(2,3),(3,1),(4,0)])
    Uses points in third argument to draw a red curve on the image
    
    """
    width = image.get_width() # store width and height for ledgibility
    height = image.get_height()
    
    output_image = copy(image)
    
    if(curveColor == "black"): #converting string-->color
        color = create_color(0,0,0)
    elif(curveColor == "white"):
        color = create_color(255, 255, 255)
    elif(curveColor == "blood"):
        color = create_color(255, 0, 0)
    elif(curveColor == "green"):
        color = create_color(0, 255, 0) 
    elif(curveColor == "blue"):
        color = create_color(0, 0, 255)
    elif(curveColor == "lemon"):
        color = create_color(255, 255, 0)
    elif(curveColor == "aqua"):
        color = create_color(0, 255, 255)
    elif(curveColor == "pink"):
        color = create_color(255, 0, 255)
    else:
        color = create_color(128, 128, 128) #default to grey
    
    
    if(point_list == None): #Skips if there are points in the third argument
        numberPoints = eval(input("Enter number of points: ")) #points user input
        point_list = []
        for i in range(numberPoints): #points user input
            pointInput = ((input("Enter point #" + str(i+1) + " in format x,y: ")).split())
            for i in range(len(pointInput)):
                pointInput[i-1] = eval(pointInput[i-1])
            point_list.extend(pointInput)
    
    point_list.sort() #sort list of points by x values
    
    interpolated = _interpolation(point_list) #get polynomial function
    
    edge_intersections = _image_border_finding((width, height),interpolated)
    
    for x in range(width): #draw line corresponding with curve (bit thin / inconsistant when flat but what can ya do)
        for y_offset in range(abs(int(interpolated(x))-int(interpolated(x+1)))+1):
            for x_offset in range(9):
                if(int(interpolated(x)) + int(numpy.sign(int(interpolated(x))-int(interpolated(x+1))))*y_offset <= height-1 and int(interpolated(x)) + int(numpy.sign(int(interpolated(x))-int(interpolated(x+1))))*y_offset >= 0 and x - x_offset + 4 >= 0 and x - x_offset + 4 <= width -1):
                    set_color(output_image,x - x_offset + 4, int(interpolated(x)) + int(numpy.sign(int(interpolated(x))-int(interpolated(x+1))))*y_offset,color)      
    
    return (output_image, edge_intersections)

def _interpolation(pointList: list):
    """
    Group 097
    Contributors: Timothy (101187187)
    March 25th, 2021
    Returns a polynonial equation given a set of x,y coordinates.
    
    >>>_interpolation([(1,2),(2,3),(3,1),(4,0)])
    Returns a function:
          2
    -0.5 x + 1.7 x + 1
    """
    x_list,y_list = get_x_y_lists(pointList)[0],get_x_y_lists(pointList)[1]
    if(len(pointList) > 2):
        
        f = numpy.poly1d(numpy.polyfit(x_list, y_list, 2)) #using poly1d for ease of use, using quadratic fit
        return f
        
        
    elif(len(pointList) > 1):
        
        f = numpy.poly1d(numpy.polyfit(x_list, y_list, 1)) #linear fit this time, again poly1d for ease of use
        return f
    
    else:
        print("ERROR!!! YOU HAVE GIVEN TOO FEW POINTS!!!") #throw error if too few points

def  _image_border_finding(image_size, interpol: numpy.poly1d) -> int:
    """
    Finds all real intersections with a given rectangular size and poly1d polynomial equation
    Returns results as list of tuples
    (Also works with higher degree polynomials, give it a try!)
    
    >>>_image_border_finding((100,100),numpy.poly1d(numpy.polyfit([1,2,3], [0,1,0], 2)))
    -Returns: [(1, 0), (2, 0)]
    
    Group 097
    Contributors: Timothy (101187187)
    March 26th, 2021
    """
    
    edges = []
    
    if(int(interpol(0)) >= 0 and int(interpol(0)) <= image_size[1]-1): #left and right border
        edges.append((0,int(interpol(0)))) 
    elif(int(interpol(image_size[0])) >= 0 and int(interpol(image_size[0])) <= image_size[1]-1):
        edges.append((image_size[0],int(interpol(0))))
    
    for i in range(len(numpy.roots(interpol))): #bottom border
        if(numpy.isreal(numpy.roots(interpol)[i]) and int(numpy.roots(interpol)[i]) >= 0 and int(numpy.roots(interpol)[i]) <= image_size[0]): # solve for roots at y= 0
            edges.append((int(numpy.roots(interpol)[i]),0)) 
    
    interpol[0] -= image_size[1] - 1 #changes y value to be able to solve for given image height (15 = x^3 + x^2 + 3 ---> 0 = x^3 + x^2 -12) 
    
    for i in range(len(numpy.roots(interpol))): #top border
        if(numpy.isreal(numpy.roots(interpol)[i]) and int(numpy.roots(interpol)[i]) >= 0 and int(numpy.roots(interpol)[i]) <= image_size[0]): # solve for roots at y= image height
            edges.append((int(numpy.roots(interpol)[i]),image_size[1] - 1))
    
    interpol[0] += image_size[1] + 1 #returns y value to original
    
    edges.sort()
    return edges
    
def flip_vertical(image:Image)->Image:
    #Junayd DeMone
    #101186381    
    """
    Flips a picture vertically from the middle of its height
    >>>flip_vertical(load_image('p2-original.png'))
    returns image flipped vertically 
    
    """

    copied_image= copy(image)
    height= get_height(copied_image)
    width= get_width(copied_image)


    for x in range(width):
    
        for y1 in range((height// 2)):
            
            for y2 in range (((height// 2)),(height)):
                
                if height% 2 == 0 :
                    if (height// 2) - y1 == y2 - ((height// 2))+ 1 :

                        c1= get_color(copied_image,x,y1)
                        r1,g1,b1 = c1
                        c2 = get_color(copied_image,x,y2)
                        r2,g2,b2 = c2
                        set_color(copied_image,x,y1,c2)
                        set_color(copied_image,x,y2,c1)
                else:
                    
                    if (height//2) - y1 == y2 - ((height//2)) :

                        c1= get_color(copied_image,x,y1)
                        r1,g1,b1 = c1
                        c2 = get_color(copied_image,x,y2)
                        r2,g2,b2 = c2
                        set_color(copied_image,x,y1,c2)
                        set_color(copied_image,x,y2,c1)   
                        
    return copied_image

def flip_horizontal(image:Image)->Image:
    #Junayd DeMone
    #101186381    
    """
    Flips a picture horizontaly from the middle of its width
    >>>flip_horizontal(load_image('p2-original.png'))
    returns image flipped horizontally 
    
    """    
    
    copied_image= copy(image)
    height= get_height(copied_image)
    width= get_width(copied_image)

    for y in range(height):
        
        for x1 in range(width// 2):
            
            for x2 in range ((width// 2),width):
                
                if width% 2 == 0:
                
                    if (width// 2) - x1 == x2 - (width// 2)+ 1 :
                        c1= get_color(copied_image,x1,y)
                        r1,g1,b1 = c1
                        c2 = get_color(copied_image,x2,y)
                        r2,g2,b2 = c2
                        set_color(copied_image,x1,y,c2)
                        set_color(copied_image,x2,y,c1)
                        
                else:
                    
                    if (width// 2) - x1 == x2 - (width// 2) :
                        c1= get_color(copied_image,x1,y)
                        r1,g1,b1 = c1
                        c2 = get_color(copied_image,x2,y)
                        r2,g2,b2 = c2
                        set_color(copied_image,x1,y,c2)
                        set_color(copied_image,x2,y,c1)
                    
    return copied_image



#Other functions
def get_x_y_lists(points:list) -> list:
    """
    Returns a list containing two lists: the x coordinates, and the y
    coordinates given a list of point tuples.
    
    >>> get_x_y_lists([(1,4),(2,3)])
    [ [1,2], [4,3] ]
    >>> get_x_y_lists([(1,1),(2,2),(3,3)])
    [ [1,1,1], [2,2,2] ]
    >>> get_x_y_lists([(0,10),(20,37),(99,120),(200,0)])
    [ [0,20,99,200], [10,37,120,0] ]
    """
    xlist = []
    ylist = []
    for (x,y) in points:
        xlist += [x]
        ylist += [y]
    return [xlist,ylist]

def _adjust_component(comp):
    """Return comp as an integer between 0 and 255, inclusive, returning 0
    if comp is negative and capping values >= 256 at 255.
    """
    comp = int(comp)
    return max(0, min(255, comp))