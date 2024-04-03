#!/usr/bin/env python
# coding: utf-8

# # Title: 
# Bank Management System

# # Objective:
# To develop a software system that allows efficient management of customer accounts and banking operations for a bank.

# # Problem Statement:
# Traditional banking systems often involve manual processes and paperwork, leading to inefficiencies and delays in customer service. A modernized system is needed to streamline operations, enhance customer experience, and ensure accuracy in financial transactions.

# # Tools:
# Programming Language: Python

# In[1]:


class Bank:
    def __init__(self,bank_name):
        self.bank_name=bank_name
        self.customers={}

    def add_customer(self,customer_id,name,initial_balance=0):
        if customer_id not in self.customers:
            self.customers[customer_id]={'name':name,'balance':initial_balance}
            print(f"Customer '{name}' added successfully!")
        else:
            print("Customer ID already exists. Please choose a different ID.")

    def deposit(self,customer_id,amount):
        if customer_id in self.customers:
            self.customers[customer_id]['balance']+=amount
            print("Deposit successful!")
        else:
            print("Customer ID not found.")

    def withdraw(self,customer_id,amount):
        if customer_id in self.customers:
            if self.customers[customer_id]['balance']>=amount:
                self.customers[customer_id]['balance']-=amount
                print("Withdrawal successful!")
            else:
                print("Insufficient balance.")
        else:
            print("Customer ID not found.")

    def check_balance(self,customer_id):
        if customer_id in self.customers:
            print(f"Balance for customer '{self.customers[customer_id]['name']}':${self.customers[customer_id]['balance']}")
        else:
            print("Customer ID not found.")

    def display_customers(self):
        print("\nCustomers:")
        for customer_id,details in self.customers.items():
            print(f"ID:{customer_id}, Name:{details['name']}, Balance:${details['balance']}")


def main():
    bank_name=input("Enter bank name: ")
    bank=Bank(bank_name)

    while True:
        print("\nMenu:")
        print("1. Add Customer")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display Customers")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            customer_id = int(input("Enter customer ID: "))
            name = input("Enter customer name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.add_customer(customer_id, name, initial_balance)
        elif choice == '2':
            customer_id = int(input("Enter customer ID: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(customer_id, amount)
        elif choice == '3':
            customer_id = int(input("Enter customer ID: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(customer_id, amount)
        elif choice == '4':
            customer_id = int(input("Enter customer ID: "))
            bank.check_balance(customer_id)
        elif choice == '5':
            bank.display_customers()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


main()


# In[ ]:




