from Cimpl import*
from unit_testing import check_equal
import numpy
import matplotlib.pyplot as plt
from simple_Cimpl_filters import grayscale
from T097_P4_image_filters import *

def test_red_channel() -> None:
    """
    Group T097
    Contributor: Muneer Bhola, 101117746
    March 11th, 2021
    
    A test fuction for red_filter
    >>>test_red_chanel()
    """
    original = create_image(3, 1)
    set_color(original, 0, 0,  create_color(0, 0, 0))
    set_color(original, 1, 0,  create_color(128, 127, 128))
    set_color(original, 2, 0,  create_color(255, 255, 255))
   
    
    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0,0,0))
    set_color(expected, 1, 0,  create_color(128,0,0))
    set_color(expected, 2, 0,  create_color(255,0,0))
    
    actual_red_image = red_channel(original)
    print("testing red_filter")
    for x, y, col in actual_red_image:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

def test_green_channel() -> None: 
    # lubna aboshaeir 
    # 101187928    
    """
    
    >>> test_green_channel()
    
    """
    
    original = create_image(3,2)
    
    set_color(original, 0,0 , create_color(0,0,0))
    set_color(original, 1,0 , create_color(255,255,255))
    set_color(original, 2,0 , create_color(20,40,20))
    set_color(original, 0,1 , create_color(255,0,255))
    set_color(original, 1,1 , create_color(25,255,0))
    set_color(original, 2,1 , create_color(52,255,0))
    
    
    expected = create_image(3,2)

    set_color(expected, 0,0 , create_color(0,0,0))
    set_color(expected, 1,0 , create_color(0,255,0))
    set_color(expected, 2,0 , create_color(0,40,0))
    set_color(expected, 0,1 , create_color(0,0,0))
    set_color(expected, 1,1 , create_color(0,255,0))
    set_color(expected, 2,1 , create_color(0,255,0)) 
    
    green_image = green_channel(original)
    
    for x, y, col in green_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
        col, get_color(expected, x, y))   

def test_blue_channel()->None :
    original= create_image(3,1)
    set_color(original,0,0,create_color(0,0,0))
    set_color(original,1,0,create_color(134,78,90))
    set_color(original,2,0,create_color(255,255,255))
    
    expected= create_image(3,1)
    set_color(expected,0,0,create_color(0,0,0))
    set_color(expected,1,0,create_color(0,0,90))
    set_color(expected,2,0,create_color(0,0,255))
    
    actual_filtered_image= blue_channel(original)
    for x,y,col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


def test_combine() -> None:
    """
    Group 097
    Contributors: Timothy
    March 10th, 2021
    
    A test function for combine
    >>>test_combine()
    """
    #This test function checks if combine sucessfully combines:
    #(0, 0, 0),(0, 0, 0), and (0, 0, 0) into (0, 0, 0) # all black
    #(0, 255, 255), (255, 0, 255), and (255, 255, 0) into (0, 0, 0) # different colors than those that should be used
    #(120, 0, 0), (0, 120, 0), and (0, 0, 120) into (120, 120, 120) # three of the same value of red, green, and blue
    #(183, 47, 111), (25, 205, 13), and (136, 69, 86) into (183, 205, 86) # all different values of red, green, and blue
    
    # Create three image with four pixels each
    original_red = create_image(4, 1)
    set_color(original_red, 0, 0,  create_color(0, 0, 0))
    set_color(original_red, 1, 0,  create_color(0, 255, 255))
    set_color(original_red, 2, 0,  create_color(120, 0, 0))
    set_color(original_red, 3, 0,  create_color(183, 47, 111))
    
    original_green = create_image(4, 1)
    set_color(original_green, 0, 0,  create_color(0, 0, 0))
    set_color(original_green, 1, 0,  create_color(255, 0, 255))
    set_color(original_green, 2, 0,  create_color(0, 120, 0))
    set_color(original_green, 3, 0,  create_color(25, 205, 13))
    
    original_blue = create_image(4, 1)
    set_color(original_blue, 0, 0,  create_color(0, 0, 0))
    set_color(original_blue, 1, 0,  create_color(255, 255, 0))
    set_color(original_blue, 2, 0,  create_color(0, 0, 120))
    set_color(original_blue, 3, 0,  create_color(136, 69, 86))
    
    # Create an image identical to the one that the function should produce  
    expected = create_image(4, 1)
    set_color(expected, 0, 0, create_color(0, 0, 0))
    set_color(expected, 1, 0, create_color(0, 0, 0))
    set_color(expected, 2, 0, create_color(120, 120, 120))
    set_color(expected, 3, 0, create_color(183, 205, 86))
    
    # Compare the output of the combine function to the expected image one pixel at a time
    combined_image = combine(original_red, original_green, original_blue)
    for x, y, col in combined_image: 
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))   

