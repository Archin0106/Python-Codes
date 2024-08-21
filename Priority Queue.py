class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def insert(self, data):
        self.queue.append(data)
        print(f"Inserted {data} into priority queue")

    def delete(self):
        try:
            if self.is_empty():
                print("Priority queue Empty")
                return None
            max_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_val]:
                    max_val = i
            item = self.queue[max_val]
            del self.queue[max_val]
            print(f"Removed {item} from priority queue")
            return item
        except IndexError:
            print("Priority queue Empty")
            return None
        
    def display(self):
        if self.is_empty():
            print("Priority queue Empty")
        else:
            print(f"Priority queue: {self}")

def main():
    myQueue = PriorityQueue()
    while True:
        print("\nOptions: ")
        print("1. Insert")
        print("2. Delete (on Priority)")
        print("3. Display")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            data = int(input("Enter data to be inserted: "))
            myQueue.insert(data)
        elif choice == '2':
            myQueue.delete()
        elif choice == '3':
            myQueue.display()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
