# Print a specific pattren through python
user = int(input("input rows: "))


for i in range(1,user):
    # print("%")
    for j in range(i,user + 1):
        print("*" , end= " ")
    print()    