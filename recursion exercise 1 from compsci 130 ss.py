def count_down(num):
    if num == 0:
        print("Go!")
    else:
        print(num)
        count_down(num-1)
        
count_down(3)
count_down(5)
