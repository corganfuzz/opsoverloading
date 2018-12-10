import os.path


def main():

    if os.path.isfile("Presidents.txt"):
        print("presidents already exist")
    else:
        outFile = open('Presidents.txt', 'w')

        # write data to the file
        outFile.write("Bill Clinton\n")
        outFile.write("Georgie\n")
        outFile.write("Obama yo mama\n")
        outFile.close()


main()
