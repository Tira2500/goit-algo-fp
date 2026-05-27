import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls=100000):
    """
    Імітує кидання двох кубиків за допомогою методу Монте-Карло.
    Рахує частоту та ймовірність кожної суми від 2 до 12.
    """
    # Словник для підрахунку кількості появ кожної суми
    sum_counts = {i: 0 for i in range(2, 12 + 1)}

    # Запуск симуляції велику кількість разів
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total_sum = die1 + die2
        sum_counts[total_sum] += 1

    # Обчислення експериментальних ймовірностей у відсотках
    monte_carlo_probabilities = {
        s: (count / num_rolls) * 100 for s, count in sum_counts.items()
    }
    
    return sum_counts, monte_carlo_probabilities


def plot_results(monte_carlo_probs, analytical_probs):
    """
    Будує порівняльний графік експериментальних (Монте-Карло) 
    та аналітичних (теоретичних) ймовірностей сум чисел на кубиках.
    """
    sums = list(range(2, 13))
    mc_values = [monte_carlo_probs[s] for s in sums]
    analytical_values = [analytical_probs[s] for s in sums]

    plt.figure(figsize=(10, 6))
    
    # Малюємо стовпчики експерименту
    plt.bar([x - 0.2 for x in sums], mc_values, width=0.4, label='Метод Монте-Карло', color='skyblue')
    # Малюємо стовпчики теорії
    plt.bar([x + 0.2 for x in sums], analytical_values, width=0.4, label='Аналітичні розрахунки', color='salmon')

    plt.title('Порівняння ймовірностей сум при киданні двох кубиків', fontsize=14)
    plt.xlabel('Сума чисел на кубиках', fontsize=12)
    plt.ylabel('Імовірність (%)', fontsize=12)
    plt.xticks(sums)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    
    print("Графік успішно згенеровано! Закрийте вікно графіка для продовження.")
    plt.show()


if __name__ == "__main__":
    # Теоретичні аналітичні ймовірності (за умовою задачі)
    analytical_probabilities = {
        2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
        8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
    }

    rolls = 100000
    counts, mc_probs = simulate_dice_rolls(rolls)

    print(f"=== РЕЗУЛЬТАТИ СИМУЛЯЦІЇ (Кількість кидків: {rolls}) ===")
    print(f"{'Сума':<6}{'Кількість':<12}{'Монте-Карло (%)':<18}{'Аналітична (%)':<15}")
    print("-" * 52)
    for s in range(2, 13):
        print(f"{s:<6}{counts[s]:<12}{mc_probs[s]:.2f}%{analytical_probabilities[s]:>14}%")

    # Візуалізація результатів
    plot_results(mc_probs, analytical_probabilities)