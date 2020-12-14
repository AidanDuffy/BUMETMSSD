import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

/**
 * This class is for a singular Node within the larger graph.
 * It contains an ID, a map of all its neighbors with associated edge weights,
 * and the direct distance to node Z.
 */
public class Node {

    //This is this node's character name, like 'A'.
    private char identifier;
    //This is this node's direct distance to Z.
    private int direct_distance;

    /**
     * This generates an empty Node with an empty HashMap of neighbors;
     */
    public Node() {

    }

    /**
     * This constructs a new Node with a specific ID and an empty list of
     * neighbors.
     *
     * @param identifier is the character that IDs this node.
     */
    public Node(char identifier) {
        this.identifier = identifier;
    }

    /**
     * This constructs a new Node with a specific ID and distance to Z with an
     * empty list of neighbors.
     *
     * @param identifier      is the character that IDs this node.
     * @param direct_distance is this node's direct distance to node Z.
     */
    public Node(char identifier, int direct_distance) {
        this.identifier = identifier;
        this.direct_distance = direct_distance;
    }


    /**
     * This sets the direct distances to node Z of all the nodes in the graph.
     *
     * @param direct_distances is the input text file with all node's direct
     *                         distance to node Z.
     * @param characterNode    is the HashMap which pairs the character ID with
     *                         the node.
     */
    public static void setDirectDistancesFromFile(
            File direct_distances, HashMap<Character, Node> characterNode) {
        try {
            FileReader fr = new FileReader(direct_distances);
            BufferedReader br = new BufferedReader(fr);
            String line;
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
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    /**
     * This returns this node's direct distance to Z.
     *
     * @return this node's direct distance to the destination node Z.
     */
    public int getDirectDistance() {
        return this.direct_distance;
    }

    /**
     * This sets this node's direct distance to the destination node Z.
     *
     * @param direct_distance is the direct distance to Z.
     */
    public void setDirectDistance(int direct_distance) {
        this.direct_distance = direct_distance;
    }

    /**
     * This returns the identifier for this node.
     *
     * @return the ID for this node.
     */
    public char getIdentifier() {
        return identifier;
    }

    /**
     * This will set the ID for this node.
     *
     * @param identifier is the ID of this node.
     */
    public void setIdentifier(char identifier) {
        this.identifier = identifier;
    }
}