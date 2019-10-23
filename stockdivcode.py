print("Which Stock Are You considering Purchasing?")
print(" ")

#Stock names
print("Enter First Stock: ")
stock1 = input()

#Enter data for first stock
print("What is the", stock1, "market price?")
markprice1 = float(input())
print("How many shares of", stock1, "are you planning on purchasing?")
shares1 = float(input())
print("For how many years do you plan to hold the", stock1, "stock?")
year1 = float(input())
print("What is the quarterly dividend for a share of", stock1,"?")
div1 =float(input())

#Quarter Data Type
quarter = int(4) 

#Perform cost calculations for first stock
def multiply(shares1, markprice1):
    return shares1 * markprice1
print("You will pay $", multiply(shares1, markprice1),"for", stock1, "stock")

#Perform dividend calculations
def multply(shares1, div1, year1, quarter):
    return shares1 * div1 * year1 * quarter
print("You will get $", multply(shares1, div1, year1, quarter),"in dividends for the time \
you plan on holding the", stock1, "stock")
