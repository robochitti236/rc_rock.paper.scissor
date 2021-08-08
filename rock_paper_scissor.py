def main():
    import random
    print("welcome to the official rock paper scissor game created by arun")
    print("do you want to know instructions? y/n")
    y=input()
    if y == "y":
        print("enter 1 for rock, 2 for paper, 3 for scissor")
        print("now lets start the game")
    else:
        print("now lets start the game")
    print("enter your input: ")
    i=int(input())
    comp=[1, 2, 3]
    com=int(random.choice(comp))
    if i<=3:
        print("your choice: ")
        if i==1:
            print("rock")
        elif i==2:
            print("paper")
        else:
            print("scissor")
        print("its computers turn now.....")
        print("computer choice is: ")
        if com==1:
            print("rock")
        elif com==2:
            print("paper")
        else:
            print("scissor")
        if int(i) == com:
            print("draw")
        elif (i==1) and (com==2):
            print("computer wins")
        elif (i==1) and (com==3):
            print("you win")
        elif (i==2) and (com==1):
            print("you win")
        elif (i==2) and (com==3):
            print("computer wins")
        elif (i==3) and (com==1):
            print("computer wins")
        else:
            print("you win")
    else:
        print("invalid input")
    print("do you wanna play it again? y/n")
    restart=input()
    if restart == "y":
        main()
    else:
        print("hope you enjoyed this game. see ya next time.")
        exit()
main()