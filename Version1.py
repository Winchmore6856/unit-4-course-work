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

# FIX: added error handling
try:
    with open('HotDogs.txt', "r") as file:
        for line in file:
            if search_query in line:
                parts = line.strip().split(",")
                
                # FIX: basic validation of row length
                if len(parts) >= 4:
                    Hotdog_data.append(parts)
except FileNotFoundError:
    print("Error: file not found")
    Hotdog_data = []

time.sleep(1)
print("1. VendorID\n2. Vendor Name\n3. Year & Week\n4. Vegan Holding Quality\n5. Meat Holding Quality\n6. Onions (kg)\n7. Ketchup (l)")
time.sleep(1)
print("     1           2           3       4     5       6      7")

for i in Hotdog_data:
    print(i)

# FIX: removed duplicate print loop


#linear searches
def linear_search(items, target):
    for i in range(len(items)):
        if items[i] == target:
            print(f"Found {target} at position {i + 1}")
            return True 
    # FIX: moved outside loop
    print(f"{target} not found")
    return False 


#linear search UNSORTED FIXED 
def linear_search_unsorted(data, target):
    for item in data:
        if item[1] == target:
            return True
    return False 

#linear search SORTED FIXED 
def linear_search_sorted(data, target):
    for item in data:
        if item[1] == target:
            return True
    return False 

#binary search
def binary_search(items, target):
    first = 0
    last = len(items) - 1
    passes = 0

    while first <= last:
        passes += 1
        midpoint = (first + last) // 2 

        if items[midpoint][1] == target:
            print(f"Found {target} after {passes} passes")
            return True
        
        if items[midpoint][1] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return False



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

if linear_search_unsorted(Hotdog_data, search_query):
    print("Linear search (unsorted): Found")
else:
    print("Linear search (unsorted): Not Found")

sorted_data = bubble_sort(Hotdog_data.copy())

if linear_search_sorted(sorted_data, search_query):
    print("Linear search (sorted): Found")
else:
    print("Linear search (sorted): Not found")

if binary_search(sorted_data, search_query):
    print("Binary search: Found")
else:
    print("Binary search: Not found")


#Call SORT functions
print("\n--- Sort Results ---")

bubble_sorted = bubble_sort(Hotdog_data.copy())
print("Bubble sorted data:")
for item in bubble_sorted:
    print(item)

quick_sorted = quick_sort(Hotdog_data.copy())
print("\nQuick sorted data:")
for item in quick_sorted:
    print(item)


#TIMING SEARCHES 

start = time.time()
linear_search_unsorted(Hotdog_data, search_query)
unsorted_time = time.time() - start

sorted_data =  bubble_sort(Hotdog_data.copy())

# FIX: used sorted_data correctly
start = time.time()
linear_search_sorted(sorted_data, search_query)
sorted_time = time.time() - start

start = time.time()
binary_search(sorted_data, search_query)
binary_time = time.time() - start


#TIMING SORTS 

start = time.time()
bubble_sort(Hotdog_data.copy())
bubble_time = time.time() - start

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

# FIX: corrected indentation + added safe conversion
for item in Hotdog_data:
    try:
        vendor = item[0]
        type_ = item[1]
        quantity = int(item[2])
        ketchup = int(item[3])
    except (IndexError, ValueError):
        continue

    if vendor not in total_per_vendor:
        total_per_vendor[vendor] = 0
    total_per_vendor[vendor] += quantity 

    if type_.lower() == "vegan":
        vegan += quantity 
    else:
        meat += quantity 

    if ketchup < least_ketchup:
        least_ketchup = ketchup
        least_vendor = vendor

# FIX: avoid crash if empty
if total_per_vendor:
    most_productive = max(total_per_vendor, key=total_per_vendor.get)
else:
    most_productive = "N/A"

print("\n--- ANALYSIS ---")
print("Most productive vendor:", most_productive)
print("Vegan hotdogs:", vegan)
print("Meat hotdogs:", meat)
print("Least ketchup used by:", least_vendor)
