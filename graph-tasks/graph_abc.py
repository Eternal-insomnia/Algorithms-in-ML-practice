from abc import ABC, abstractmethod
from typing import Dict, List, Tuple


class Graph(ABC):
    """
    Abstract base class for a graph. Stores:
      - vertices: number of vertices (0..n-1)
      - directed: whether the graph is directed
      - weighted: whether the graph is weighted
    """

    def __init__(self, vertices: int, directed: bool = False, weighted: bool = False):
        """Initialize basic graph properties and internal adjacency list.

        Args:
            vertices (int): number of vertices (>=0). Vertices are numbered 0..n-1.
            directed (bool, optional): True if the graph is directed. Defaults to False.
            weighted (bool, optional): True if the graph is weighted. Defaults to False.
        """
        if vertices < 0:
            raise ValueError("vertices must be non-negative")
        self.vertices = vertices
        self.directed = directed
        self.weighted = weighted
        self._adjacency_list: Dict[int, List[Tuple[int, float]]] = {i: [] for i in range(vertices)}

    def _check_vertex(self, v: int) -> None:
        """Helper method to verify vertex index validity.

        Args:
            v (int): Vertex index to validate.
        """
        if not (0 <= v < self.vertices):
            raise IndexError(f"vertex {v} is out of range [0, {self.vertices - 1}]")

    @abstractmethod
    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        """Abstract method for adding an edge (u -> v).

        Args:
            u (int): source vertex
            v (int): target vertex
            weight (float, optional): edge weight; should be ignored (and treated as 1.0)
                                      for unweighted graphs. Defaults to 1.0.

        Requirements:
            - Self-loops (u == v) are not allowed.
        """
        pass


    #   GRAPH REPRESENTATIONS

    def get_adjacency_list(self) -> Dict[int, List[Tuple[int, float]]]:
        """Return the graph as an adjacency list: {v: [(u, weight), ...], ...}.

        Returns:
            Dict[int, List[Tuple[int, float]]]: a copy of the adjacency list where
            each vertex maps to a list of (neighbor, weight) pairs.

        Hints:
            - Build a new dict with new lists of (u, weight) pairs.
            - Sort neighbors by u (and by weight if needed).

        TODO:
            - Implement deep copy construction and sorting of neighbors by vertex id.
        """
        raise NotImplementedError("Adjacency list: implement me")


    def get_adjacency_matrix(self) -> List[List[float]]:
        """Return the adjacency matrix of size n x n (n = number of vertices).

        Returns:
            List[List[float]]: square matrix representation.

        TODO:
            - Implement adjacency matrix construction considering:
                * weighted/unweighted modes
                * no self-loops
        """
        raise NotImplementedError("Adjacency matrix: implement me")


    def get_incidence_matrix(self) -> List[List[int]]:
        """Return the incidence matrix of size n x m (n = vertices, m = edges).

        Column formation rules (each column corresponds to one edge):
            - Directed graph: for edge (u -> v):
                  -1 in row u, +1 in row v.
            - Undirected graph: for edge {u, v}:
                  +1 in row u, +1 in row v.
            - Self-loops are not allowed.
            - Duplicate undirected edges must not be counted twice.
            - Column ordering must be deterministic:
                * Directed: lexicographically by (u, v)
                * Undirected: by (min(u, v), max(u, v))

        Returns:
            List[List[int]]: incidence matrix of size n x m

        TODO:
            - Implement incidence matrix construction following all rules above.
        """
        raise NotImplementedError("Incidence matrix: implement me")