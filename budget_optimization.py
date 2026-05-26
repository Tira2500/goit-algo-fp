def greedy_algorithm(items, budget):
    """
    Жадібний підхід: максимізує співвідношення калорій до вартості.
    Швидкість роботи: O(N log N) за рахунок сортування.
    """
    # Перетворюємо словник у список для зручності сортування, 
    # додаючи розраховане співвідношення калорії/вартість
    sorted_items = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        sorted_items.append((name, info["cost"], info["calories"], ratio))
    
    # Сортуємо за спаданням питомої калорійності (ratio)
    sorted_items.sort(key=lambda x: x[3], reverse=True)
    
    chosen_items = []
    total_calories = 0
    remaining_budget = budget
    
    for name, cost, calories, _ in sorted_items:
        if remaining_budget >= cost:
            chosen_items.append(name)
            total_calories += calories
            remaining_budget -= cost
            
    return {
        "items": chosen_items,
        "total_calories": total_calories,
        "remaining_budget": remaining_budget
    }


if __name__ == "__main__":
    food_data = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    
    test_budget = 100
    
    print(f"=== ТЕСТ З БЮДЖЕТОМ {test_budget} ===")
    greedy_res = greedy_algorithm(food_data, test_budget)
    print(f"Жадібний алгоритм: {greedy_res}")