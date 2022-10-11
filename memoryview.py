# 当我们需要反复大量的进行一段数据的读取操作或者改变原数据的赋值操作，使用memoryview的时候，每次不不要重新在内存中进行赋值。


import time
import matplotlib.pyplot as plt

sizes = range(100000, 600000, 100000)
# Without Memoryview
l1 = []
for n in sizes:
    data = b'x' * n
    start = time.time()
    b = data
    while b:
        b = b[1:]
    stop = time.time()
    print(f'bytes {n} {stop-start}')
    l1.append(stop-start)
# With Memoryview
l2 = []
for n in sizes:
    data = b'x' * n
    start = time.time()
    b = memoryview(data)
    while b:
        b = b[1:]
    stop = time.time()
    print(f'memview {n} {stop-start}')
    l2.append(stop-start)
# Plot everything
plt.plot(l1, 'x-', label='Without Memoryview')
plt.plot(l2, 'o--', label='With Memoryview')
plt.xlabel('Size of Bytearray')
plt.ylabel('Time (s)')
plt.legend()
plt.show()