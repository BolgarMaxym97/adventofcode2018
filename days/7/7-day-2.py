import sys
import heapq
from pprint import pprint
from collections import defaultdict

class Worker:
    def __init__(self):
        self.task = None
        self.done = False
        self.working_for = 0

    def set_task(self, task):
        self.task = task
        self.done = False
        self.working_for = (ord(task) - ord('A') + 1) + 60

    def is_busy(self):
        return self.working_for > 0

    def next_timestep(self):
        if self.is_busy:
            self.working_for -= 1
            if self.working_for == 0:
                self.done = True

lines = open('../../dist/7.txt', 'r').readlines()
lines = [line.strip() for line in lines if line.strip()]

connections = []
char_to_succ = defaultdict(list)
char_to_pred = defaultdict(list)

for line in lines:
    split = line.split(' ')
    src, dst = split[1].strip(), split[7].strip()
    connections.append((src, dst))

for (src, dst) in connections:
    char_to_succ[src].append(dst)
    char_to_pred[dst].append(src)

workers = [Worker() for _ in range(5)]

order = []
q = []
starters = set(char_to_succ.keys()) - set(char_to_pred.keys())
for starter in starters:
    heapq.heappush(q, starter)

seconds = 0
while len(order) != 26:
    available_workers = [worker for worker in workers if not worker.is_busy()]

    for worker in available_workers:
        if q:
            next_task = heapq.heappop(q)
            worker.set_task(next_task)

    for worker in workers:
        worker.next_timestep()
        if worker.done:
            order.append(worker.task)

            for s in char_to_succ[worker.task]:
                preds = char_to_pred[s]
                if s not in order and all(p in order for p in preds):
                    heapq.heappush(q, s)

            worker.done = False

    seconds += 1

print(seconds)