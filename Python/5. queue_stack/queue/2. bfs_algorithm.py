def BFS(root, target):
    from collections import deque

    queue = deque([root])
    visited = set([root])
    step = 0

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()

            if cur == target:
                return step

            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        step += 1

    return -1