import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

/**
 * This is the class for the graph which will be traversed by the algorithms.
 */
public class Graph {

    //This is a list of the nodes (vertices) in this graph.
    private ArrayList<Node> nodes;
    //This is a list of all edges in the graph
    private ArrayList<Edge> edges;
    //This is a HashMap of all the nodes mapped to a list of all its edges.
    private HashMap<Node, ArrayList<Edge>> nodesWithEdges;
    //This is the current Node in the graph.
    private Node position;

    /**
     * This creates an empty list of nodes and map of edges for the graph and
     * sets the positon to an empty Node.
     */
    public Graph() {
        this.position = new Node();
        this.nodes = new ArrayList<>();
        this.edges = new ArrayList<>();
        this.nodesWithEdges = new HashMap<>();
    }

    /**
     * This constructs a graph with a given list of nodes.
     *
     * @param nodes is the list of nodes in this graph.
     */
    public Graph(ArrayList<Node> nodes) {
        this.position = new Node();
        this.edges = new ArrayList<>();
        this.nodes = nodes;
        this.nodesWithEdges = new HashMap<>();
    }

    /**
     * This constructs a graph with a given list of nodes with a given current
     * position.
     *
     * @param position is the current position node.
     * @param nodes    is the list of nodes in this graph.
     */
    public Graph(Node position, ArrayList<Node> nodes) {
        this.position = position;
        this.nodes = nodes;
        this.edges = new ArrayList<>();
        this.nodesWithEdges = new HashMap<>();
    }

    /**
     * This constructs a graph with a given list of nodes, list of edges, and
     * current position.
     *
     * @param position is the current position node.
     * @param nodes    is the list of nodes in this graph.
     * @param edges    is the list of edges in this graph.
     */
    public Graph(Node position, ArrayList<Node> nodes, ArrayList<Edge> edges) {
        this.position = position;
        this.nodes = nodes;
        this.edges = edges;
        this.nodesWithEdges = new HashMap<>();
    }

    /**
     * This constructs a graph with a given list of nodes, list of edges, map of
     * nodes mapped to a list of their edges, and the current position.
     *
     * @param position       is the current position node.
     * @param nodes          is the list of nodes in this graph.
     * @param edges          is the list of edges in this graph.
     * @param nodesWithEdges is map of nodes mapped to a list
     *                       of their edges.
     */
    public Graph(Node position, ArrayList<Node> nodes, ArrayList<Edge> edges,
                 HashMap<Node, ArrayList<Edge>> nodesWithEdges) {
        this.position = position;
        this.nodes = nodes;
        this.edges = edges;
        this.nodesWithEdges = nodesWithEdges;
    }

