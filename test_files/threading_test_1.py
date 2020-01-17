import time
import threading

event = threading.Event()

def wait_fnc():
    print("...waiting func...")
    while not event.is_set():
        event.wait(5.0)
    print("done waiting")

def tgr_fnc():
    print("...tgr func...")
    print("sleeping in tgr")
    time.sleep(60)
    print("done sleeping in tgr")
    print("triggering")
    event.set()

def main():
    t1 = threading.Thread(target=wait_fnc)
    t2 = threading.Thread(target=tgr_fnc)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
