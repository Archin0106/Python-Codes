class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def push(self, data):
        self.queue.append(data)
        print(f"Enqueued {data} to queue.")

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        dequeued_data = self.queue.pop(0)
        print(f"Dequeued {dequeued_data} from queue.")
        return dequeued_data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        front_data = self.queue[0]
        print(f"Front of the queue is {front_data}")
        return front_data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        print("Queue elements are:")
        for data in self.queue:
            print(data, end=" -> ")
        print("None")


def main():
    queue = Queue()

    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Get Front\n4. Display\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            data = input("Enter value to enqueue: ")
            queue.push(data)
        elif choice == '2':
            queue.pop()
        elif choice == '3':
            queue.get_front()
        elif choice == '4':
            queue.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
