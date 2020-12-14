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
    }

    /**
     * This constructs a graph with a given list of nodes, map of edges, and
     * current position.
     *
     * @param position is the current position node.
     * @param nodes    is the list of nodes in this graph.
     * @param edges    is the hash map of edges in this graph.
     */
    public Graph(Node position, ArrayList<Node> nodes, ArrayList<Edge> edges) {
        this.position = position;
        this.nodes = nodes;
        this.edges = edges;
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
     * @param graph is the graph that needs edges.
     * @throws Exception if the graph has no vertices setup, which is needed to
     * generate the list of edges.
     */
    public static void generateEdges(Graph graph) throws Exception {
        if (graph.numVertices() == 0) {
            throw new Exception("This graph has not been constructed yet!");
        }
        ArrayList<Node> nodes = graph.vertices();
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

    public Edge getEdge(Graph graph, Node one, Node two) {
        for (Edge edge: graph.edges) {

        }
        return null;
    }
}