class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        
        item_graph = [[] for _ in range(n)]
        item_indegree = [0] * n
        
        group_graph = [[] for _ in range(m)]
        group_indegree = [0] * m
        
        for i in range(n):
            for before in beforeItems[i]:
                item_graph[before].append(i)
                item_indegree[i] += 1
                
                if group[before] != group[i]:
                    group_graph[group[before]].append(group[i])
                    group_indegree[group[i]] += 1
        
        def topo_sort(graph, indegree):
            queue = deque()
            
            for i in range(len(indegree)):
                if indegree[i] == 0:
                    queue.append(i)
            
            result = []
            
            while queue:
                node = queue.popleft()
                result.append(node)
                
                for nei in graph[node]:
                    indegree[nei] -= 1
                    
                    if indegree[nei] == 0:
                        queue.append(nei)
            
            if len(result) != len(graph):
                return []
            
            return result
        
        group_order = topo_sort(group_graph, group_indegree)
        
        if not group_order:
            return []
        
        item_order = topo_sort(item_graph, item_indegree)
        
        if not item_order:
            return []
        
        groups = [[] for _ in range(m)]
        
        for item in item_order:
            groups[group[item]].append(item)
        
        result = []
        
        for g in group_order:
            result.extend(groups[g])
        
        return result