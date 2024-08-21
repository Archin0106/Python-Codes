S = []

def isEmpty(stk):
    return len(stk) == 0
    
def push(stk, item):
    stk.append(item)
    print(f'{item} added successfully')

def s_pop(stk):
    if isEmpty(stk):
        return 'Underflow!'
    else:
        return stk.pop()

def peek(stk):
    if isEmpty(stk):
        return 'Underflow!'
    else:
        return stk[-1]

def display(stk):
    if isEmpty(stk):
        print('Stack is Empty')
    else:
        print(f'{stk[-1]} <---top')
        for i in range(len(stk) - 2, -1, -1):
            print(stk[i])

while True:
    print("\nStack Implementation")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    try:
        ch = int(input("Enter choice (1-5): "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    if ch == 1:
        item = int(input("Enter item you want to push: "))
        push(S, item)
    elif ch == 2:
        item = s_pop(S)
        if item == 'Underflow!':
            print('Stack is Empty!')
        else:
            print(f'{item} is popped')
    elif ch == 3:
        item = peek(S)
        if item == 'Underflow!':
            print('Stack is Empty!')
        else:
            print(f'{item} is at top')
    elif ch == 4:
        display(S)
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid")
