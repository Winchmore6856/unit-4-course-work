#vendor list
avaliable_vendors = ["Dolly Dogs", "Korner Kart"]

#loop for valid input
while True:
    search_query = input ("enter vendor name (2-25 chars): ")

    #length check
    if len(search_query) < 2 or len(search_query) > 25:
        print("name must be between 2 and 25 characters")
        continue

    #check if vendor exists
    if search_query not in avaliable_vendors:
        print("vendor not found")
        continue
    break

#read text file + store matches
Hotdog_data = []

with open('HotDogs.txt', "r") as file:
    for line in file:
        #checking if vendor appears in line
        if search_query in line:
            parts = line.strip().split(",")
            Hotdog_data.append(parts)

#linear searches
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            print(f"Found {target} at position {i + 1}")
            return
        print(f"{target} not found")

#binary search(fixed)
def binary_search(items, target):
    first = 0
    last = len(items) - 1
    passes = 0

    while first <= last:
        midpoint 
