class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self): 
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)
        print(f'{item} added to queue.')

    def dequeue(self):
        if self.is_empty():
            return 'Queue is Empty!'
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.is_empty():
            return 'Queue is Empty!'
        else:
            return self.queue[0]

    def display(self):
        if self.is_empty():
            print('Queue is Empty!')
        else:
            print('Queue:', ' <- '.join(map(str, self.queue)))


def main():
    q = Queue()

    while True:
        print("\nQueue Implementation")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        try:
            choice = int(input("Enter choice (1-5): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            item = int(input("Enter item to enqueue: "))
            q.enqueue(item)
        elif choice == 2:
            item = q.dequeue()
            if item == 'Queue is Empty!':
                print(item)
            else:
                print(f'{item} dequeued from queue.')
        elif choice == 3:
            item = q.peek()
            if item == 'Queue is Empty!':
                print(item)
            else:
                print(f'The front element is {item}.')
        elif choice == 4:
            q.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
