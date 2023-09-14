#!/usr/bin/env python

# system include files
#
import sys
import os
import numpy as np


# funciton that check to see if the -help command was added
#
def help(argv):
     # for loop that run through all the given argument 
     #
     for i in  sys.argv:

          # look for any argument that contain the help
          #
          if i.lower() == "-help":

               # open the text file for the help command 
               #
               with open("help.txt","r") as fp:

                    # print everything out in the file
                    # .read() is being use to read the file pointer
                    #
                    print(fp.read())
                    exit()
               # end of the with open
          # end of the if statment
     # end of the for loop
# check to see if the file being ope exist
#
def check_file(argv):
     
     # for loop to loop through the file name 
     #
     for i in  sys.argv[2:]:

          # if statement to check if the file exist
          #
          if os.path.isfile(i) != True:
               print("The file " + i +" do not exist")
               exit()
          # end of if statement
     #end of the for loop

# main: this is the main function of this Python
#
# int main(int argc, char** argv)
#
def main(argv):

     # call a function to look for the help command
     #
     help(argv)

     # checking the file to se if they exist 
     #
     check_file(argv)
     
     # num is a int that count the number of lines that begin read
     #
     num = 0

     # count how make time the word is found
     #
     time =0
     
     # for loop that run to get the file name
     # sys.argv is the argument given in the command line
     # [#:] is use as starting point for the loop [1:] is for
     # the second argument 
     #
     for i in  sys.argv[2:]:
       
          # open the file and asign it as a file pointer
          #
          with open(i) as search_file:

               # loop through the file (search_file) line by line
               #
               for line in search_file:
                    num = num + 1
                    # loop through a line string by string
                    #
                    for string in line.split():

                         # look for a string that was given in the command line
                         #
                         if argv[1].lower() == string.lower(): 
                              
                              # print out text file
                              #
                              print("file: " + i) 
                              print ("line", num,  ": " + line)
                              time = 1 + time
                         #  end of if statement
                    # end of loop
               # end of loop
          # with close file
     # end of the loop

     # print out the numeber of matches
     #
     print("lines matched = ",time)
#
# end of main

# begin gracefully
#
if __name__ == "__main__":
    main(sys.argv)

#
# end of file
