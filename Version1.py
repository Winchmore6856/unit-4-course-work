#vendor list
import time
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

time.sleep(1)
print("1. VendorID\n2. Vendor Name\n3. Year & Week\n4. Vegan Holding Quality\n5. Meat Holding Quality\n6. Onions (kg)\n7. Ketchup (l)")
time.sleep(1)
print("     1           2           3       4     5       6      7")
for i in Hotdog_data:
    print(i)

for i in Hotdog_data:
    print(i)
#linear searches
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            print(f"Found {target} at position {i + 1}")
            return True 
        print(f"{target} not found")
        return False 

#linear search UNSORTED 
def linear_search_unsorted(data, target):
    for item in data:
        if item[0] == target:
            return True
    return False 

#linear search SORTED 
def linear_search_sorted(data, target):
    for item in data:
        if item[0] == target:
            return True
    return False 

#binary search
def binary_search(items, target):
    first = 0
    last = len(items) - 1
    passes = 0

    while first <= last:
        passes += 1  # Added to track search attempts
        midpoint = (first + last) // 2 

        # Indent the if block to be inside the while loop
        if items[midpoint][0] == target:
            print(f"Found {target} after {passes} passes")
            return True
        
        # Standard binary search logic to update range
        if items[midpoint][0] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

            
    return False # Return False if the loop ends and target isn't found



#bubble sort 
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][0] > data[j + 1][0]:
                data[j], data[j+1] = data[j+1], data[j]
    return data 

#quick sort
def quick_sort(data):

    if len(data) <=1:
        return data

    pivot = data[0]
    left = []
    right = []

    for item in data[1:]:
        if item[0] <= pivot[0]:
            left.append(item)
        else:
            right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)

#Call SEARCH functions 
print("\n--- Search Results ---")

#Linear unsorted 
if linear_search_unsorted(Hotdog_data, search_query):
    print("Linear search (unsorted): Found")
else:
    print("Linear search (unsorted): Not Found")

#Sort data first 
sorted_data = bubble_sort(Hotdog_data.copy())

#Linear sorted 
if linear_search_sorted(sorted_data, search_query):
    print("Linear search (sorted): Found")
else:
    print("Linear search (sorted): Not found")

#Binary search
if binary_search(sorted_data, search_query):
    print("Binary search: Found")
else:
    print("Binary search: Not found")

#Call SORT functions
print("\n--- Sort Results ---")

#Bubble sort
bubble_sorted = bubble_sort(Hotdog_data.copy())
print("Bubble sorted data:")
for item in bubble_sorted:
    print(item)

#Quick sort
quick_sorted = quick_sort(Hotdog_data.copy())
print("\nQuick soted data:")
for item in quick_sorted:
    print(item)
#TIMING SEARCHES 


#linear unsorted 
start = time.time()
linear_search_unsorted(Hotdog_data, search_query)
unsorted_time = time.time() - start

#sort first
sorted_data =  bubble_sort(Hotdog_data.copy())

#linear sorted 
start = time.time()
linear_search_sorted(Hotdog_data, search_query)
sorted_time = time.time() - start

#binary Search 
start = time.time()
binary_search(Hotdog_data, search_query)
binary_time = time.time() - start

#TIMING SORTS 

#bubble sort
start = time.time()
bubble_sort(Hotdog_data.copy())
bubble_time = time.time() - start

#quick sort
start = time.time()
quick_sort(Hotdog_data.copy())
quick_time = time.time() - start

print("\n--- TIMINGS ---")
print("linear unsorted:",unsorted_time)
print("linear sorted:",sorted_time)
print("binary search:",binary_time)
print("bubble sort:",bubble_time)
print("quick sort:",quick_time)
#Analysis

total_per_vendor = {}
vegan = 0
meat = 0
least_ketchup = float("inf")
least_vendor = ""

for item in Hotdog_data:
    vendor = item[0]
    type_ = item[1]
    quantity = int(item[2])
    ketchup = int(item[3])

#total per vendor 
if vendor not in total_per_vendor:
    total_per_vendor[vendor] = 0
total_per_vendor[vendor] += quantity 

#vegan vs meat
if type_.lower() == "vegan":
    vegan += quantity 
else:
    meat += quantity 

#least ketchup 
if ketchup < least_ketchup:
    least_ketchup = ketchup
    least_vendor = vendor

most_productive = max(total_per_vendor, key=total_per_vendor.get)

print("\n--- ANALYSIS ---")
print("Most productive vendor:", most_productive)
print("Vegan hotdogs:", vegan)
print("Meat hotdogs:", meat)
print("Least ketchup used by:", least_vendor)
