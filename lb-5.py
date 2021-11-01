filePath = "studentList.txt"

while True:

    print("0. Вихід з програми\n1. Друк списка\n2. Доповнити список\n3. Друк рядка...\n4. Пошук за фамілією або балом\n")

    userInput = str(input())

    if userInput == "0":
        break


    elif userInput == "1":

        file1 = open(filePath, "r")
        file2 = file1.readlines()

        for line in file2:
            print(line)


    elif userInput == "2":

        print("Введіть доповнення")
        newData = (str(input()) + "\n")

        file1 = open(filePath, "a+")
        file1.write(newData)
        file1.close()

        print("Дані додано\n")


    elif userInput == "3":

        print("Який рядок друкувати?")
        row1 = int(input())

        line = open(filePath).readlines()[row1]
        print(line)



    elif userInput == "4":

        print("Введіть фамілію або бал")
        searchInput = str(input())

        file1 = open(filePath, "r")
        file2 = file1.readlines()

        for row in file2:
            if searchInput in row:
                print(row)


    else:
        print("Виберіть щось з списку")