def test_three_tone():
    """
    Muneer Bhola 101117746
    A test fuction for the three tone filter
    
    >>>test_three_tone()
    """
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    blood = create_color(255,0,0)
    green = create_color(0,255,0)
    blue = create_color(0,0,255)
    lemon = create_color(255,255,0)
    aqua = create_color(0,255,255)
    pink = create_color(255,0,255)
    gray = create_color(128,128,128)
    black = create_color(0,0,0)
    white = create_color(255,255,255)
    color_names = ["black", "white", "blood", "green", "blue", "lemon", "aqua", "pink", "gray"]
    colors = [black, white, blood, green, blue, lemon, aqua, pink, gray]
    col1 = input("Enter color1 to test ")
    col2 = input("Enter color2 to test ")
    col3 = input("Enter color3 to test ")
    
    
    for i in range(len(color_names)):
        if col1 == color_names[i]:
            color1 = colors[i]
        elif col2 == color_names[i]:
            color2 = colors[i]
        elif col3 == color_names[i]:
            color3 = colors[i]
    FILENAME = choose_file()
    original_image = load_image(FILENAME)
    show(original_image)
    image_three_tone = three_tone(original_image,col1,col2,col3)
    show(image_three_tone)
    
    check = 0
    
    for pixels in original_image:
        x, y, (r, g, b) = pixels
        avg = (r + g + b)// 3
        if avg <= 84:
            colortest=color1
            colorimage=get_color(image_three_tone,x,y)
        elif avg <= 170:
            colortest=color2
            colorimage=get_color(image_three_tone,x,y)
        else:
            colortest=color3
            colorimage=get_color(image_three_tone,x,y)
            
        
        if colortest==colorimage:
            check = check
        else:
            check += 1
            
    if check == 0:
        print("PASSED THREE-TONE")
    else:
        print("FAILED THREE-TONE\n" + str(check) + "Pixel(s) failed.")


def test_extreme_contrast()-> None:
    """
    Muneer Bhola (101117746)
    A test function for extreme_contrast
    >>>test_extreme_contrast()
    """
    image = create_image(3, 1)
    set_color(image, 0, 0,  create_color(120, 0, 70))
    set_color(image, 1, 0,  create_color(128, 230, 23))
    set_color(image, 2, 0,  create_color(255, 40, 34)) 

    expected = create_image(3, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(225, 225, 0))
    set_color(expected, 2, 0,  create_color(225, 0, 0))

    extreme_contrast_image = extreme_contrast(image)
    for x, y, col in extreme_contrast_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))

def test_sepia():
    """
    Group 097
    Contributors: Timothy
    March 21st, 2021
    
    A test function for sepia
    >>>test_sepia()
    """
    #This test function checks if combine sucessfully :
    #(0, 0, 0) into (0, 0, 0) # all black
    #(0, 255, 255), (255, 0, 255), and (255, 255, 0) into (0, 0, 0) # different colors than those that should be used
    #(120, 0, 0), (0, 120, 0), and (0, 0, 120) into (120, 120, 120) # three of the same value of red, green, and blue
    #(183, 47, 111), (25, 205, 13), and (136, 69, 86) into (183, 205, 86) # all different values of red, green, and blue
    
    # Create three image with four pixels each    
    original_image = create_image(5,1) 
    set_color(original_image,0,0,create_color(0,0,0))
    set_color(original_image,1,0,create_color(25,90,12))
    set_color(original_image,2,0,create_color(50,100,90))
    set_color(original_image,3,0,create_color(200,210,190))
    set_color(original_image,4,0,create_color(255,255,255))
    
    expected_image = create_image(5,1) 
    set_color(expected_image,0,0,create_color(0,0,0))
    set_color(expected_image,1,0,create_color(46,42,37))
    set_color(expected_image,2,0,create_color(92,80,68))
    set_color(expected_image,3,0,create_color(216,200,186))
    set_color(expected_image,4,0,create_color(255,255,237))    
    
    actual_image = sepia(original_image)
    for x,y,col in actual_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))    

def test_posterize()->None :
    #Junayd DeMone
    #101186381    
    """
    returns passed if correct otherwise returns failed
    >>>test_posterize()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(1, 0) PASSED
    ------
    Checking pixel @(2, 0) PASSED
    ------
    Checking pixel @(3, 0) PASSED
    ------
    """
    original= create_image(4,1)
    set_color(original,0,0,create_color(0,0,0))
    set_color(original,1,0,create_color(51,51,51))
    set_color(original,2,0,create_color(133,133,133))
    set_color(original,3,0,create_color(221,221,221))
    
    expected= create_image(4,1)
    set_color(expected,0,0,create_color(0,0,0))
    set_color(expected,1,0,create_color(0,0,0))
    set_color(expected,2,0,create_color(95,95,95))
    set_color(expected,3,0,create_color(159,159,159))
    
    actual_filtered_image= posterize(original)
    for x,y,col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


