import random
count = 0
while True :
    data = (input("Roll the dice...(Y/N)?")).lower()
    
    if(data == 'y'):
        no_dice = int(input("How many dice do you want...?"))
        result_tuple = tuple(random.randint(1, 6) for _ in range(no_dice))
#        for i in range (no_dice):
#            random_num = random.randint(1, 6)
#            print(f"Roll {i+1}: {random_num}")
        print(result_tuple)
        count += 1
    elif(data == 'n'):
        print("Thank you for playing!!")
        print(f"You have rolled the dice {count} times")
        break
    else :
        print("Wrong Choice..!!")

