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
if __name__ == "__main__":
    processes = [1, 2, 3, 4, 5]
    bully = BullyAlgorithm(processes)
    bully.hold_election(initiator=5)