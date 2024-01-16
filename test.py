import sys
import time


def progress_bar(iterable, length=30):
    total = len(iterable)
    step = total / length
    current = 0

    for i, item in enumerate(iterable):
        yield item
        current += 1
        if current >= step:
            sys.stdout.write("\r[" + "=" * int(i / total * length) + " " * (length - int(i / total * length)) + f"] {int(i / total * 100)}%")
            sys.stdout.flush()
            current = 0

    sys.stdout.write("\n")
    sys.stdout.flush()



items_to_process = range(11)
for item in progress_bar(items_to_process):
    # Ваш код обработки здесь
    time.sleep(0.1)