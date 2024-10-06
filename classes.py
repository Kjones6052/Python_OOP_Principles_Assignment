# These are all of the class that is used in the main.py script.

class BudgetCategory:
    # Constructor and private attributes
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    # Getters and setters for category name and budget
    def get_category(self):
        return self.__category_name
    
    def set_category(self, new_category):
        self.__category_name = new_category
    
    def get_initial_budget(self):
        return self.__allocated_budget
    
    def set_budget(self, new_budget):
        self.remaining_budget = new_budget
    
    # Method to add an expense to the category and validate expense before deduction
    def add_expense(self, amount):
        if amount < self.__allocated_budget > 0:
            self.set_budget(self.__allocated_budget - amount)
            print(f"{self.get_category()} expense added: {amount}")
        else:
            print("Insufficient budget for the expense.")
            
    # Method to display the budget category details
    def display_category_summary(self):
        print(f"{self.get_category()} allocated budget: ${self.get_initial_budget()}, Remaining Budget: ${self.remaining_budget}")
