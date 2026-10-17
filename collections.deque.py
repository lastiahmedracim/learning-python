from collections import deque

# customers = deque(["Alice", "Bob", "Charlie"])

# customers.append("David")
# customers.appendleft("Eve")

# served = customers.popleft()
# last = customers.pop()

# print(served)
# print(last)

# print(customers)

search_history = deque(maxlen= 5)

search_history.append("Python")
search_history.append("SQL")
search_history.append("Django")
search_history.append("FastAPI")
search_history.append("Docker")
search_history.append("Linux")
search_history.append("Git")

print(search_history)

search_history.append("Kubernetes")

print(search_history)