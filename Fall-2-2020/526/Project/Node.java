/**
 * This class is for a singular Node within the larger graph.
 * It contains an ID, a map of all its neighbors with associated edge weights, and
 * the direct distance to node Z.
 */
public class Node {

    private char identifier; //This is this node's character name, like 'A'.
    private HashMap<Node,Integer> neighbors; //This is all the adjacent vertecies and the weights of the edge.
    private int direct_distance; //This is this node's direct distance to Z.

    /**
     * This generates an empty Node with an empty HashMap of neighbors;
     */
    public Node() {
        this.neighbors = new HashMap<>();
    }

    /**
     * This constructs a new Node with a specific ID and an empty list of neighbors.
     * @param identifier is the character that IDs this node.
     */
    public Node(char identifier) {
        this.identifier = identifier;
        this.neighbors = new HashMap<>();
    }

    /**
     * This constructs a new Node with a specific ID and distance to Z with an
     * empty list of neighbors.
     * @param identifier is the character that IDs this node.
     * @param direct_distance is this node's direct distance to node Z.
     */
    public Node(char identifier, int direct_distance) {
        this.identifier = identifier;
        this.direct_distance = direct_distance;
        this.neighbors = new HashMap<>();
    }

    /**
     * This constructs a new Node with a specific ID and distance to Z with an
     * empty list of neighbors.
     * @param identifier is the character that IDs this node.
     * @param neighbors is the map of all adjacent vertices to this node, with the value
     *                  being the weight of their shared edge.
     * @param direct_distance is this node's direct distance to node Z.
     */
    public Node(char identifier, HashMap<Node,Integer> neighbors, int direct_distance) {
        this.identifier = identifier;
        this.neighbors = neighbors;
        this.direct_distance = direct_distance;
    }

    /**
     * This adds an edge to this nodes HashMap of neighbors.
     * @param neighbor is the the neighbor Node.
     * @param weight is the weight of the shared edge.
     */
    public void addEdge(Node neightbor, int weight) {
        this.neighbors.put(neightbor,weight);
    }

    /**
     * This sets this node's direct distance to the destination node Z.
     * @param direct_distance is the direct distance to Z.
     */
    public void setDirectDistance(int direct_distance) {
        this.direct_distance = direct_distance;
    }

    /**
     * This returns this node's direct distance to Z.
     * @return this node's direct distance to the destination node Z.
     */
    public int getDirectDistance() {
        return this.direct_distance;
    }

    /**
     * This returns this node's list of neighbors.
     * @return
     */
    public HashMap<Node, Integer> getNeighbors() {
        return neighbors;
    }

    /**
     * This will set the ID for this node.
     * @param identifier is the ID of this node.
     */
    public void setIdentifier(char identifier) {
        this.identifier = identifier;
    }

    /**
     * This returns the identifier for this node.
     * @return the ID for this node.
     */
    public char getIdentifier() {
        return identifier;
    }
}