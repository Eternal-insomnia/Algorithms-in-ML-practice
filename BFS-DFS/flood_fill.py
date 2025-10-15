class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image) # rows
        n = len(image[0]) # cols
        start_color = image[sr][sc]
        queue = [f"{sr}.{sc}"]
        visited = set()
        while len(queue) > 0:
            if queue[0] in visited:
                del queue[0]
                continue
            sr = int(queue[0].split('.')[0])
            sc = int(queue[0].split('.')[1])
            value = image[sr][sc]
            if value == start_color:
                image[sr][sc] = color
                # Up element
                if sr - 1 >= 0 and image[sr-1][sc] == start_color and f"{sr-1}.{sc}" not in visited:
                    queue.append(f"{sr-1}.{sc}")
                # Right element
                if sc + 1 < len(image[sr]) and image[sr][sc+1] == start_color and f"{sr}.{sc+1}" not in visited:
                    queue.append(f"{sr}.{sc+1}")
                # Down element
                if sr + 1 < len(image) and image[sr+1][sc] == start_color and f"{sr+1}.{sc}" not in visited:
                    queue.append(f"{sr+1}.{sc}")
                # Left element
                if sc - 1 >= 0 and image[sr][sc-1] == start_color and f"{sr}.{sc-1}" not in visited:
                    queue.append(f"{sr}.{sc-1}")
            visited.add(queue[0])
            del queue[0]
        return image
