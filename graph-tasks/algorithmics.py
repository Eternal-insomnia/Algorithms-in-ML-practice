from typing import List, Dict
from graph_abc import Graph
from queue import Queue

class GraphAlgorithms:
    """
    A collection of algorithms operating on Graph objects.
    NOTE: all algorithms are left as TODO stubs.
    They must utilize the representation methods implemented in Graph:
      - get_adjacency_list() - MUST be used
      - get_adjacency_matrix() - not required (but can be used for exta credit)
      - get_incidence_matrix() - not required (but can be used for extra credit)
    """

    @staticmethod
    def bfs(graph: Graph, start: int) -> List[int]:
        """
        TODO: Breadth-First Search (BFS) starting from vertex start.

        Implementation steps:
            1) Validate start: ensure 0 <= start < graph.vertices.
               Raise IndexError if invalid.
            2) Obtain the adjacency list: adj = graph.get_adjacency_list().
               It is expected that the neighbors of each vertex are already sorted.
            3) Implement standard BFS:
               - Use a queue (FIFO).
               - Maintain a visited array/list of size n.
               - Process neighbors in ascending order.
            4) Return a list of vertices in the order they are dequeued
               (visit order).

        Args:
            graph (Graph): the graph on which the traversal is performed.
            start (int): the starting vertex.

        Returns:
            List[int]: the order in which vertices are visited by BFS.

        Hints:
            - Use deque from collections for the queue.
            - Mark vertices as visited at the time of enqueueing,
              not when dequeued — this avoids duplicates.
        """

        if start < 0 or start >= graph.vertices:
            raise IndexError("Wrong start vertcie index")
        visited = []
        adj = graph.get_adjacency_list()
        queue = Queue()
        queue.put(start)
        while not queue.empty():
            curr_vertice = queue.get()
            if curr_vertice in visited:
                continue
            for edge in adj[curr_vertice]:
                if edge[0] not in visited:
                    queue.put(edge[0])
                else:
                    continue
            visited.append(curr_vertice)

        return visited

    @staticmethod
    def _go_deeper(adj, stack, visited):
        if stack[-1] in visited:
            del stack[-1]
            return
        else:
            visited.append(stack[-1])
            for edge in adj[stack[-1]]:
                stack.append(edge[0])
                GraphAlgorithms._go_deeper(adj, stack, visited)

    @staticmethod
    def dfs(graph: Graph, start: int) -> List[int]:
        """
        TODO: Depth-First Search (DFS) starting from vertex start.

        Implementation steps:
            1) Validate start: ensure 0 <= start < graph.vertices.
               Raise IndexError if invalid.
            2) Obtain the adjacency list: adj = graph.get_adjacency_list().
               Neighbors should already be sorted in ascending order.
            3) Implement DFS (recursive or iterative with a stack):
               - Mark the vertex as visited upon entering it.
               - Visit neighbors in ascending order.
            4) Return the list of vertices in preorder (first-time visits).

        Args:
            graph (Graph): the graph on which the traversal is performed.
            start (int): the starting vertex.

        Returns:
            List[int]: order of vertices visited by DFS.

        Hints:
            - Recursion is simpler, but watch recursion depth for large graphs.
            - In the iterative version, the order of adding neighbors to the stack
              affects determinism.
        """

        if start < 0 or start >= graph.vertices:
            raise IndexError("Wrong start vertcie index")
        visited = []
        adj = graph.get_adjacency_list()
        stack = []
        stack.append(start)
        while len(stack) > 0:
            GraphAlgorithms._go_deeper(adj, stack, visited)

        return visited

    @staticmethod
    def connected_components(graph: Graph) -> List[List[int]]:
        """
        TODO: Find connected components.

        Implementation steps:
            1) Get adjacency list: adj = graph.get_adjacency_list().
            2) If the graph is undirected:
               - Compute standard connected components.
            3) If the graph is directed:
               - Compute WEAKLY connected components (ignore edge directions).
                 You can build a temporary undirected adjacency list:
                 for each (u -> v), add both u-v and v-u.
            4) Traverse the graph (BFS or DFS) starting from unvisited vertices,
               collecting vertices of each component into a list.
            5) Sort vertices within each component in ascending order.
            6) Sort the list of components by the smallest vertex in each
               (deterministic ordering).

        Args:
            graph (Graph): the graph for which to compute connected components.

        Returns:
            List[List[int]]: list of components; each component is a sorted
            list of vertex indices.

        Hints:
            - Use a shared visited array to prevent revisiting vertices.
            - For directed graphs, build a temporary dict[int, List[int]]
              with symmetric edges, then perform BFS/DFS over it.
        """
        raise NotImplementedError("Connected components: implement me")

    @staticmethod
    def components_with_stats(graph: Graph) -> List[Dict[str, object]]:
        """
        TODO: Return statistics for each connected component.

        Implementation steps:
            1) Obtain components: comps = GraphAlgorithms.connected_components(graph).
            2) For each component, compute:
               - vertices: the sorted list of vertices.
               - node_count: number of vertices.
               - edge_count:
                   * For undirected graphs: count each edge once.
                     You can iterate over adj and only consider pairs (u, v)
                     where u < v.
                   * For directed graphs: count directed edges (u -> v)
                     where both endpoints are in the same component.
               - smallest_vertex: the smallest vertex (vertices[0]).
            3) Return a list of dictionaries (one per component) and SORT it by:
               (-node_count, -edge_count, smallest_vertex)
               i.e., larger components first, then those with more edges,
               then by smallest vertex ascending.

        Result element format:
            {
                "vertices": List[int],
                "node_count": int,
                "edge_count": int,
                "smallest_vertex": int
            }

        Args:
            graph (Graph): the graph for which to compute component statistics.

        Returns:
            List[Dict[str, object]]: sorted list of component statistics.

        Hints:
            - Build a vertex -> component_index mapping for quick lookup.
            - For undirected graphs, use u < v (or a set of pairs) to avoid
              double-counting edges.
        """
        raise NotImplementedError("Components with stats: implement me")
