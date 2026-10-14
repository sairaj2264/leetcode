class Solution:
    def makeConnected(self, n: int, connections: list[list[int]]) -> int:
        size = [1] * n
        parent = [0] * n
        edges = len(connections)
        if (n - 1) > edges:
            return -1
        for i in range(0 ,n):
            parent[i] = i

        def find_parent(a):
            if parent[a] == a:
                return a
            temp = find_parent(parent[a])
            parent[a] = temp
            return temp
        def union_by_size(a,b):
            a_parent = find_parent(a)
            b_parent = find_parent(b)
            if a_parent == b_parent:
                return
            a_size = size[a_parent]
            b_size = size[b_parent]

            if a_size > b_size:
                parent[b_parent] = a_parent
                size[a_parent] += size[b_parent]
            
            elif a_size == b_size:
                parent[b_parent] = a_parent
            
            else:
                parent[a_parent] = b_parent
                size[b_parent] += size[a_parent]
        
        for a,b in connections:
            union_by_size(a,b)
        
        unique_parents = set()
        for i in range (0 ,n):
            unique_parents.add(find_parent(i))

        answer = len(unique_parents) - 1
        return answer


                    
