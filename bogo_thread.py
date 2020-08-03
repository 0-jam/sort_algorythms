import threading
import time

from modules.list_generator import generate_random_list
from modules.sorter import bogo_sort

play_event = threading.Event()


def play(event):
    event.wait()

    time.sleep(1)
    print('complete')
    event.clear()


def init_player():
    return threading.Thread(target=play, args=(play_event,))


def main():
    orig_list = generate_random_list(list_size=7)

    for i in range(3):
        player = init_player()
        player.start()

        print('attempt:', i)

        bogo_sort(orig_list)
        play_event.set()

    player.join()
    print('done')


if __name__ == '__main__':
    main()
