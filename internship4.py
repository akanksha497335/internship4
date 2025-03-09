import random

def coin_toss():
    return random.choice(["Heads", "Tails"])

def multiple_tosses(n):
    heads, tails = 0, 0
    for _ in range(n):
        result = coin_toss()
        print(result)
        if result == "Heads":
            heads += 1
        else:
            tails += 1
    
    print("\nResults:")
    print(f"Heads: {heads} ({(heads/n)*100:.2f}%)")
    print(f"Tails: {tails} ({(tails/n)*100:.2f}%)")

def main():
    while True:
        try:
            flips = int(input("Enter the number of coin flips: "))
            if flips <= 0:
                print("Please enter a positive number.")
                continue
            multiple_tosses(flips)
        except ValueError:
            print("Invalid input. Please enter a number.")

        again = input("Do you want to toss again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
