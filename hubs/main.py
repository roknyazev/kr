from server import *
import time
import threading
import requests
import multiprocessing


def start_uav(slot):
    # {'orders': [{id: track}, {id: track}, {id: track}, ...], 'departure_hub_id': id, 'destination_hub_id': id}
    
    i = 0
    for next_hub, products in slot.dirs.items():
        print("len products ", len(products))
        i = i + 1
        d = {"orders": [products], 'departure_hub_id': hubId[0], 'destination_hub_id': next_hub}
        print("Send")
        r = requests.post("http://45.79.251.166:8080/api/orders", data=d)


def work():
    while True:
        time.sleep(0.01)
        t = time.time()
        key = None
        try:
            key = min(supply.keys())
        except BaseException:
            key = None
            continue
        try:
            if t >= key and key != None and key != 0:
                start_uav(supply[key])
                supply.pop(key)
        except BaseException:
            continue


def run_proc(port):
    thread = threading.Thread(target=work)
    thread.start()
    run(port - 8000, addr="188.134.78.182", port=port)


if __name__ == '__main__':
    proces = []
    for i in range(207):
        time.sleep(0.1)
        proces.append(multiprocessing.Process(target=run_proc, args=(8000 + i,)))
        proces[i].start()
    proces[0].join()

