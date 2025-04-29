# PROJECT-1
# Import:
# - datetime from datetime
from datetime import datetime
# Classes:
# - Task
#   - init(self, title, description, due_date)
#   - mark_complete(self)
#   - str(self)
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False

    def mark_complete(self):
        self.status = True

    def __str__(self):
        return f'Title: {self.title}\n Description: {self.description}\n Due Date: {self.due_date}\n Status: {self.status}\n'
    
# - ToDoList
#   - init(self)
#   - add_task(self, title, description, due_date)
#   - mark_task_complete(self, title)
#   - list_all_tasks(self)
#   - list_incomplete_tasks(self)
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date):
        task = Task(title, description, due_date)
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f'The {title} completed successfully!')    
            else:
                print(f'The {title} not found')

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.status:
                print(task)
        # print('All completed!')


# Function:
# - main()
def main():
    todo = ToDoList()

    while True:
        print("\nToDo List Menu:")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            title = input('Enter task title: ')
            description  = input('Enter task description: ')
            due_date_str = input('Enter due date YYYY-MM-DD: ')
            try:
                due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
                todo.add_task(title, description, due_date)
                print('Task added successfully!')
            except ValueError:
                print('Invalid date format, use YYYY-MM-DD')
        elif choice == '2':
            title = input('Enter the title of the task to mark as complete: ')
            todo.mark_task_complete(title)
        elif choice == '3':
            todo.list_all_tasks()
        elif choice == '4':
            todo.list_incomplete_tasks()
        elif choice == '5':
            print('Exit, goodbye!')
            break
        else:
            print('Invalid choice, please enter number from 1 to 5: ')  

# Condition:
if __name__ == "__main__":
    main()

PROJECT-2
# Homework 2. Simple Blog System

# Define Post Class:
# Create a Post class with attributes like title, content, and author.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f'Title: {self.title} \n Content: {self.content} \n Author: {self.author}'

# Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
# Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
class Blog:
    def __init__(self):
        posts = []

    def add_post(self, title, content, author):
        post = Post(title, content, author)
        self.posts.append(post)

    def list_all_posts(self):
        for a in self.posts:
            print(a)

    def display_by_author(self, author):
        if self.author == author:
            self.__str__()
    
    def delete_post(self, title):
        if self.title == title:
            self.posts.remove(self.post)

    def edit_post(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        print('Edited successfully!')

    def display_latest_post(self):
        if self.posts:
            self.posts[-1]
        else: 
            print('There is no any post')

# Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
def main():
    post = Post()

    while True:
        print("\nSimple Blog System:")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Edit Post")
        print("4. Display Specific Post ")
        print("5. Display Latest Post ")
        print("6. Delete Post")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            title = input('Enter a title: ')
            content = input('Enter a content: ')
            author = input('Enter an author')
        elif choice == '2':
            post.list_all_posts()
            #post = Post(title, content, author)
        elif choice == '3':
            post.edit_post()
        elif choice == '4':
            post.display_by_author()
        elif choice == '5':
            post.display_latest_post()
        elif choice == '6':
            post.delete_post()
        elif choice == '7':
            print('exit, goodbye!')
            break
        else:
            print('please, enter number from 1-7 =>')
# Condition:
if __name__ == "__main__":
    main()

PROJECT-3
# Homework 3. Simple Banking System

# Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
class Account:
    def __init__(self, account_number, holder_name, balance = 0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def __str__(self):
        return f'Account Number: {self.account_number}, Account holder name: {self.holder_name}, Account Balance: {self.balance}'
# Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
# Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
class Bank:
    accounts = []

    def add_account(self, account_number, holder_name, balance):
        account = Account(self, account_number, holder_name, balance)
        self.accounts.append(account)
        print('Account added successfully!')

    def check_balance(self):
        if self.balance:
            print(self.balance)
        else:
            print('0 balance')
    
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Deposited {amount}. New balance is {self.balance}')
        else:
            print('Deposit value must be positive')

    def withdraw_money(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f'Withdrawn {amount}. New balance is {self.balance}')
            else: 
                print('Insufficient balance')
        else:
            print('Withdrawal amount must be positive.')

    def transfer_money(self, amount, receiver_account):
        if amount >= 0:
            if amount > self.balance:
                self.balance -= amount
                receiver_account += amount
                print(f'Transferred {amount} to {receiver_account} \n Your new balance is {self.balance}')
            else:
                print('Insufficient balance. Transfer failed')
        else:
            print('Transfer amount must be posotive')

    def display_account_details(self, account):
        print(account)

# Create Main Program:
# Develop a CLI to interact with the Banking system.
def Main():
    account = Account()

    while True:
        print("\nSimple Blog System:")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            account_number = input('Enter an account number: ')
            holder_name = input('Enter an account holder name: ')
            balance = input('Enter your balance: ')
        elif choice == '2':
            account.check_balance()
        elif choice == '3':
            account.deposit_money()
        elif choice == '4':
            account.withdraw_money()
        elif choice == '5':
            account.transfer_money()
        elif choice == '6':
            account.display_account_details()
        elif choice == '7':
            print('Exiting, bye!')
            break
        else:
            print('Please enter number from 1-7 :')

if __name__ == "__main__":
    Main()

