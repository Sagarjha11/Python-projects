input_text = str(input("Enter text to write to the file : "))

with open("output.txt","wt") as fh:
    file = fh.write(input_text)
    fh.write("\n")
    print("Data successfully written to output.txt")

text = str(input("Enter additional text to append : "))
with open("output.txt","at") as app:
    new = app.write(text)
    print("Data successfully appended.")
with open("output.txt","rt") as final:
    read = final.read()
    print("final Content of the output.txt ")
    print(read)