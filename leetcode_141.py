# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return None

        nodeMap = {}
        nodes = []

        nodes.append(node)
        nodeMap[node] = UndirectedGraphNode(node.label)

        start = 0
        while start < len(nodes):
            tmpNode = nodes[start]
            start += 1
            for neighbor in tmpNode.neighbors:
                if neighbor not in nodeMap:
                    nodes.append(neighbor)
                    nodeMap[neighbor] = UndirectedGraphNode(neighbor.label)

        for tmpNode in nodes:
            tmpNewNode = nodeMap[tmpNode]
            for neighbor in tmpNode.neighbors:
                tmpNewNode.neighbors.append(nodeMap[neighbor])

        return nodeMap[node]
            
        
if __name__ == "__main__":
    s = Solution()
    first = UndirectedGraphNode(-1)
    second = UndirectedGraphNode(1)
    first.neighbors.append(second)
    second.neighbors.append(second)
    result = s.cloneGraph(first)
    print result.neighbors[0].label
