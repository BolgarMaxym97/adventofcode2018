import heapq
from collections import defaultdict

lines = open('../../dist/7.txt', 'r').readlines()
lines = [line.strip() for line in lines if line.strip()]

connections = []

char_to_succ = defaultdict(list)  # successors
char_to_pred = defaultdict(list)  # predecessors

for line in lines:
    split = line.split(' ')
    src, dst = split[1].strip(), split[7].strip()
    connections.append((src, dst))

for (src, dst) in connections:
    char_to_succ[src].append(dst)
    char_to_pred[dst].append(src)

q = []
starters = set(char_to_succ.keys()) - set(char_to_pred.keys()) # possible starting points (tasks with no predecessors)
for starter in starters:
    heapq.heappush(q, starter)

order = []
while q:
    next_item = heapq.heappop(q)
    order.append(next_item)
    for s in char_to_succ[next_item]:
        preds = char_to_pred[s]
        if s not in order and all(p in order for p in preds):
            heapq.heappush(q, s)

print("".join(order))