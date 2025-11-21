# Made by Luuk Klingens
# GitHub: https://github.com/luukklingens
# Copyright Luuk Klingens 2025

# Practice file to demonstrate stack traces found online which i am analyzing on the moment. 


def make_pizza(toppings):
    # 🍕 Let's make a pizza!
    print(f"Making pizza with {len(toppings)} toppings")
    return f"Pizza ready with {', '.join(toppings)}! 🍕"

def order_pizza():
    # 🛒 Customer orders a pizza
    toppings = None  # Oops! Forgot to set toppings
    return make_pizza(toppings)

# 🎮 Let's try to order!
result = order_pizza()