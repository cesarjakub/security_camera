#imports here


#code here 

list = [1,2,6,4,8,5]

def number_loop(obj):
    for x in obj:
        print(x, end=" ")

def sorted_loop(obj):
    obj = sorted(obj)
    for x in obj:
        print(x, end=" ")


number_loop(list)
print()
sorted_loop(list)
