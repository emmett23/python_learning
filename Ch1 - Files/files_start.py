#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # myfile = open("textfile.txt", "w+") #creates a new file, w+
    
    # Open the file for appending text to the end
    # f = open("textfile.txt", "a+")

    # # write some lines of data to the file
    # for i in range(1,10):
    #     f.write("This is some new text \n")
    
    # # close the file when done
    # f.close()
    
    # Open the file back up and read the contents

    my_file = open("textfile.txt", "r")

    if my_file.mode == "r":
        # contents = my_file.read()
        # print(contents)
        readlines = my_file.readlines()

        for line in readlines:
            print(line)
if __name__ == "__main__":
    main()
