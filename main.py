from plyer import notification
import time

def show_notification(step):
    notification.notify(
        title="Прогрес процесу",
        message=f"Виконано {step}/5 кроків",
        timeout=5  # Час показу сповіщення
    )


def reverse(text):
    return text[::-1]  #usage:  [start:stop:step]


if __name__ == "__main__":
    print(reverse("12345678"))




