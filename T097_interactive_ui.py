from Cimpl import*
from T097_P4_image_filters import*

user_input = None
image = None 
new_image = None
color1 = ""
color2 = ""
color3 = ""


def interac_three_tone(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "three_tone"
    
    interac_three_tone()
    show(filtered_image)
    """
    #Timothy Kennedy 101187187 (error fix)
    if image != None:
        filtered_image = three_tone(new_image,"aqua","blood","lemon")
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")


def interac_extreme_contrast(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "extreme_contrast"
    
    interac_extreme_contrast()
    show(filtered_image)
    """
    if image != None:
        filtered_image = extreme_contrast(new_image)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")
        

def interac_sepia(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "sepia"
    
    interac_sepia()
    show(filtered_image)
    """
    if image != None:
        filtered_image = sepia(new_image)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")


def interac_posterize(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "posterize"
    
    interac_posterize()
    show(filtered_image)
    """
    if image != None:
        filtered_image = posterize(new_image)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")
        

def interac_detect_edges(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "detect_edges"
    
    interac_detect_edges()
    show(filtered_image)
    """
    if image != None:
        threshold = int(input("Enter threshold value: "))
        filtered_image = detect_edges(new_image, threshold)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")


def interac_flip_vertical(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "flip_vertical"
    
    interac_flip_vertical()
    show(filtered_image)
    """
    if image != None:
        filtered_image = flip_vertical(new_image)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")     
        
        
def interac_flip_horizontal(new_image:Image) -> Image:
    """
    Muneer Bhola 101117746
    A user interactive function to operate "flip_horizontal"
    
    interac_flip_horizontal()
    show(filtered_image)
    """
    if image != None:
        filtered_image = flip_horizontal(new_image)
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")   

def interac_filter_draw(new_image:Image) -> Image:
    """
    Timothy Kennedy 101187187
    A function to interact with filter_draw
    """
    if image != None:
        filtered_image,border = filter_draw(new_image,"lemon")
        show(filtered_image)
        return filtered_image
    else:
        print("No image loaded")   

while user_input != False:
    """
    Muneer Bhola 101117746
    A while loop, to recognize user input and configure it with filters
    """
    user_input = input("L)oad image   S)ave-as \n3)-tone   X)treme contrast   T)int sepia   "+
    "P)osterize \nE)dge detect   V)ertical filp   H)orizontal filp \nD)raw curve\nQ)uit \n\n: ")
    
    if user_input == "Q" or user_input == "q":
        user_input = False
        
    elif user_input == 'L' or user_input == 'l':
        image = load_image(choose_file())
        new_image = copy(image)
    
    elif user_input =='S' or user_input == 's':
        save_as()
    elif user_input == '3':
        new_image = interac_three_tone(new_image)
        
    elif user_input == 'X' or user_input == 'x': 
        new_image = interac_extreme_contrast(new_image)
        
    elif user_input == 'T' or user_input == 't': 
        new_image = interac_sepia(new_image)
        
    elif user_input == 'P' or user_input == 'p':
        new_image = interac_posterize(new_image)
        
    elif user_input == 'E' or user_input == 'e':
        new_image = interac_detect_edges(new_image)
        
    elif user_input == 'V' or user_input == 'v':
        new_image = interac_flip_vertical(new_image)
        
    elif user_input == 'H' or user_input == 'h':
        new_image = interac_flip_horizontal(new_image)
    elif user_input == 'D' or user_input == 'd':
        new_image = interac_filter_draw(new_image)
        show(new_image)
    else:
        print("No such command")