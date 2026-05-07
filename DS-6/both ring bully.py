class BullyAlgorithm:
    def __init__(self, processes, coordinator=None):
        self.processes = processes
        self.coordinator = coordinator if coordinator else max(processes)

    def is_alive(self, process_id):
        return process_id in self.processes

    def hold_election(self, initiator):
        print(f"\nProcess {initiator} starts election.")

        higher_processes = [p for p in self.processes if p > initiator]

        if not higher_processes:
            self.coordinator = initiator
            print(f"Process {initiator} becomes new coordinator.")
            return

        for p in higher_processes:
            print(f"Election message sent from {initiator} to {p}")

        responses = [p for p in higher_processes if self.is_alive(p)]

        if responses:
            print(f"Responses received from {responses}")
            highest = max(responses)
            self.hold_election(highest)
        else:
            self.coordinator = initiator
            print(f"Process {initiator} becomes new coordinator.")

# -------------------------------
# Ring Algorithm
# -------------------------------

class RingAlgorithm:
    def __init__(self, processes):
        self.processes = sorted(processes)
        self.coordinator = None

    def hold_election(self, initiator):
        print(f"\nProcess {initiator} starts election.")

        election_list = []
        index = self.processes.index(initiator)

        while True:
            current = self.processes[index]
            election_list.append(current)

            next_index = (index + 1) % len(self.processes)
            next_process = self.processes[next_index]

            print(f"Message passed from {current} to {next_process}")

            index = next_index

            if self.processes[index] == initiator:
                break

        winner = max(election_list)
        self.coordinator = winner

        print(f"Process {winner} is elected as coordinator.")

# -------------------------------
# Main Program
# -------------------------------

print("1. Bully Algorithm")
print("2. Ring Algorithm")

choice = int(input("Enter choice: "))

if choice == 1:
    processes = [1, 2, 3, 5, 6]
    bully = BullyAlgorithm(processes)

    initiator = int(input("Enter process ID to start election: "))
    bully.hold_election(initiator)

elif choice == 2:
    processes = [1, 2, 4, 6]
    ring = RingAlgorithm(processes)

    initiator = int(input("Enter process ID to start election: "))
    ring.hold_election(initiator)

else:
    print("Invalid Choice")
