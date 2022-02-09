src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

src_unique = set()
src_doubles = set()
for src_el in src:
       if src_el not in src_doubles:
              src_unique.add(src_el)
       else:
              src_unique.discard(src_el)
       src_doubles.add(src_el)
print(src_unique)

src_unique_list = [src_el for src_el in src if src_el in src_unique]
print(src_unique_list)