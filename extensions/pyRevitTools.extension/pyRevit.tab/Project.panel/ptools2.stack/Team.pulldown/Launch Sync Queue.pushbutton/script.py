import json

class SynchronizationQueue:
    def __init__(self):
        self.queue = []
        self.current_user = None

    def load_queue(self):
        try:
            with open('sync-queue.json', 'r') as file:
                self.queue = json.load(file)
        except FileNotFoundError:
            self.queue = []

    def save_queue(self):
        with open('queue.json', 'w') as file:
            json.dump(self.queue, file)

    def join_queue(self, user):
        if user not in self.queue:
            self.queue.append(user)
            self.save_queue()
            print(f'{user} joined the queue.')

    def leave_queue(self, user):
        if user in self.queue:
            self.queue.remove(user)
            self.save_queue()
            print(f'{user} left the queue.')

    def synchronize(self):
        if self.current_user is None and self.queue:
            self.current_user = self.queue.pop(0)
            self.save_queue()
            print(f'Synchronizing with central model for {self.current_user}.')
            self.current_user = None

    def display_queue(self):
        print('Current Queue:')
        for user in self.queue:
            print(user)

if __name__ == "__main__":
    queue = SynchronizationQueue()
    queue.load_queue()

    while True:
        print("\nOptions:")
        print("1. Join Queue")
        print("2. Leave Queue")
        print("3. Synchronize")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            user = input("Enter your username: ")
            queue.join_queue(user)
        elif choice == '2':
            user = input("Enter your username: ")
            queue.leave_queue(user)
        elif choice == '3':
            queue.synchronize()
        elif choice == '4':
            queue.display_queue()
        elif choice == '5':
            queue.save_queue()
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
