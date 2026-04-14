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

#TIMING SEARCHES 
import time

#linear unsorted 
start = time.time()
linear_search_unsorted(Hotdog_data, search_querry)
unsorted_time = time.time() - start 

#sort first
sorted_data =  bubble_sort(Hotdog_data.copy())

#linear sorted 
start = time.time()
linear_search_sorted(Hotdog_data, search_querry)
sorted_time = time.time() - start 

#binary 
start = time.time()
binary_search(Hotdog_data, search_querry)
binary_time = time.time() - start

#TIMING SORTS 
start = time.time()
bubble(Hotdog_data.copy())
bubble_time = time.time() - start 
