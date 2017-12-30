def get_total_cost_of_meal():
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    tip = meal_cost / 100 * tip_percent
    tax = meal_cost / 100 * tax_percent
    total_cost = int(round(meal_cost+tip+tax))
    return str(total_cost)

print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")
