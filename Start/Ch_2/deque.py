# deque objects are like double-ended queues

import collections
import string


# TODO: initialize a deque with lowercase letters
deq = collections.deque(string.ascii_lowercase)

# TODO: deques support the len() function
print(f"Item Count:{len(deq)}")

# TODO: deques can be iterated over
for item in deq:
    print(item.upper())
# TODO: manipulate items from either end
deq.pop()
deq.popleft()
deq.append(1)
deq.appendleft(2)
print(deq)

# TODO: use an index to get a particular item
print(deq[2])

# rotate
deq.rotate(1)
print(deq)

deq.rotate(-4)
print(deq)

