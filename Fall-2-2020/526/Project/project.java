import java.io.File;
import java.util.*;

public class project {

    /**
     * This is the first graph traversal algorithm, which bases the next move
     * based on the smallest direct distance to node Z.
     *
     * @param graph   is the actual graph.
     * @param exclude is the list of Nodes to exclude if we are backtracking.
     * @return the next node.
     */
    public static Node algorithmOne(Graph graph, ArrayList<Node> exclude) {
        Node position = graph.getPosition();
        HashMap<Node, Integer> neighbors = position.getNeighbors();
        int minimum_weight = Integer.MAX_VALUE;
        Set<Node> nodes = neighbors.keySet();
        Node next = null;
        for (Node current : nodes) {
            if (current.getDirectDistance() < minimum_weight &&
                    !exclude.contains(current)) {
                minimum_weight = current.getDirectDistance();
                next = current;
            }
        }
        return next;
    }

    /**
     * This is the second graph traversal algorithm, which bases the next move
     * based on the smallest direct distance to node Z plus the weight of the
     * shared edge.
     *
     * @param graph   is the actual graph.
     * @param exclude is the list of Nodes to exclude if we are backtracking.
     * @return the next node.
     */
    public static Node algorithmTwo(Graph graph, ArrayList<Node> exclude) {
        Node position = graph.getPosition();
        HashMap<Node, Integer> neighbors = position.getNeighbors();
        int minimum_weight = Integer.MAX_VALUE;
        Set<Node> nodes = neighbors.keySet();
        Node next = null;
        for (Node current : nodes) {
            if (neighbors.get(current) + current.getDirectDistance() <
                    minimum_weight && !exclude.contains(current)) {
                minimum_weight = neighbors.get(current)
                        + current.getDirectDistance();
                next = current;
            }
        }
        return next;
    }

    /**
     * This is the part of the program where it receives the user input for the
     * starting node to find the best path to node Z.
     *
     * @param characterNode is the HashMap which pairs the character ID with the
     *                      node.
     * @return the character identifier for the starting Node.
     */
    public static char getStartingNode(HashMap<Character, Node> characterNode) {
        Scanner scanner;
        String nodeID;
        while (true) {
            scanner = new Scanner(System.in);
            System.out.print("Enter the starting Node (single capital " +
                    "character): ");
            nodeID = scanner.nextLine();
            if (nodeID.length() == 1) {
                char identifier = nodeID.charAt(0);
                if (Character.isLetter(identifier)) {
                    if (characterNode.containsKey(identifier)) {
                        return identifier;
                    } else {
                        System.out.println("Error: Input was a lowercase " +
                                "letter! Please enter a single capital" +
                                " letter!");
                    }
                } else {
                    System.out.println("Error: Input was not a letter!" +
                            "Please enter a letter!");
                }
            } else {
                System.out.println("Error: Input length is greater than one! " +
                        "Please enter a valid character!");
            }
        }
    }

    public static void runAlgorithm(Graph graph, char identifier,
                                    int algoNumber) {
        System.out.println("Algorithm " + algoNumber + ": \n");
        ArrayList<Character> path = new ArrayList<>();
        LinkedList<Character> shortestPath = new LinkedList<>();
        path.add(identifier);
        shortestPath.add(identifier);
        Node temp = graph.getPosition();
        ArrayList<Node> exclude = new ArrayList<>();
        int length = 0;
        Node next;
        char tmp;
        //Here is the algorithm running...
        while (graph.getPosition().getIdentifier() != 'Z') {
            if (algoNumber == 1) {
                next = algorithmOne(graph, exclude);
            } else {
                next = algorithmTwo(graph, exclude);
            }
            //This is to handle backtracking
            if (path.contains(next.getIdentifier())) {
                if (graph.getPosition().getNeighbors().size() == 1) {
                    shortestPath.remove(shortestPath.size() - 1);
                    exclude.add(graph.getPosition());
                    length -= Node.findWeight(next, graph.getPosition());
                    graph.setPosition(next);
                } else {
                    if (shortestPath.contains(next.getIdentifier())) {
                        length -= graph.getEdge(
                                next,graph.getPosition()).getWeight();
                        shortestPath.remove(shortestPath.size() - 1);
                        exclude.add(graph.getPosition());
                        graph.setPosition(next);
                    } else {
                        exclude.add(next);
                    }
                }
                path.add(next.getIdentifier());
                continue;
            }
            path.add(next.getIdentifier());
            shortestPath.add(next.getIdentifier());
            length += Node.findWeight(next, graph.getPosition());
            graph.setPosition(next);
        }

        System.out.print("\tSequence of all nodes: " + path.get(0));
        for (int i = 1; i < path.size(); i += 1) {
            System.out.print("->" + path.get(i));
        }
        System.out.print("\n\tShortest path: " + shortestPath.get(0));
        for (int i = 1; i < shortestPath.size(); i += 1) {
            System.out.print("->" + shortestPath.get(i));
        }
        System.out.print("\n\tShortest path length: " + length + "\n\n");
    }

    public static void main(String[] args) {
        File direct_distances = new File("direct_distance.txt");
        File graph_file = new File("graph_input.txt");

        HashMap<Character, Node> characterNode = new HashMap();
        Graph graph = new Graph(Graph.constructGraph(graph_file,
                characterNode));
        try {
            Graph.generateEdges(graph);
        } catch (IllegalArgumentException e) {
            System.out.print("The program failed to construct the graph, bad" +
                    "input file.");
            return;
        }
        Node.setDirectDistances(direct_distances, characterNode);

        char identifier = getStartingNode(characterNode);
        graph.setPosition(characterNode.get(identifier));

        System.out.println("");

        runAlgorithm(graph,identifier, 1);
        graph.setPosition(characterNode.get(identifier));
        runAlgorithm(graph,identifier, 2);
    }

}