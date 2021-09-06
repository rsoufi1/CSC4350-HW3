import csv
import math
import time
import tempfile

#1
def FizzBuzz():
    for i in range(1, 101):
        if(i%3 == 0):
            print("Fizz", end="")
            if(i%5==0):
                print("Buzz", end="")
        elif(i%5 == 0):
            print("Buzz", end="")
        else:
            print(i, end="")
        
        print(" ", end="")
    
    print()

#2
def volumeSphere(r):
    volume = 4*math.pi*math.pow(r, 3)/3
    return round(volume, 3)

#3
def toCSV():
    headers = ["Title", "Author", "ISBN13", "Pages"]
    csvData = [["1984", "George Orwell", "978-045154935", "268"],
                ["Animal Farm", "George Orwell", "978-0451526342", "144"],
                ["Brave New World", "Aldous Huxley", "978-0060929879", "288"],
                ]
    
    with open('csv', 'w', encoding='UTF8', newline='') as f:
        #create a new csv writer
        writer = csv.writer(f)

        #write the headers
        writer.writerow(headers)

        for i in range(0, len(csvData)):
            writer.writerow(csvData[i])
    

#4
def toList():
    headers=[]
    csvData=[]
    csvDataRow = []

    with open('csv', mode='r') as f:
        reader = csv.reader(f)
        firstline = True

        for row in reader:
            if firstline:
                firstline = False
                for item in row:
                    headers.append(item)
            else:
                for item in row:
                    csvDataRow.append(item)
                csvData.append(csvDataRow)
                csvDataRow=[]
    
    print("Output:")
    print(headers)
    print(csvData)

#5
def writeAndRead(input):
    file = tempfile.TemporaryFile(mode="w+t")

    for i in range(0, len(input)):
        for j in range(0, len(input[i])):
            file.write(input[i][j])
            if j != len(input[i]) - 1:
                file.write(", ")
        
        if i != len(input) - 1:
            file.write("||")

    #add contents of file to a dict similar to the input
    fileContents = []
    file.seek(0)
    contents = file.read()

    contentsSplitByLine = contents.split("||")

    for i in contentsSplitByLine:
        lineContents = i.split(',')
        fileContents.append(lineContents)
    
    print(fileContents)
    file.close()

print("Testing #1")
startTime = time.time()
FizzBuzz()
endTime = time.time()
print("Total time to run: " + str(round((endTime-startTime), 3)))

print("Testing #2")
print("Volume of a sphere with radius 10: " + str(volumeSphere(10)))
print("Volume of a sphere with radius 5: " + str(volumeSphere(5)))
print("Volume of a sphere with radius 2: " + str(volumeSphere(2)))

print("Testing #3")
toCSV()
print("See file csv")

print("Testing #4")
toList()

print("Testing #5")
data = [["1984", "George Orwell", "978-045154935", "268"],
                ["Animal Farm", "George Orwell", "978-0451526342", "144"],
                ["Brave New World", "Aldous Huxley", "978-0060929879", "288"]
                ]
writeAndRead(data)


print("Complete")