import turtle


def draw_pythagoras_tree(branch_len, level):
    # Базовий випадок (умова виходу з рекурсії)
    if level == 0:
        return

    # Малюємо основну гілку (стовбур поточного піддерева)
    turtle.forward(branch_len)

    # Обчислюємо параметри для наступного рівня
    next_len = branch_len * 0.75  # Кожна наступна гілка коротша на 25%
    angle = 30  # Кут розгалуження гілок

    # Рекурсивний виклик для правого піддерева
    turtle.right(angle)
    draw_pythagoras_tree(next_len, level - 1)

    # Рекурсивний виклик для лівого піддерева
    turtle.left(angle * 2)
    draw_pythagoras_tree(next_len, level - 1)

    # Повертаємо черепашку в початкову позицію та напрямок
    turtle.right(angle)
    turtle.backward(branch_len)


def main():
    # Запит рівня рекурсії у користувача
    try:
        user_level = int(input("Введіть рівень рекурсії (оптимально від 1 до 10): "))
    except ValueError:
        print("Будь ласка, введіть коректне ціле число.")
        return

    # Налаштування екрана та швидкості малювання
    turtle.setup(width=800, height=600)
    turtle.speed("fastest")
    turtle.left(90)  # Повертаємо черепашку вгору, щоб дерево росло знизу вгору
    turtle.up()
    turtle.goto(0, -200)  # Зміщуємо точку старту донизу екрана
    turtle.down()
    turtle.color("green")

    # Перший виклик рекурсивної функції
    draw_pythagoras_tree(100, user_level)

    # Тримаємо вікно відкритим після завершення малювання
    turtle.mainloop()


if __name__ == "__main__":
    main()