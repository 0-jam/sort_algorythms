import threading
import multiprocessing as mp
import time

from modules.list_generator import generate_random_list
from modules.sorter import bogo_sort


def play(event):
    event.wait()

    time.sleep(1)
    print('complete')
    event.clear()


def init_player():
    return threading.Thread(target=play, args=(play_event,))


def sort():
    play_event = threading.Event()
    orig_list = generate_random_list(list_size=9)
    while True:
        player = threading.Thread(target=play, args=(play_event,))
        player.start()

        bogo_sort(orig_list)
        play_event.set()


def main():
    sorter = mp.Process(target=sort)

    sorter.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        sorter.kill()
    finally:
        print('done')


if __name__ == '__main__':
    main()
