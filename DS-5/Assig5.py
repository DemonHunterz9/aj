import threading
import time

class TokenRing:
    def __init__(self, num_processes):
        self.num_processes = num_processes
        self.current_holder = 0
        self.running = True  # control flag

    def process(self, process_id):
        while self.running:
            if self.current_holder == process_id:
                print(f"Process {process_id} ENTERING critical section")
                time.sleep(1)
                print(f"Process {process_id} EXITING critical section\n")

                # Pass token to next process
                self.current_holder = (process_id + 1) % self.num_processes

            time.sleep(0.5)

    def start(self):
        threads = []

        for i in range(self.num_processes):
            t = threading.Thread(target=self.process, args=(i,))
            threads.append(t)
            t.start()

        # wait for user to stop
        input("Press ENTER to stop...\n")
        self.running = False

        for t in threads:
            t.join()


# ---- MAIN ----
num = int(input("Enter number of processes: "))
ring = TokenRing(num)
ring.start()