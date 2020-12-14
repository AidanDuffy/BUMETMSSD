import java.util.HashMap;
import java.util.Objects;

/**
 * This class is for a singular Edge within the larger graph.
 * It contains the two Nodes that make up the edge and the weight of the edge.
 */
public class Edge {

    //This is the weight of the edge.
    private int weight;
    //These are the two Nodes that make up the edge.
    private Node nodeOne;
    private Node nodeTwo;

    /**
     * This constructs an edge with two empty nodes and a weight of -1, which
     * signals an empty Edge.
     */
    public Edge() {
        this.nodeOne = new Node();
        this.nodeTwo = new Node();
        this.weight = -1;
    }

    /**
     * This constructs a fully populated Edge.
     *
     * @param one    is the first of the two given nodes.
     * @param two    is the second of the two given nodes.
     * @param weight is the weight of the two nodes.
     */
    public Edge(Node one, Node two, int weight) {
        this.nodeOne = one;
        this.nodeTwo = two;
        this.weight = weight;
    }

    /**
     * This gets the weight of this edge.
     *
     * @return the weight of this specific edge.
     */
    public int getWeight() {
        return weight;
    }

    /**
     * This sets the weight of this edge.
     *
     * @param weight is the new weight of this edge.
     */
    public void setWeight(int weight) {
        this.weight = weight;
    }

    /**
     * This returns one of the two nodes. Inaccessible since the user should
     * only need both at once, see getNodes().
     *
     * @return the node marked as nodeOne.
     */
    private Node getNodeOne() {
        return nodeOne;
    }

    /**
     * This sets one of the two nodes. This is inaccessible to the user because
     * the user should only need to set both at one time. See: setNodes
     *
     * @param nodeOne is one of the given nodes.
     */
    private void setNodeOne(Node nodeOne) {
        this.nodeOne = nodeOne;
    }

    /**
     * This returns one of the two nodes. Inaccessible since the user should
     * only need both at once, see getNodes().
     *
     * @return the node marked as nodeTwo.
     */
    private Node getNodeTwo() {
        return nodeTwo;
    }

    /**
     * This sets one of the two nodes. This is inaccessible to the user because
     * the user should only need to set both at one time. See: setNodes
     *
     * @param nodeTwo is one of the given nodes.
     */
    private void setNodeTwo(Node nodeTwo) {
        this.nodeTwo = nodeTwo;
    }

    /**
     * This returns a list of both nodes for the user.
     *
     * @return a Node array of length 2 containing both Nodes of this edge.
     */
    public Node[] getNodes() {
        Node[] nodes = new Node[2];
        nodes[0] = getNodeOne();
        nodes[1] = getNodeTwo();
        return nodes;
    }

    /**
     * This sets both nodes for this edge as well as the weight of the edge.
     *
     * @param one is one of the two nodes.
     * @param two is the other of the two nodes.
     * @throws Exception if the two nodes are not neighbors.
     */
    public void setNodes(Node one, Node two) throws Exception {
        if (getWeight() == -1) {
            HashMap<Node, Integer> oneAdj = one.getNeighbors();
            HashMap<Node, Integer> twoAdj = two.getNeighbors();
            if (oneAdj.size() > 0 && oneAdj.containsKey(two)) {
                setWeight(oneAdj.get(two));
            } else if (twoAdj.size() > 0 && twoAdj.containsKey(one)) {
                setWeight(twoAdj.get(one));
            } else
                throw new Exception("These nodes are not neighbors!");
        }
        setNodeOne(one);
        setNodeTwo(two);
    }

    /**
     * This checks if the given edge is made of the two edges.
     *
     * @param one is one of the two nodes.
     * @param two is the other of the two nodes.
     * @return true if this edge consists of the give edges, false otherwise.
     */
    public boolean checkEdge(Node one, Node two) {
        Node[] nodes = this.getNodes();
        if (one.equals(nodes[0]) && two.equals(nodes[1])) {
            return true;
        } else return one.equals(nodes[1]) && two.equals(nodes[0]);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Edge edge = (Edge) o;

        boolean nodeOrderOne = Objects.equals(nodeOne, edge.nodeOne) &&
                Objects.equals(nodeTwo, edge.nodeTwo);
        boolean nodeOrderTwo = Objects.equals(nodeTwo, edge.nodeOne) &&
                Objects.equals(nodeOne, edge.nodeTwo);
        boolean result = (weight == edge.weight) && (nodeOrderOne
                || nodeOrderTwo);
        return result;
    }

    @Override
    public int hashCode() {
        int hash1 = Objects.hash(weight, nodeOne, nodeTwo);
        int hash2 = Objects.hash(weight, nodeTwo, nodeOne);
        return Objects.hash(hash1,hash2);
    }
}
