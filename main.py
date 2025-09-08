

#Author: Usman Shahid


import math 

print("==================Area Calculator 📐==================")
print("1) Triangle\n2) Rectangle\n3) Square\n4) Circle\n5) Quit \n")
user_input = int (input('Which shape: '))

if user_input== 1:
    sides_ofSquare = int(input('\nSide: '))
    Square = sides_ofSquare * sides_ofSquare
    print("\nThe area is: ",Square)

elif user_input == 2:
    length_ofRectangle = int (input('\nLength: '))
    Width_ofRectangle = int (input ('\nWidth: '))
    Rectangle = length_ofRectangle * Width_ofRectangle 
    print("\nThe area is: ",Rectangle)

elif user_input == 3:
    height_ofTriangle = int (input('\nHeight: '))
    base_ofTriangle = int (input ('\nBase: '))
    Triangle = (height_ofTriangle * base_ofTriangle)/2
    print("\nThe area is: ",Triangle)

elif user_input == 4:
    radius = int (input('\nRadius: \n'))
    circle = math.pi * (radius * radius)
    print("\nThe area is: ",circle)

elif user_input==5:
    print("\nQuitting... ")

else:
    print("Error...")