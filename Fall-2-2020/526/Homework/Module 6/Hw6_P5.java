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
                namesWithFriends.put(namesLine[0], namesWithFriends.get(namesLine[0]) + "," +  namesLine[1]);
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

    public static TreeMap<String,String> setupAdjaceny(HashMap<String,String> namesWithFriends, int[][] friends, int numVertices) {
        TreeMap<String,String> namesWithFriendsTree = new TreeMap<>(namesWithFriends);
        HashMap<String, Integer> nameIndex = new HashMap<>();
        int i = 0;
        for (String name: namesWithFriendsTree.keySet()) {
            nameIndex.put(name, i++);
        }
        for (String name: namesWithFriendsTree.keySet()) {
            String cur = namesWithFriends.get(name);
            String[] friendsNames = cur.split(",");
            for (String friend : friendsNames) {
                int friendIndex = nameIndex.get(friend);
                int index = nameIndex.get(name);
                friends[index][friendIndex] = 1;
                friends[friendIndex][index] = 1;
            }
        }
        return namesWithFriendsTree;
    }

    public static void printAdjacenyMatrix(TreeMap<String,String> namesWithFriendsTree, int[][] friends, int numVertices) {
        System.out.print("\t\t");
        for (String name: namesWithFriendsTree.keySet()) {
            String temp = name;
            while (temp.length() < 8) {
                temp += " ";
            }
            System.out.print("| " + temp);
        }
        System.out.print("\n");
        int i = 0;
        for (String name: namesWithFriendsTree.keySet()) {
            String temp = name;
            while (temp.length() < 7) {
                temp += " ";
            }
            System.out.print(temp);
            for (int j = 0; j < numVertices; j += 1) {
                System.out.print(" |    " + friends[i][j] + "   ");
            }
            i += 1;
            System.out.print("\n");
        }
    }

    public static void main(String[] args) {
        int[][] friends;
        int numVertices = 0;
        HashMap<String,String> namesWithFriends = initialSetup();
        if (namesWithFriends == null) {
            return;
        }
        numVertices = namesWithFriends.size();
        friends = new int[numVertices][numVertices];
        TreeMap<String,String> namesWithFriendsTree = setupAdjaceny(namesWithFriends, friends, numVertices);
        printAdjacenyMatrix(namesWithFriendsTree, friends, numVertices);
        System.out.println("friends");
    }
}