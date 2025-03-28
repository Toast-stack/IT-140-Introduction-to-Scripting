# IT-140: Introduction to Scripting

## **Overview**
This repository contains coursework for *IT-140: Introduction to Scripting*. The assignments and projects focus on fundamental programming concepts using Python. Key topics covered include user input handling, conditional statements, loops, functions, and file handling.

## **Table of Contents**
- [Module 2: Simple User Interaction](#module-2-simple-user-interaction)
- [Module 3: Wage Calculation](#module-3-wage-calculation)
- [Module 4: Number Guessing Game](#module-4-number-guessing-game)
- [Project 1: Text-Based Adventure Game](#project-1-text-based-adventure-game)
- [Key Takeaways](#key-takeaways)

---

## **Module 2: Simple User Interaction**
### **Description**
This script demonstrates basic user input handling and output formatting. It prompts the user for their name and age, then calculates their birth year based on the current year (2022).

### **Code Snippet**
     ''' Python
     user_name = input("Enter your name: ")
     user_age = int(input("Enter your age: "))
     current_year = 2022
     birth_year = current_year - user_age

     print('Hello', user_name + '!', 'You were born in', birth_year)

### Concepts Covered
* Basic  `input()` and `print()` functions
* Data type conversion (`int()`)
* string formatting

## Module 3: Wage Calculation
### **Description**
This script calculates the total wages for a user based on their work hours. It implements overtime pay logic:
* Regular hours (≤ 40) are paid at `$20/hour`
* Overtinme hours (>40) are paid at `$30/hour`

### **Code Snippet**
    ''' python
    user_wage = 20
    user_over = 30
    hours = int(input("Enter hours worked: "))

    if hours <= 40:
        total = (hours * user_wage)
    else:
        over_t = (hours % 40)
        reg_t = (hours - over_t)
        total = (reg_t * 20) + (over_t * 30)

    print("Total earnings:", total)

### **Concepts Covered**
* Conditional statements `if-else`
* Arithmetic operations
* Basic payroll calculation roll

## Module 4: Number Guessing Game
### **Description**
This script generates a random number within a user-defined range and allows the player to guess it. The game provides feedback if the guess is too high or too low.

### **Code Snippet**
    ''' python
    import random

    lwr_bnd = int(input("Choose a lower bound: "))
    up_bnd = int(input("Choose an upper bound: "))

    if lwr_bnd < up_bnd:
        rnd_int = random.randint(lwr_bnd, up_bnd)
        while True:
            guess = int(input("Please guess a number: "))
            if guess < lwr_bnd or guess > up_bnd:
                print("Please choose a number between your lower and upper bound.")
            elif guess == rnd_int:
                print("You got it!")
                break
            elif guess > rnd_int:
                print("Nope, too high.")
            else:
                print("Nope, too low.")

### **Concepts Covered**
* Random number generation (`random.randint()`)
* Loops (`while True`)
* Conmditional logic (`if-elif-else`)

## Project 1: Text-Based Adventure Game
### **Overview**
This project is a text-based adventure game where the player navigates through different rooms, collecting essential items to defeat a dragon and save the kingdom.

### **Game Features**
* **Room Navigation:** Players move between rooms using directional commands (North, South, East, West).
* **Item Collection:**  Certain rooms contain essential items for the final battle.
* **Win/Loss Conditions:**
    * Enter the Dragon’s Den with all required items → Victory!
    * Enter without required items → Defeat.

### **Game Flow**
1. **Introduction** - The player receives background information and instructions.
2. **Exploration** - The player navigates eight rooms and collects items.
3. **Final Battle** - The outcome depends on the player's inventory.

### **Code Structure**
* Dictionaries are used to store room connections.
* Loops & Conditionals drive game logic.
* User Input Handling ensures smooth interaction.

## **Key Takeaways**
This course introduced fundamental programming skills that are relevant to software development and automation
1. **Input Handling & Validation** - Ensuring correct user input prevents errors in real-world applications.
2. **Looping & Iteration** - Essential for scripting repetitive tasks.
3. **Modular Code Design** - Helps maintain readability and efficiency in complex programs.

## **Future Enhancements**
* **Expand Game Mechanics** - Add more challenges or an interactive combat system.
* **Improve Code Efficiency** - Refactor scripts to use more modular functions.
* **Implement a GUI** - Convert text-based games into graphical applications.

## **How to Run the code**
### **Prerequisites**
* Python 3 installed on your system
* clone this repository:

      ''' sh
      git clone https://github.com/Toast-stack/IT-140-Introduction-to-Scripting.git
* Run the Python scripts using:

      ''' sh
      python <filename>.py

