import java.io.*;
import java.util.*;

public class project {

    /**
     * This intakes the graph input text file and creates the graph and populates the
     * characterNode hashmap
     *
     * @param graph         is the graph input text file.
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
            for (char letter : line) {
                if (letter == " " || letter == "\n") {
                    continue;
                }
                Node current = new Node(letter);
                characterNode.put(letter, current);
            }
            Scanner scanner;
            Set<Character> nodeIDs = characterNode.keySet();
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
                            continue;
                        }
                        neighborID = nodeIDs[index++];
                        neighborNode = characterNode.get(neighborID);
                        current_Node.addEdge(neighborNode, weight);
                    }
                }
                nodes.add(current_Node);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * This sets the direct distances to node Z of all the nodes in the graph.
     *
     * @param direct_distances is the input text file with all node's direct distance to node Z.
     * @param characterNode    is the HashMap which pairs the character ID with the node.
     */
    public static void setDirectDistances(File direct_distances,
                                          HashMap<Character, Node> characterNode) {
        try {
            FileReader fr = new FileReader(graph_file);
            BufferedReader br = new BufferedReader(fr);
            String line;
            Set<Character> nodeIDs = characterNode.keySet();
            Scanner scanner;
            char identifier;
            Node current_node;
            int distance;
            while ((line = br.readLine()) != null) {
                identifier = line.charAt(0);
                current_node = characterNode.get(identifier);
                scanner = new Scanner(line.substring(1));
                if (scanner.hasNextInt()) {
                    distance = scanner.nextInt();
                    current_node.setDirectDistance(distance);
                }
            }
        }

        public static void main (String[]args){
            File direct_distances = new File("direct_distance.txt");
            File graph_file = new File("graph_input.txt");

            HashMap<Character, Node> characterNode = new HashMap();
            ArrayList<Node> nodes = constructGraph(graph_file, characterNode);
            graph_file.close();
            setDirectDistances(direct_distances, characterNode);
            direct_distances.close();
            Graph graph = new Graph(nodes);
        }
    }