import random;

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,"B":4,"C":6,"D":8
}
symbol_values={
    "A":5,"B":4,"C":3,"D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_check=column[line]
            if symbol!=symbol_check:
                break
        else:
            winnings+=values[symbol]*bet
            winning_lines.append(line+1)
    return winnings,winning_lines 

def get_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def deposit():
    while(True):
        amount=input("What would you like to deposit !? ₹")
        if amount.isdigit():
            amount=int(amount) 
            if(amount>0):
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number: ")

    return amount


def get_no_of_lines():
    while(True):
        lines=input("Enter the number of lines to bet on( 1 - "+str(MAX_LINES)+ " ) !? ")
        if(lines.isdigit()):
            lines=int(lines)
            if(1<=lines<=MAX_LINES):
                break
            else:
                print(f"Lines must be between 1 and {MAX_LINES}")
        else:
            print("Enter a number")

    return lines

def get_bet():
    while(True):
        amount=input("How much would you like to bet on each line !? ")
        if(amount.isdigit()):
            amount=int(amount)
            if(MIN_BET<=amount<=MAX_BET):
                break
            else:
                print(f"Amount should be between ₹{MIN_BET}-₹{MAX_BET}")
        else:
            print("Please enter a number")
    
    return amount

def spin(balance):
    lines=get_no_of_lines()
    while(True):
        bet=get_bet()
        total_bet=bet*lines
        if(total_bet>balance):
            print(f"You don't have enough balance,your current balance is ₹{balance}")
        else:
            break
    
    print(f"You are betting ₹{bet} on {lines} line. Total bet is ₹{total_bet}")
    
    slots=get_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winnings(slots,lines,bet,symbol_values)
    print(f"You won ₹{winnings}")
    if winning_lines:
        print(f"You won on", *winning_lines, "line(s)")
    else:
        print("You won on 0 line") 
        
    return winnings-total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ₹{balance}")
        if balance <= 0:
            print("You've run out of money!")
            answer = input("Would you like to deposit more? (y/n): ")
            if answer.lower() == 'y':
                balance += deposit()
                continue
            else:
                break
                
        answer = input("Press enter to play (q to quit)")
        if answer == "q" or answer == "Q":
            break
        balance += spin(balance)
    print("You left with ₹",balance)

# def main():
#     balance=deposit()
#     while True:
#         print(f"Current balance is ₹{balance}")
#         answer=input("Press enter to play (q to quit)")
#         if answer=="q" or answer=="Q":
#             break
#         balance+=spin(balance)
#     print("You left with ₹",balance)


main()