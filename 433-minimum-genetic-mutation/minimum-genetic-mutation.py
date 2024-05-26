from collections import deque

class Solution:
  def minMutation(self, startGene, endGene, bank):
    
    visited = set()
    queue = deque([(startGene, 0)])  

    while queue:
      gene, level = queue.popleft()
      visited.add(gene)

      if gene == endGene:
        return level

      for i in range(len(gene)):
        for char in ['A', 'C', 'G', 'T']:
          new_gene = gene[:i] + char + gene[i+1:]
          if new_gene in bank and new_gene not in visited:
            queue.append((new_gene, level + 1))

    return -1 

