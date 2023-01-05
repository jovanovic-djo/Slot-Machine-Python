# importing 'random' module in order to define values randomly
import random

# defining constant values
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3

# determining how rare and valuable are symbols within slot machine
# instead of fruit symbols, capital letters or other objects can represent slot machine symbols
symbol_count = {
    "🍒": 2,
    "🍇": 4,
    "🍌": 6,
    "🥝": 8

}

symbol_value = {
    "🍒": 10,
    "🍇": 7,
    "🍌": 5,
    "🥝": 3
}


# method that returns total amount of winnings and number of lines
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


# generating symbols layout with every spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for i, j in symbols.items():
        for _ in range(j):
            all_symbols.append(i)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# printing slot symbols layout in program terminal 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# input of valid value for deposit
def deposit():
    while True:
        amount = input("Wanted deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Error occured!")
        else:
            print("Enter valid number!")
    return amount

# user chooses 1 - 3 lines to bet on
def get_number_of_lines():
    while True:
        lines = input(
            "Bet lines (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Error occured!")
        else:
            print("Enter valid number!")

    return lines


# user enters his choosen bet
def get_bet():
    while True:
        amount = input("Enter Bet: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Error occured!")
        else:
            print("Enter valid number!")
    return amount


# Method that calculates winnings or loses based on spin and balance
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("Error occured!")
        else:
            break
    slots = get_slot_machine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    return winnings - total_bet

# main function that includes all previous methods
# calculates final user balance
def main():
    balance = deposit()
    while True:
        print(f"Balance: ${balance}")
        answer = input("Press enter to play (q to quit) ")
        if answer.upper() == "Q":
            break
        balance += spin(balance)
    print(f"Total: ${balance}")

# calling main method
main()
