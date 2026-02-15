from traceback import print_tb
import time

from plyer import notification
import time

def show_notification(step):
    notification.notify(
        title="Прогрес процесу",
        message=f"Виконано {step}/5 кроків",
        timeout=5  # Час показу сповіщення
    )


def ceyvo():
    pass

def reverse(text):
    return text[::-1]  #usage:  [start:stop:step]

def why_not():
    pass

if __name__ == "__main__":
    print(reverse("reverse"))

    print("Hello World")


