import java.io.*;
import java.util.*;

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
     *
     * @param nodes is the list of nodes in this graph.
     */
    public Graph(ArrayList<Node> nodes) {
        this.position = new Node();
        this.nodes = nodes;
    }

    /**
     * This constructs a graph with a given list of nodes with a given current position.
     *
     * @param position is the current position node.
     * @param nodes    is the list of nodes in this graph.
     */
    public Graph(Node position, ArrayList<Node> nodes) {
        this.position = position;
        this.nodes = nodes;
    }

    /**
     * This returns this graph's list of nodes.
     *
     * @return the graph's list of nodes.
     */
    public ArrayList<Node> getNodes() {
        return nodes;
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
     * @param position is the given node which is the current position for this graph.
     */
    public void setPosition(Node position) {
        this.position = position;
    }

    /**
     * This intakes the graph input text file and creates the graph and populates the
     * characterNode hashmap
     *
     * @param graph_file    is the graph input text file.
     * @param characterNode is the HashMap which pairs the character ID with the node.
     * @return this returns the array list of all nodes for graph constructor.
     */
    public static ArrayList<Node> constructGraph(File graph_file,
                                                 HashMap<Character, Node> characterNode) {
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
}