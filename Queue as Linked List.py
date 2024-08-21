class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def push(self, data):
        new_node = Node(data)
        if self.rear is None:  # If queue is empty
            self.front = self.rear = new_node
            print(f"Enqueued {data} to queue.")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued {data} to queue.")

    def pop(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:  # If the queue becomes empty after dequeue
            self.rear = None
        print(f"Dequeued {dequeued_data} from the queue.")
        return dequeued_data

    def get_front(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        print(f"Front of the queue is {self.front.data}")
        return self.front.data

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        print("Queue elements are:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
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
