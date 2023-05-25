if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    #  Removing duplicates from the list
    new_arr = list(set(arr))
    
    # Sorting the list
    new_arr.sort()
    
    # Printing the the second last element
    print(new_arr[-2])
    
    