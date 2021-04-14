from Cimpl import*
from T097_P4_image_filters import*

#Timothy Kennedy 101187187


batch_file_name = input("Filename of batch file: ") #get filename
batch_file = open(batch_file_name)

lines = batch_file.read().split("\n") #splits file into seperate lines
for i in range(len(lines)):
    lines[i] = lines[i].split(" ") #splits lines into spaces (individual commands)

for i in range(len(lines)):
    
    original_image = load_image(lines[i][0]) #loads image coresponding to the first entry of the line
    new_image = copy(original_image) #creates a copy to be output at the end of the line
    
    for j in range(len(lines[i])-2):#for each command after the original image and the desired save name,
                                    #perform the operation corresponding to the command
        
        if(lines[i][j+2] == "3"):
            new_image = three_tone(new_image,"aqua","blood","lemon")
            
        elif(lines[i][j+2] == "X" or lines[i][j+2] == "x"):
            new_image = extreme_contrast(new_image)
            
        elif(lines[i][j+2] == "T" or lines[i][j+2] == "t"):
            new_image = sepia(new_image)
            
        elif(lines[i][j+2] == "P" or lines[i][j+2] == "p"):
            new_image = posterize(new_image)
            
        elif(lines[i][j+2] == "E" or lines[i][j+2] == "e"):
            new_image = detect_edges(new_image, 15)
            
        elif(lines[i][j+2] == "V" or lines[i][j+2] == "v"):
            new_image = flip_vertical(new_image)
            
        elif(lines[i][j+2] == "H" or lines[i][j+2] == "h"):
            new_image = flip_horizontal(new_image)
            
        
    save_as(new_image,lines[i][1]) #save the image with the desired save name
    
    