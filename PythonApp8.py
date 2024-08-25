amount = int(input("Минимальная сумма инвестиций: "));

balance_mike = int(input("Cколько долларов вложит Майкл: "));

balance_ivan = int(input("Сколько долларов вложит Иван: "));

if (balance_mike >= amount) and (balance_ivan >= amount):
    print(2);

elif (balance_mike >= amount) and (balance_ivan <= amount):
    print("Mike");

elif (balance_mike <= amount) and (balance_ivan >= amount):
    print("Ivan");

elif (balance_mike <= amount) and (balance_ivan <= amount) and ((balance_mike + balance_ivan) >= amount):
    print(1);

elif (balance_mike <= amount) and (balance_ivan <= amount) and ((balance_mike + balance_ivan) <= amount):
    print(0);