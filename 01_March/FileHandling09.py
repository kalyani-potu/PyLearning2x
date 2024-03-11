with open("Testdata.txt", 'w') as file: # w mode creates a new file and writes the data, if file exists , then it truncates and writes the data new data
    file.write("Hello Krithi, How are you ?")
file.close()