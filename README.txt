Email: timothykennedy@cmail.carleton.ca
Website: https://github.com/trk20/Aperture-Image-Editor
-------------------------------------------------------
Wednesday, April 14th, 2021

Aperture Image Editor version 4.2

Aperture Image Editor is an image processing program built on the Cimpl library in Python that enables several image editing tools in both an interactive UI format and a batch format.
-------------------------------------------------------

Installation
------------------------------------------------------                                                                                                                                  
Program Requires the Installation of 
(1) Python, (python 3.7.4 or later version is recommended),   
(2) Wing 101/PythonIDE (Most recent version)                                                                                                        
(3) Update Command prompt by installing “pip”                                                                                                 
(4) Update Command prompt to “numpy” as well (1.19.5 or later works)                                                      
(5) Have “Cimpl”, “simple_cimpl_filter”, and “point_manipution” downloaded in the same folder as this software program 
(6) When running the main program have  “T097_P4_image_filters.py”,  “T097_P4_test_image_filters.py”, “T097_interactive_ui.py”, and “T097_batch_ui.py”  all in the same folder as well.
-------------------------------------------------------
Usage:
After you've installed the projects you're ready to use them. The first project file is the images_filters. The filters in this file are red_channel(), green_channel(), blue_channel(), three_tone(), extreme(), sepia(), posterize(), edge(),draw(),vertical() and horizontal(). Below you can see how you can call these filters.

>>>red_channel(load_image(‘p2-original.png’))

>>>green_channel(load_image(‘p2-original.png’))

>>>blue_channel(load_image(‘p2-original.png’))

>>>three_tone(load_image(‘p2-original.png’), ‘black’,’white’,’green’)

>>>extreme(load_image(‘p2-original.png’))

>>>sepia(load_image(‘p2-original.png’))

>>>posterize(load_image(‘p2-original.png’))

>>>edge(load_image(‘p2-original.png’),1)

>>>draw(load_image(‘p2-original.png’),’black’)

>>>vertical(load_image(‘p2-original.png’))

>>>horizontal(load_image(‘p2-original.png’))

The next project file is the text-based interactive user interface. This file allowed us to call the above function by inputting a specific letter or number. The list of inputs are

‘L’ or ‘l’ - copies image

‘S’ or ‘s’ -  save as

‘3’- applies three tone filter

‘X’ or ‘x’ - applies extreme contrast filter

‘T’ or ‘t’ - applies sepia tint filter

‘P’ or ‘p’ - applies posterize filter

‘E’ or ‘e’ - applies detect edge filter

‘V’ or ‘v’ - applies flip vertical filter

‘H’ or ‘h’ - applies flip horizontal filter

‘D’ or ‘d’- applies draw line filter


The final Project file is the file-based batch user interface. This file allows us to manipulate an image by using the text-based interactive user interface inputs and then save the manipulated image as a new photo. Some examples of this are as follows.

>>>P2-original.png new_image 3 v T

‘P2-original.png’ is the image we are going to manipulate

‘New_image’ is the name that the manipulated image will be saved as 

‘3 v T’  are the filters that will be applied to the original image in this case three tone, flip vertical and sepia tint will be applied to the image.

-------------------------------------------------------
Credits:
-In this project Junayd as a team member did the blue channel, test blue channel, sepia tint, test posterize, flip vertical, flip horizontal and test edge detection. For the project report he did the project process and for the README file he did usage.
-In this project Muneer as a team member contributed by the red filter, test red filter, organization/problem statement & referencing of project report, three tone, test extreme contrast, edge detect, test draw curve, interactive_ui, organization/installation in README.txt and calling/organizing of meetings.
-In this project Tim as the group leader took responsibilities relating the summation/gathering of files and their submission on culearn, the batch UI, several tweaks and bug/error fixes in various places, the image filters for posterize and curve drawing, the tests for the sepia, vertical flip, and horizontal flip filters, and the refactoring of the image filters and tests.
-------------------------------------------------------
License:
Cimpl Image Editing Software
Copyright (C) 2021 Aperture Science

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
-------------------------------------------------------