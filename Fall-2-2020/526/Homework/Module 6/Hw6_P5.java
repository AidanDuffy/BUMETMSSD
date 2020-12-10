import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.Arrays;

public class Hw6_P5 {

    public static HashMap<String,String> initialSetup() {
        File friend_input = new File("friends_input.txt");
        Scanner myReader;
        try {
            myReader = new Scanner(friend_input);
        } catch (FileNotFoundException e) {
            System.out.println("File not found! Try again!");
            return null;
        }
        HashMap<String,String> namesWithFriends = new HashMap<>();
        String[] namesLine = new String[2];
        while (myReader.hasNextLine()) {
            String line = myReader.nextLine();
            namesLine = line.split(", ");
            if(namesWithFriends.containsKey(namesLine[0])) {
                namesWithFriends.put(namesLine[0], namesWithFriends.get(namesLine[0]) + namesLine[1]);
            } else {
                namesWithFriends.put(namesLine[0], namesLine[1]);
            }
            if(namesWithFriends.containsKey(namesLine[1])) {
                namesWithFriends.put(namesLine[1], namesWithFriends.get(namesLine[1]) + "," + namesLine[0]);
            } else {
                namesWithFriends.put(namesLine[1], namesLine[0]);
            }
        }
        return namesWithFriends;
    }

    public static void setupAdjaceny(HashMap<String,String> namesWithFriends, int[][] friends) {
        
    }

    public static void main(String[] args) {
        int[][] friends;
        int numVertices = 0;
        HashMap<String,String> namesWithFriends = initialSetup();
        if (namesWithFriends == null) {
            return;
        } else {
            numVertices = namesWithFriends.size();
            friends = new int[numVertices][numVertices];
            setupAdjaceny(namesWithFriends, friends);
        }
    }
}