import queue
import time

service_queue = queue.Queue()

def generate_request(request_id):
    print(f"Нова заявка {request_id} додана до черги.")
    service_queue.put(f"Заявка #{request_id}")

def process_request():
    if not service_queue.empty():
        request = service_queue.get()
        print(f"Обробка {request}...")
        time.sleep(1)  
        print(f"{request} оброблено.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

def main():
    request_id = 1 
    while True:
        print("\nМеню:")
        print("1. Створити нову заявку")
        print("2. Обробити заявку")
        print("3. Вийти")

        choice = input("Виберіть опцію: ")
        
        if choice == "1":
            generate_request(request_id)
            request_id += 1
        elif choice == "2":
            process_request()
        elif choice == "3":
            print("Роботу завершено.")
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
