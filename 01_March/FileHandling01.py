try :
    file = open('Testdata.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError as f:
    print(f)
finally:
    file.close()