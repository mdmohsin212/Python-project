import csv

fh = open("inventoryforFruitsitem.csv", "w+", newline="")
w = csv.writer(fh)

header = ["Fruits Name", "Unit Price", "Quantity", "Total Price"]
w.writerow(header)

data = []

while True:
    try:
        n = int(input("How many fruits records do you want to insert? "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    else:
        break

for i in range(n):
    fruitsname = input("Enter Fruit Name: ")
    
    while True:
        try:
            unitprice = float(input("Enter Unit Price: "))
        except ValueError:
            print("Please enter a valid unit price.")
            continue
        else:
            break
    
    while True:
        try:
            quantity = int(input("Enter Quantity: "))
        except ValueError:
            print("Please enter a valid quantity.")
            continue
        else:
            break
    
    totalprice = unitprice * quantity
    rec = [fruitsname, unitprice, quantity, totalprice]
    data.append(rec)

w.writerows(data)
fh.close()

print("Printing fruits items summary data from stored CSV file")
fh = open("inventoryforFruitsitem.csv", "r")
r = csv.reader(fh)

for row in r:
    print(row)

fh.close()
