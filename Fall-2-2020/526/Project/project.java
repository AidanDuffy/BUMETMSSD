import java.io.*;
import java.util.*;

public class project {

    /**
     * This is the first graph traversal algorithm, which bases the next move based on the
     * smallest direct distance to node Z.
     * @param graph is the actual graph.
     * @param exclude is the Node to exclude if we are backtracking.
     * @return the next node.
     */
    public static Node algorithmOne(Graph graph, Node exclude) {
        Node position = graph.getPosition();
        HashMap<Node, Integer> neighbors = position.getNeighbors();
        int minimum_weight = Integer.MAX_VALUE;
        Set<Node> nodes = neighbors.keySet();
        Node next = null;
        for(Node current: nodes) {
            if (current.getDirectDistance() < minimum_weight && !current.equals(exclude)) {
                minimum_weight = current.getDirectDistance();
                next = current;
            }
        }
        return next;
    }

    /**
     * This is the second graph traversal algorithm, which bases the next move based on the
     * smallest direct distance to node Z plus the weight of the shared edge.
     * @param graph is the actual graph.
     * @param exclude is the Node to exclude if we are backtracking.
     * @return the next node.
     */
    public static Node algorithmTwo(Graph graph, Node exclude) {
        Node position = graph.getPosition();
        HashMap<Node, Integer> neighbors = position.getNeighbors();
        int minimum_weight = Integer.MAX_VALUE;
        Set<Node> nodes = neighbors.keySet();
        Node next = null;
        for(Node current: nodes) {
            if (neighbors.get(current) + current.getDirectDistance() < minimum_weight
                    && !current.equals(exclude)) {
                minimum_weight = neighbors.get(current) + current.getDirectDistance();
                next = current;
            }
        }
        return next;
    }

    public static void main(String[] args) {
        File direct_distances = new File("direct_distance.txt");
        File graph_file = new File("graph_input.txt");

        HashMap<Character, Node> characterNode = new HashMap();
        ArrayList<Node> nodes = Graph.constructGraph(graph_file, characterNode);

        Node.setDirectDistances(direct_distances, characterNode);
        Graph graph = new Graph(nodes);

        ArrayList<Character> path = new ArrayList<>();

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the starting Node (single character): ");
        String nodeID = scanner.nextLine();
        if(nodeID.length() == 1) {
            char identifer = nodeID.charAt(0);
            if (Character.isLetter(identifer) && characterNode.containsKey(identifer)) {
                graph.setPosition(characterNode.get(identifer));
                path.add(identifer);
            } else {
                System.out.println("Please run again and enter a valid character!");
                return;
            }
        } else {
            System.out.println("Please run again and enter a valid character!");
            return;
        }
        Node temp = graph.getPosition();
        Node exclude = null;
        //Here is algorithm one running...
        while (graph.getPosition().getIdentifier() != 'Z') {
            Node next = algorithmOne(graph,exclude);
            if (path.contains(next.getIdentifier())) {
                path.remove(graph.getPosition().getIdentifier());
                exclude = graph.getPosition();
                graph.setPosition(next);
                continue;
            }
            path.add(next.getIdentifier());
            graph.setPosition(next);
            exclude = null;
        }
        System.out.println(path);
        path = new ArrayList<>();
        path.add(temp.getIdentifier());
        graph.setPosition(temp);
        //Here is algorithm two running...
        while (graph.getPosition().getIdentifier() != 'Z') {
            Node next = algorithmTwo(graph,exclude);
            if (path.contains(next.getIdentifier())) {
                path.remove(graph.getPosition().getIdentifier());
                exclude = graph.getPosition();
                graph.setPosition(next);
                continue;
            }
            path.add(next.getIdentifier());
            graph.setPosition(next);
            exclude = null;
        }
        System.out.println(path);
    }

}