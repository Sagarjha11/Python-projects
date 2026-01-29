try :
    with open("Sample.txt" , "rt") as fh:
        content = fh.read()
        print(content)
except FileNotFoundError:
    print("The file sample.txt was not found")
