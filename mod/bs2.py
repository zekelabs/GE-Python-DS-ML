"""
Description about the module :
author :created date

"""
def binary_search(l,key):
    """
    This is bs implementation
    """
    if len(l) ==0:
        return False
    else:    
        mid = len(l) // 2

        if key == l[mid]:
            return True
        elif key < l[mid]:
            return binary_search(l[:mid],key)
        else:
            return binary_search(l[mid+1:],key)

if __name__ =='__main__':
    print("Binary search example")        
    l = [10,20,30,40,50,60,70,80]
    key = 600
    print(binary_search(sorted(l),key))