from collections import deque
from typing import List


class CourseSchedule:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        # List to store adjacency list
        adjacency_list = [[] for _ in range(numCourses)]
        # List to store the indegree of every node
        indegrees = [0] * numCourses
        # Populate both adjacency_list and indegrees
        for i in range(numCourses):
            adjacency_list.append([])
        for prerequisite in prerequisites:
            adjacency_list[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1
        # Queue to store nodes with zero indegree
        zero_indegree_nodes = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                zero_indegree_nodes.append(i)
        # Count of courses that one can take
        count = 0
        # Process for all zero indegree nodes
        while len(zero_indegree_nodes) > 0:
            count += 1
            node = zero_indegree_nodes.popleft()
            for neighbor in adjacency_list[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    zero_indegree_nodes.append(neighbor)
        return numCourses == count
