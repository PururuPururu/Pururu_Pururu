import sys
from time import perf_counter

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 88, 44, 33, 66, 98, 123,
       543, 234, 64, 234, 76, 234, 737, 53, 233]

start = perf_counter()
src_gen = (src[i] for i in range(1, len(src)) if src[i] > src[i-1])
print(*src_gen)
print('memory:', sys.getsizeof((src_gen)), 'time:', perf_counter() - start)

start = perf_counter()
src_list_comp = [src[i] for i in range(1, len(src)) if src[i] > src[i-1]]
print(*src_list_comp)
print('memory: ', sys.getsizeof((src_list_comp)), 'time:', perf_counter() - start)

#Опытным путём выяснено, что в большинстве случаев генератор будет занимать меньше памяти,
# а List_comprehension будет предоставлять более быстрый доступ к элементам. 