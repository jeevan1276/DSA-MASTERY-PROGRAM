class Solution:
    # Function to find the parent of a node with path compression
    def find(self, x, par):
        if par[x] != x:
            par[x] = self.find(par[x], par)
        return par[x]

    # Function to merge two nodes a and b
    def union_(self, a, b, par, rank1):
        rootA = self.find(a, par)
        rootB = self.find(b, par)

        if rootA == rootB:
            return

        # Union by rank
        if rank1[rootA] < rank1[rootB]:
            par[rootA] = rootB
        elif rank1[rootA] > rank1[rootB]:
            par[rootB] = rootA
        else:
            par[rootB] = rootA
            rank1[rootA] += 1

    # Function to check whether 2 nodes are connected or not
    def isConnected(self, x, y, par, rank1):
        return int(self.find(x, par) == self.find(y, par))

