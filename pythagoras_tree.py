import turtle


def draw_pythagoras_tree(branch_len, level):
    # Базовий випадок — зупиняємо рекурсію
    if level == 0:
        return

    # ОБЧИСЛЕННЯ ЕФЕКТУ ОБ'ЄМУ:
    # Використовуємо степеневу залежність (level ** 1.8) для контрасту між основою та верхівкою
    thickness = (level ** 1.8) * 0.5
    
    # Встановлюємо стан для руху вперед
    turtle.pensize(thickness)
    if level > 2:
        turtle.color("#8B4513")  # Коричневий стовбур
    else:
        turtle.color("#228B22")  # Зелене листя

    # Малюємо гілку вперед
    turtle.forward(branch_len)

    # Обчислюємо параметри для наступних розгалужень
    next_len = branch_len * 0.75
    angle = 30

    # Рекурсивний обхід правого піддерева
    turtle.right(angle)
    draw_pythagoras_tree(next_len, level - 1)

    # Рекурсивний обхід лівого піддерева
    turtle.left(angle * 2)
    draw_pythagoras_tree(next_len, level - 1)

    # Повертаємо початковий напрямок черепашки для поточного вузла
    turtle.right(angle)
    
    # Відновлюємо стан поточного рівня перед кроком назад
    turtle.pensize(thickness)
    if level > 2:
        turtle.color("#8B4513")
    else:
        turtle.color("#228B22")
        
    # Повертаємося назад
    turtle.backward(branch_len)


def main():
    try:
        user_level = int(input("Введіть рівень рекурсії (рекомендую 8 або 9): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    turtle.setup(width=900, height=700)
    turtle.speed("fastest")
    
    # Вимикаємо проміжну анімацію для швидкого рендерингу
    turtle.tracer(0, 0)

    # Початкова позиція черепашки
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -260)
    turtle.down()

    # Запуск
    draw_pythagoras_tree(130, user_level)

    # Оновлюємо екран після завершення рекурсії
    turtle.update()
    
    print("Дерево побудовано з правильними пропорціями!")
    turtle.exitonclick()


if __name__ == "__main__":
    main()