def test_edge()->None :
    #Junayd DeMone
    #101186381    
    """
    Returns prints passed if correct otherwise prints failed
    >>>test_edge()
    Checking pixel @(0, 0) PASSED
    ------
    Checking pixel @(0, 1) PASSED
    ------
    Checking pixel @(0, 2) PASSED
    ------
    """
    original= create_image(1,3)
    set_color(original,0,0,create_color(5,5,5))
    set_color(original,0,1,create_color(2,1,3))
    set_color(original,0,2,create_color(124,133,17))

    
    expected= create_image(1,3)
    set_color(expected,0,0,create_color(0,0,0))
    set_color(expected,0,1,create_color(255,255,255))
    set_color(expected,0,2,create_color(255,255,255))

    
    actual_filtered_image= detect_edges(original,1)
    for x,y,col in actual_filtered_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


def test_filter_draw() -> None:
    """
    Muneer Bhola, 101117746
    
    A test fuction for draw_curve
    >>>test_filter_draw()
    """
    original = create_image(9, 1)
    set_color(original, 0, 0,  create_color(123,44,94))
    set_color(original, 1, 0,  create_color(137, 110, 80))
    set_color(original, 2, 0,  create_color(150, 125, 94))
    set_color(original, 3, 0,  create_color(130, 107, 73))
    set_color(original, 4, 0,  create_color(141, 122, 79))
    set_color(original, 5, 0,  create_color(134, 114, 64))
    set_color(original, 6, 0,  create_color(141, 122, 64))
    set_color(original, 7, 0,  create_color(144, 122, 62))
    set_color(original, 8, 0,  create_color(222,169,13))
    
    expected = create_image(9, 1)
    set_color(expected, 0, 0,  create_color(0, 0, 0))
    set_color(expected, 1, 0,  create_color(0, 0, 0))
    set_color(expected, 2, 0,  create_color(0, 0, 0))
    set_color(expected, 3, 0,  create_color(0, 0, 0))
    set_color(expected, 4, 0,  create_color(0, 0, 0))
    set_color(expected, 5, 0,  create_color(0, 0, 0))
    set_color(expected, 6, 0,  create_color(0, 0, 0))
    set_color(expected, 7, 0,  create_color(0, 0, 0))
    set_color(expected, 8, 0,  create_color(0, 0, 0))
    
    filter_draw_image, border = filter_draw(original, "black", [(0,0), (4,20), (7,0)])
    print("testing filter_draw")
    for x, y, col in filter_draw_image:  
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected, x, y))


def test_horizontal():
    """
    Group 097
    Contributors: Timothy (101187187)
    March 27th, 2021
    A test function for the horizontal flip function
    """
    #this function tests if the function sucessfully reverses various pixels across the
    #horizontal direction
    original_image = create_image(5,1) 
    set_color(original_image,0,0,create_color(0,0,0))
    set_color(original_image,1,0,create_color(25,90,12))
    set_color(original_image,2,0,create_color(50,100,90))
    set_color(original_image,3,0,create_color(200,210,190))
    set_color(original_image,4,0,create_color(255,255,255))
    
    expected_image = create_image(5,1) 
    
    set_color(expected_image,0,0,create_color(255,255,255))
    set_color(expected_image,1,0,create_color(200,210,190))
    set_color(expected_image,2,0,create_color(50,100,90))
    set_color(expected_image,3,0,create_color(25,90,12))
    set_color(expected_image,4,0,create_color(0,0,0))
    
    actual_image = flip_horizontal(original_image)
    for x,y,col in actual_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))     

def test_vertical():
    """
    Group 097
    Contributors: Timothy (101187187)
    March 27th, 2021
    A test function for the horizontal flip function
    A test function for the vertical flip function
    """
    #this function tests if the function sucessfully reverses various pixels across the
    #vertical direction    
    original_image = create_image(1,5) 
    set_color(original_image,0,0,create_color(0,0,0))
    set_color(original_image,0,1,create_color(25,90,12))
    set_color(original_image,0,2,create_color(50,100,90))
    set_color(original_image,0,3,create_color(200,210,190))
    set_color(original_image,0,4,create_color(255,255,255))
    
    expected_image = create_image(1,5) 
    
    set_color(expected_image,0,0,create_color(255,255,255))
    set_color(expected_image,0,1,create_color(200,210,190))
    set_color(expected_image,0,2,create_color(50,100,90))
    set_color(expected_image,0,3,create_color(25,90,12))
    set_color(expected_image,0,4,create_color(0,0,0))
    
    actual_image = flip_vertical(original_image)
    for x,y,col in actual_image:
        check_equal('Checking pixel @(' + str(x) + ', ' + str(y) + ')',
                     col, get_color(expected_image, x, y))   

#Main script
test_extreme_contrast()
test_sepia()
test_posterize()
test_edge()
test_filter_draw()
test_horizontal()
test_vertical()
test_three_tone()
test_red_channel()
test_green_channel()
test_blue_channel()
test_combine()