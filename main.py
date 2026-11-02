print("Hello World")

from collections import deque

'''1. Initializing the queue and adding five orders with numbers
  We use tuples (order_number, drink_name) for clarity'''
cafe_queue = deque([
    (101, "Еспресо"),
    (102, "Лате"),
    (103, "Капучино"),
    (104, "Американо"),
    (105, "Флет Вайт")
])
print("Чергу замовлень створено. Додано 5 замовлень.")

'''Function to check if the queue is empty'''
def check_queue(q):
    if not q:
        print("Черга порожня! Всі замовлення виконано.")
        return True
    return False

'''2. Display the next order to be prepared (the item at the front of the queue)'''
if not check_queue(cafe_queue):
    next_order = cafe_queue[0]
    print(f"Наступне замовлення на черзі: №{next_order[0]} ({next_order[1]})")

print("\n--- Обробка замовлень ---")

'''3. We process two orders (removing them from the beginning using popleft)'''
for _ in range(2):
    if not check_queue(cafe_queue):
        served_order = cafe_queue.popleft()
        print(f"Замовлення №{served_order[0]} ({served_order[1]}) готове та видане!")

print("\n--- Поточний стан черги ---")

'''4. Displaying remaining orders'''
if not check_queue(cafe_queue):
    print("Замовлення, що залишилися в черзі:")
    for order in cafe_queue:
        print(f"  • Замовлення №{order[0]}: {order[1]}")

'''5. Display a message if the queue is empty'''
print("\n--- Очищення черги для демонстрації порожнього стану ---")
while cafe_queue:
    cafe_queue.popleft()


check_queue(cafe_queue)