import java.io.*;

public class project {

    /**
     * This intakes the graph input text file and creates the graph and populates the
     * characterNode hashmap
     * @param graph if the graph input text file.
     * @param characterNode is the HashMap which pairs the character ID with the node.
     */
    public static void constructGraph(File graph, HashMap<Character, Node> characterNode) {
        try {
            FileReader fr = new FileReader(graph);
            BufferedReader br = new BufferedReader(fr);
            String line = br.readLine();
            //This first loop creates new empty Nodes, just with a character ID
            for(char letter: line) {
                if (letter == " " || letter == "\n") {
                    continue;
                }
                
            }
            while((line = br.readLine()) != null) {

            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        File direct_distances = new File("direct_distance.txt");
        File graph = new File("graph_input.txt");

        HashMap<Character, Node> characterNode = new HashMap();
        constructGraph(graph, characterNode);
        graph.close();
    }
}