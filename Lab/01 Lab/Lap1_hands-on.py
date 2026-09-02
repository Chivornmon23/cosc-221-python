try: 
    myFile = open("task1.txt", "r")
    fileContent = myFile.read()
    print(fileContent)
    # print(open("tasks1.txt", "r").read())
    myFile.close()
except FileNotFoundError:
    print("file is not found")
except ValueError:
    print("Data is not a valid integer")
finally: 
    print("End of Program")


# task 5
import pickle

#Writing binary data to file
outfile = open("sample_data.pkl", "wb")
pickle.dump([1, 2, 3, 4, 5], outfile)
outfile.close
