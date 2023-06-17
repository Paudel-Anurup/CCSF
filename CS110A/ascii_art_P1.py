
'''
Inputs : None
Outputs : A dog looking from a telescope as he talks with his hooman.
Date : 06/16/2023
'''

# Creates a text file with write attribute.
file = open("Ascii.txt", 'w')

# Writes the following on the text file.
file.write("A dog trying to look through a telescope.\n")
file.write("     .-.                  \n")                               
file.write("    {}``; (|=======|      \n")                            
file.write("    / ('    / | \         \n")                              
file.write("(  /  |    /  |  \        \n")                             
file.write(" \(_)_]]  /   |   \       \n")
file.write("Why cant I see a thing hooman? " + "Please human help me I would like to see the stars.") #Use of string concatenation 
file.write("\nFooled you Doggo I closed the eye piece.") 
# closes the file
file.close()

# open the text file with a read attribute
file = open("Ascii.txt", 'r')

#Assigning a variable to read the text file so we can print it, on the console. 
text = file.read()
print(text)
# close the text file
file.close()

'''
This activity was to get familiar with python on how to create an Ascii art and external file using python
It is a simple program but helps us understand how to create steps to get desired output.
'''