    /**
     * This intakes the graph input text file and creates the graph and
     * populates the characterNode hashmap
     *
     * @param graph_file    is the graph input text file.
     * @param characterNode is the HashMap which pairs the character ID with the
     *                      node.
     * @return this returns the array list of all nodes for graph constructor.
     */
    public static ArrayList<Node> constructGraph(
            File graph_file, HashMap<Character, Node> characterNode) {
        ArrayList<Node> nodes = new ArrayList<>();
        try {
            FileReader fr = new FileReader(graph_file);
            BufferedReader br = new BufferedReader(fr);
            String line = br.readLine();
            //This first loop creates new empty Nodes, just with a character ID
            for (int i = 0; i < line.length(); i += 1) {
                char letter = line.charAt(i);
                if (letter == ' ' || letter == '\n') {
                    continue;
                }
                Node current = new Node(letter);
                characterNode.put(letter, current);
            }
            Scanner scanner;
            Set<Character> nodeIDs = characterNode.keySet();
            ArrayList<Character> nodeIDsArrayList = new ArrayList<>(nodeIDs);
            int index;
            char neighborID;
            Node neighborNode;
            int weight;
            char current_letter;
            Node current_Node;

            while ((line = br.readLine()) != null) {
                current_letter = line.charAt(0);
                current_Node = characterNode.get(current_letter);
                scanner = new Scanner(line.substring(1));
                index = 0;
                while (scanner.hasNext()) {
                    if (scanner.hasNextInt()) {
                        weight = scanner.nextInt();
                        if (weight == 0) {
                            index += 1;
                            continue;
                        }
                        neighborID = nodeIDsArrayList.get(index++);
                        neighborNode = characterNode.get(neighborID);
                        current_Node.addEdge(neighborNode, weight);
                    }
                }
                nodes.add(current_Node);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
        return nodes;
    }

    /**
     * After running the graph construction method, run this to create the edge
     * list for this graph.
     *
     * @throws Exception if the graph has no vertices setup, which is needed to
     *                   generate the list of edges.
     */
    public static void generateEdges(Graph graph) throws
            IllegalArgumentException {
        if (graph.numVertices() == 0) {
            throw new IllegalArgumentException("This graph has not been " +
                    "constructed yet!");
        }
        ArrayList<Node> nodes = graph.vertices();
        HashMap<Node,ArrayList<Edge>> nodesWithEdges =graph.getNodesWithEdges();
        HashMap<Node, Integer> nodeNeighbors;
        ArrayList<Edge> nodesEdges;
        Edge edge;
        Node nodeOne, nodeTwo;
        for (int i = 0; i < graph.numVertices(); i += 1) {
            nodeOne = nodes.get(i);
            nodeNeighbors = nodeOne.getNeighbors();
            for (int j = i + 1; j < graph.numVertices(); j += 1) {
                nodeTwo = nodes.get(j);
                if(nodeNeighbors.containsKey(nodeTwo)) {
                    edge = new Edge(nodeOne, nodeTwo,
                            nodeNeighbors.get(nodeTwo));
                    if (graph.edgeNotAdded(nodeOne, edge)) {
                        graph.insertEdge(edge);
                    }
                }
            }
        }

    }

    /**
     * This inserts a given edge into the graph's list of edges and the map
     * of nodes:list of edges
     * @param edge is the given edge that will be added.
     */
    public void insertEdge(Edge edge) {
        ArrayList<Edge> edges = this.edges();
        HashMap<Node,ArrayList<Edge>> nodesWithEdges = this.getNodesWithEdges();
        edges.add(edge);
        this.setEdges(edges);
        Node[] edgeNodes = edge.getNodes();
        for(Node node: edgeNodes) {
            edges = this.getNodesEdgeList(node);
            edges.add(edge);
            nodesWithEdges.put(node,edges);
        }
        this.setNodesWithEdges(nodesWithEdges);
    }

    /**
     * This returns if the graph has already accounted for the given edge.
     * @param node is the node the edge comes from.
     * @param edge is the given edge.
     * @return true if the edge has not been accounted for, false otherwise
     */
    public boolean edgeNotAdded(Node node, Edge edge) {
        ArrayList<Edge> edges = getNodesEdgeList(node);
        if (edges == null) {
            return true;
        } else {
            return (!edges.contains(edge));
        }
    }

    /**
     * This sets the node list to a given array list.
     *
     * @param nodes is the given list of nodes.
     */
    public void setNodes(ArrayList<Node> nodes) {
        this.nodes = nodes;
    }

    /**
     * This returns this graph's current position Node.
     *
     * @return the graph's current position.
     */
    public Node getPosition() {
        return position;
    }

    /**
     * This sets the current position of this graph to a given node.
     *
     * @param position is the given node which is the current position for this
     *                 graph.
     */
    public void setPosition(Node position) {
        this.position = position;
    }

    /**
     * This returns the number of vertices in this graph.
     *
     * @return number of vertices in the graph as an integer.
     */
    public int numVertices() {
        return this.nodes.size();
    }

    /**
     * This retrieves the map of this graph's nodes mapped to edges.
     * @return the map of the graph's nodes:list of edges.
     */
    public HashMap<Node, ArrayList<Edge>> getNodesWithEdges() {
        return nodesWithEdges;
    }

    /**
     * This sets the graphs map of nodes mapped to edges.
     * @param nodesWithEdges the given map.
     */
    public void setNodesWithEdges(HashMap<Node, ArrayList<Edge>>
                                          nodesWithEdges) {
        this.nodesWithEdges = nodesWithEdges;
    }

    /**
     * This returns this graph's list of nodes.
     *
     * @return the graph's list of nodes.
     */
    public ArrayList<Node> vertices() {
        return nodes;
    }

    /**
     * This returns the number of edges in this graph.
     *
     * @return number of edges in the graph as an integer.
     */
    public int numEdges() {
        return this.edges.size();
    }

    /**
     * This returns this graph's list of edges.
     *
     * @return the graph's list of edges.
     */
    public ArrayList<Edge> edges() {
        return edges;
    }

    /**
     * This sets the graphs list of edges to a given array list.
     * @param edges the array list of edges.
     */
    public void setEdges(ArrayList<Edge> edges) {
        this.edges = edges;
    }

    /**
     * This checks all the edges for this graph to see if there exists an edge
     * shared between two given nodes.
     *
     * @param one is one of the two nodes.
     * @param two is the other of the two nodes.
     * @return if this edge exists, then it returns the edge, otherwise null.
     */
    public Edge getEdge(Node one, Node two) {
        ArrayList<Edge> edges = getNodesEdgeList(one);
        for (Edge edge : edges) {
            if (edge.checkEdge(one, two)) {
                return edge;
            }
        }
        return null;
    }

    /**
     * This returns a given node's list of edges.
     * @param node is the node
     * @return the list of edges for this node.
     */
    public ArrayList<Edge> getNodesEdgeList(Node node) {
        HashMap<Node, ArrayList<Edge>> nodesWithEdges = getNodesWithEdges();
        if (nodesWithEdges.containsKey(node)) {
            return nodesWithEdges.get(node);
        } else {
            return new ArrayList<Edge>();
        }
    }

}