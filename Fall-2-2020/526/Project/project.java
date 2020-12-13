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
        ArrayList<Character> shortestPath = new ArrayList<>();

        Scanner scanner;
        String nodeID;
        while (true) {
            scanner = new Scanner(System.in);
            System.out.print("Enter the starting Node (single capital character): ");
            nodeID = scanner.nextLine();
            if (nodeID.length() == 1) {
                char identifer = nodeID.charAt(0);
                if (Character.isLetter(identifer) && characterNode.containsKey(identifer)) {
                    graph.setPosition(characterNode.get(identifer));
                    path.add(identifer);
                    shortestPath.add(identifer);
                    break;
                } else {
                    System.out.println("Please try again and enter a valid character!");
                }
            } else {
                System.out.println("Please try again and enter a valid character!");
            }
        }
        System.out.println("");
        Node temp = graph.getPosition();
        Node exclude = null;
        int length = 0;

        System.out.println("Algorithm 1: \n");
        //Here is algorithm one running...
        while (graph.getPosition().getIdentifier() != 'Z') {
            Node next = algorithmOne(graph,exclude);
            //This is to handle backtracking one node
            if (path.contains(next.getIdentifier())) {
                shortestPath.remove(shortestPath.size() - 1);
                exclude = graph.getPosition();
                path.add(next.getIdentifier());
                length -= Node.findWeight(next,graph.getPosition());
                graph.setPosition(next);
                continue;
            }
            path.add(next.getIdentifier());
            shortestPath.add(next.getIdentifier());
            length += Node.findWeight(next,graph.getPosition());
            graph.setPosition(next);
            exclude = null;
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

        length = 0;
        path = new ArrayList<>();
        shortestPath = new ArrayList<>();
        path.add(temp.getIdentifier());
        shortestPath.add(temp.getIdentifier());
        graph.setPosition(temp);

        System.out.println("Algorithm 2: \n");
        //Here is algorithm two running...
        while (graph.getPosition().getIdentifier() != 'Z') {
            Node next = algorithmTwo(graph,exclude);
            //This is to handle backtracking one node
            if (path.contains(next.getIdentifier())) {
                shortestPath.remove(shortestPath.size() - 1);
                exclude = graph.getPosition();
                path.add(next.getIdentifier());
                length -= Node.findWeight(next,graph.getPosition());
                graph.setPosition(next);
                continue;
            }
            path.add(next.getIdentifier());
            shortestPath.add(next.getIdentifier());
            length += Node.findWeight(next,graph.getPosition());
            graph.setPosition(next);
            exclude = null;
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

}