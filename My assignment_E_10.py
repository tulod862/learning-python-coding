#def does_it_contain(arr, element):
#    return element in arr

#a = [1, 2, 3, 4, 5]
#print(does_it_contain(a, 3)) 
  
#print(does_it_contain(a, 6))
      



      
#def does_it_contain_duplicates(arr):
   
#    return len(arr) != len(set(arr)) 

#a = [1, 2, 3, 4, 5]
#print(does_it_contain_duplicates(a)) 

#b = [1, 2, 3, 4, 5, 3]
#print(does_it_contain_duplicates(b))  


def does_it_contain(arr, element):
    for item in arr:
        if item == element:
            return True
    return False

a = [1, 2, 3, 4, 5]
print(does_it_contain(a, 3)) 
print(does_it_contain(a, 6))




#def does_it_contain_duplicates(arr):
#    for i in range(len(arr)):
#        for j in range(i + 1, len(arr)):
#            if arr[i] == arr[j]:
#                return True
#    return False

def does_it_contain_duplicates(arr):
    seen = set()
    for item in arr:
        if item in seen:
            return True
        seen.add(item)
    return False

a = [1, 2, 3, 4, 5]
print(does_it_contain_duplicates(a))

b = [1, 2, 3, 4, 5, 3]
print(does_it_contain_duplicates(b)) 