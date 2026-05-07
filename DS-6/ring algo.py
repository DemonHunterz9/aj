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

if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    ring = RingAlgorithm(processes)
    ring.hold_election(initiator=5)