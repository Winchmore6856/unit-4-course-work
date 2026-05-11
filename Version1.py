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

# IMPROVEMENT: Function to display data as a clean table
def display_table(data_list, title):
    print(f"\n--- {title} ---")
    header = "ID    Name           Year/Wk    Vegan   Meat    Onion   Ketchup"
    print(header)
    print("-" * len(header))
    for row in data_list:
        # Formats each column to be aligned
        print(f"{row[0]:<5} {row[1]:<14} {row[2]:<10} {row[3]:<7} {row[4]:<7} {row[5]:<7} {row[6]}")

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

#linear searches
def linear_search(items, target, verbose=True):
    found_items = []
    for i in range(len(items)):
        if items[i][1] == target:
            if verbose: print(f"Found {target} at position {i + 1}")
            found_items.append(items[i])
    
    if found_items:
        if verbose: display_table(found_items, "Linear Search Results") 
        return True
    if verbose: print(f"{target} not found")
    return False 

#linear search UNSORTED 
def linear_search_unsorted(data, target, verbose=True):
    results = []
    for item in data:
        if item[1] == target: 
            results.append(item)
    if results:
        if verbose: display_table(results, "Linear Unsorted Table") 
        return True
    return False 

#linear search SORTED 
def linear_search_sorted(data, target, verbose=True):
    results = []
    for item in data:
        if item[1] == target:   
            results.append(item)
    if results:
        if verbose: display_table(results, "Linear Sorted Table") 
        return True
    return False 

#binary search
def binary_search(items, target, verbose=True):
    first = 0
    last = len(items) - 1
    passes = 0
    results = []

    while first <= last:
        passes += 1  
        midpoint = (first + last) // 2 

        if items[midpoint][1] == target:  
            if verbose: 
                print(f"Found {target} after {passes} passes")
                results.append(items[midpoint])
                display_table(results, "Binary Search Table") 
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

#Linear unsorted 
if linear_search_unsorted(Hotdog_data, search_query, verbose=True):
    print("Linear search (unsorted): Found")
else:
    print("Linear search (unsorted): Not Found")

#Sort data first 
sorted_data = bubble_sort(Hotdog_data.copy())

#Linear sorted 
if linear_search_sorted(sorted_data, search_query, verbose=True):
    print("Linear search (sorted): Found")
else:
    print("Linear search (sorted): Not found")

#Binary search
if binary_search(sorted_data, search_query, verbose=True):
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
print("\nQuick sorted data:")
for item in quick_sorted:
    print(item)

#TIMING SEARCHES (linear and binary search tables could be shown twice now it wont)

#linear unsorted 
start = time.time()
linear_search_unsorted(Hotdog_data, search_query, verbose=False)
unsorted_time = time.time() - start

#sort first
sorted_data =  bubble_sort(Hotdog_data.copy())

#linear sorted 
start = time.time()
linear_search_sorted(sorted_data, search_query, verbose=False)
sorted_time = time.time() - start

#binary Search 
start = time.time()
binary_search(sorted_data, search_query, verbose=False)
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
print("linear unsorted:",(unsorted_time * 1000000))
print("linear sorted:",(sorted_time * 1000000))
print("binary search:",(binary_time * 1000000))
print("bubble sort:",(bubble_time * 1000000))
print("quick sort:",(quick_time * 1000000))

#Analysis
total_per_vendor = {}
vegan = 0
meat = 0
least_ketchup = float("inf")
least_vendor = ""

# FIXED: Indented the analysis logic so it runs for every item
for item in Hotdog_data:
    vendor = item[1]
    type_ = item[2]
    quantity_vegan = int(item[3])
    quantity_meat = int(item[4])
    ketchup = int(item[6])

    #total per vendor 
    if vendor not in total_per_vendor:
        total_per_vendor[vendor] = 0
    total_per_vendor[vendor] += (quantity_vegan + quantity_meat)

    #vegan vs meat
    vegan += quantity_vegan
    meat += quantity_meat

    #least ketchup 
    if ketchup < least_ketchup:
        least_ketchup = ketchup
        least_vendor = vendor

if total_per_vendor:
    most_productive = max(total_per_vendor, key=total_per_vendor.get)
else:
    most_productive = "None"

print("\n--- ANALYSIS ---")
print("Most productive vendor:", most_productive)
print("Total Vegan hotdogs sold by this vendor:", vegan)
print("Total Meat hotdogs sold by this vendor:", meat)
print("Least ketchup used by this vendor in a single week:", least_vendor)

 #Save Results to File 

results = f"""
Most productive vendor: {most_productive}
Total vegan hotdogs: {vegan}
total meat hotdogs: {meat}
Vendor using least ketchup: {least['name']}
"""

save_results("analysis.txt", result)
