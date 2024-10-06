# This contains the main script for the program.

# import class
from classes import BudgetCategory

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()

entertainment_category = BudgetCategory("Entertainment", 100)
entertainment_category.add_expense(50)
entertainment_category.display_category_summary()

utilities_category = BudgetCategory("Utilities", 300)
utilities_category.add_expense(75)
utilities_category.display_category_summary()
