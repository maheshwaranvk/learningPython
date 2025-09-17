class ShoppingList:
    with open("./week3/classroom/txtFiles/shoppingList.txt", "a") as f:
        f.write("\nNewsPaper - 20")
        f.write("\nVegetables - 200")
    number=[]
    with open("./week3/classroom/txtFiles/shoppingList.txt", "r") as f:
        print(f.read())
        f.seek(0) #sets pointer to begining of the file again
        for line in f:
            for word in line.split():
                if (word.isdigit()):
                    number.append(int(word))
    print("Total Shopping cost : Rs.", sum(number))