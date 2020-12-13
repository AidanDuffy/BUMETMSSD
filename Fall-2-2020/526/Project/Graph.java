/**
 * This is the class for the graph which will be traversed by the algorithms.
 */
public class Graph {

    private ArrayList<Node> nodes; //This is just a list of the nodes in this graph.
    private Node position; //This is the current Node in the graph.

    /**
     * This creates an empty list of nodes for the graph and sets the
     * positon to an empty Node.
     */
    public Graph() {
        this.position = new Node();
        this.nodes = new ArrayList<>();
    }

    /**
     * This constructs a graph with a given list of nodes.
     * @param nodes is the list of nodes in this graph.
     */
    public Graph(ArrayList<Node> nodes) {
        this.position = new Node();
        this.nodes = nodes;
    }

    /**
     * This constructs a graph with a given list of nodes with a given current position.
     * @param position is the current position node.
     * @param nodes is the list of nodes in this graph.
     */
    public Graph(Node position, ArrayList<Node> nodes) {
        this.position = position;
        this.nodes = nodes;
    }

    /**
     * This sets the node list to a given array list.
     * @param nodes is the given list of nodes.
     */
    public void setNodes(ArrayList<Node> nodes) {
        this.nodes = nodes;
    }

    /**
     * This returns this graph's list of nodes.
     * @return the graph's list of nodes.
     */
    public ArrayList<Node> getNodes() {
        return nodes;
    }

    /**
     * This sets the current position of this graph to a given node.
     * @param position is the given node which is the current position for this graph.
     */
    public void setPosition(Node position) {
        this.position = position;
    }

    /**
     * This returns this graph's current position Node.
     * @return the graph's current position.
     */
    public Node getPosition() {
        return position;
    }
}