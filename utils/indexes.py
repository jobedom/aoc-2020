def unique_index_pairs(n):
    for i in range(n):
        for j in range(i + 1, n):
            yield i, j

def unique_index_triplets(n):
    for i in range(n):
        for j in range(i + 1, n):
           for k in range(n):
               if j == k or i == k:
                  continue
               yield i, j, k

