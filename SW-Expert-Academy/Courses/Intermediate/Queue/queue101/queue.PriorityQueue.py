import queue
q = queue.PriorityQueue()

q.put((3, "c"))
q.put((1, "a"))
q.put((2, "b"))

print(q.get())
print(q.get())
print(q.get())