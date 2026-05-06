class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Build the graph and in-degree map
        adj_list = defaultdict(set)
        in_degree = defaultdict(int)
        all_chars = set("".join(words))
        
        # Initialize in-degree of all characters to 0
        for char in all_chars:
            in_degree[char] = 0
        
        # Step 2: Find all edges (a -> b means a comes before b)
        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]
            min_length = min(len(first_word), len(second_word))
            
            # Compare characters until a difference is found
            for j in range(min_length):
                if first_word[j] != second_word[j]:
                    if second_word[j] not in adj_list[first_word[j]]:
                        adj_list[first_word[j]].add(second_word[j])
                        in_degree[second_word[j]] += 1
                    break
            else:
                # Check if second word is a prefix of the first word
                if len(second_word) < len(first_word):
                    return ""  # Invalid order
            
        # Step 3: Topological Sort using Kahn's Algorithm
        queue = deque([char for char in all_chars if in_degree[char] == 0])
        sorted_order = []
        
        while queue:
            char = queue.popleft()
            sorted_order.append(char)
            
            for neighbor in adj_list[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(sorted_order) != len(all_chars):
            return ""  # There was a cycle or disconnected parts
        
        return "".join(sorted_order)