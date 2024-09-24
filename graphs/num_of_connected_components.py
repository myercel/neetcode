"""
Problem No. 323

You have a graph of n nodes. You are given an integer n
and an array edges where edges[i] = [a, b] indicates that 
there is an edge between a and b in the grapph.

Return the number of connected componenets in the graph.

Example 1:
    Input: n = 5, edges = [[0,1], [1,2], [3,4]]
    Output = 2

** Similar to leetcode 547
"""
# Union Find - made to count connected components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        pay = [ i for i in range(n)]
        rank = [1] * n

        def find(n1):
            ans = n1

            while ans != par[ans]:
                par[ans] = par[par[ans]] # path compression
                ans = par[ans]
            return ans

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1

        ans = n
        for n1, n2 in edges:
            ans -= union(n1, n2)
        
        return ans