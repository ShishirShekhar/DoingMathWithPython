import random

def num_toss_money(amount):
    tosses = 0

    while amount > 0:
        
        toss = random.randint(0,1)
        tosses += 1

        if toss == 0:
            amount -= 1.50
            print("Tails! Current amount:", amount)
        
        elif toss == 1:
            amount += 1
            print("Heads! Current amount:", amount)

    print("Game over :(")
    print("Current amount:", amount, "Coint toss:", tosses)

if __name__ == "__main__":
    amount = int(input("Enter starting amount: "))
    num_toss_money(amount)
