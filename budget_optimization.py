def greedy_algorithm(items, budget):
    """
    Жадібний підхід: максимізує співвідношення калорій до вартості.
    Швидкість роботи: O(N log N) за рахунок сортування.
    """
    sorted_items = []
    for name, info in items.items():
        ratio = info["calories"] / info["cost"]
        sorted_items.append((name, info["cost"], info["calories"], ratio))
    
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


def dynamic_programming(items, budget):
    """
    Динамічне програмування: знаходить абсолютно точний набір для максимальної калорійності.
    Швидкість роботи: O(N * budget)
    """
    # Перетворюємо словник у список кортежів для фіксованого індексування в таблиці DP
    item_list = [(name, info["cost"], info["calories"]) for name, info in items.items()]
    n = len(item_list)
    
    # Створюємо таблицю розміром (n + 1) x (budget + 1)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    # Заповнюємо таблицю DP за алгоритмом рюкзака
    for i in range(1, n + 1):
        name, cost, calories = item_list[i - 1]
        for w in range(budget + 1):
            if cost <= w:
                # Вибираємо максимум між тим, щоб НЕ брати страву, або ВЗЯТИ її
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
                
    # Рухаємося назад по таблиці, щоб відновити сам набір обраних страв
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        # Якщо значення змінилося в порівнянні з попереднім рядком — цей елемент було взято
        if dp[i][w] != dp[i - 1][w]:
            name, cost, _ = item_list[i - 1]
            chosen_items.append(name)
            w -= cost
            
    # Перевертаємо список, щоб зберегти прямий порядок додавання страв
    chosen_items.reverse()
    
    return {
        "items": chosen_items,
        "total_calories": dp[n][budget],
        "remaining_budget": w
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
    
    print(f"=== ПОРІВНЯЛЬНИЙ ТЕСТ З БЮДЖЕТОМ {test_budget} ===")
    
    greedy_res = greedy_algorithm(food_data, test_budget)
    print(f"Жадібний підхід:      {greedy_res}")
    
    dp_res = dynamic_programming(food_data, test_budget)
    print(f"Динамічний підхід:    {dp_res}")