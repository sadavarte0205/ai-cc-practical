from queue import PriorityQueue

goal = [1,2,3,4,5,6,7,8,0]

def heuristic(state):
    return sum([1 for i in range(9) if state[i] != goal[i]])

pq = PriorityQueue()

start = [1,2,3,4,5,6,0,7,8]

pq.put((heuristic(start), start))

visited = []

while not pq.empty():
    cost, state = pq.get()

    if state == goal:
        print("Goal Reached")
        print(state)
        break

    visited.append(state)

    print(state)