import random
import matplotlib.pyplot as plt

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Simulate rolling the dice multiple times
def simulate_rolls(num_rolls=100):
    results = [roll_dice() for _ in range(num_rolls)]
    return results

# Analyze results and show visualization
def analyze_results(results):
    frequencies = [results.count(i) for i in range(1, 7)]
    print("Frequencies of Dice Rolls:")
    for i in range(6):
        print(f"{i+1}: {frequencies[i]} times")

    plt.bar(range(1, 7), frequencies, tick_label=[str(i) for i in range(1, 7)])
    plt.title("Dice Roll Frequencies")
    plt.xlabel("Dice Face")
    plt.ylabel("Count")
    plt.grid(axis='y')
    plt.show()

# Run the simulation
if __name__ == "__main__":
    dice_results = simulate_rolls(100)
    analyze_results(dice_results)
