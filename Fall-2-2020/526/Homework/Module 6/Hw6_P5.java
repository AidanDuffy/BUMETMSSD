import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.Arrays;

public class Hw6_P5 {
    /**
     * 
     * @return
     */
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
        HashMap<String, Integer> nameIndex = new HashMap<>();
        int i = 0;
        for (String name: namesWithFriendsTree.keySet()) {
            nameIndex.put(name, i++);
        }
        Scanner input;
        int option = 0;
        while (option != 3) {
            System.out.print("\nMain Menu\n\nSearch Options:\n1.  Friends of a person\n2.  Friend or not?" +
                    "\n3.  Exit\n\nEnter Option Number: ");
            input = new Scanner(System.in);
            try {
                option = input.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Please enter a valid integer!");
                continue;
            }
            if (option < 1 || option > 3) {
                System.out.print("\nError! Please enter a valid number!");
                input = new Scanner(System.in);
                option = input.nextInt();
                continue;
            } else {
                if (option == 1) {
                    System.out.print("Please enter the name of a person: ");
                    input = new Scanner(System.in);
                    String name = input.next();
                    if (namesWithFriends.containsKey(name)) {
                        String[] optionOneFriends = namesWithFriends.get(name).split(",");
                        for (String buds: optionOneFriends) {
                            System.out.print(buds + " ");
                        }
                        System.out.print("\n");
                    } else {
                        System.out.println("This name is not in the adjacency matrix! Try again...");
                        continue;
                    }
                } else if (option == 2) {
                    System.out.print("Please enter the names of two people, separated by a single space: ");
                    input = new Scanner(System.in);
                    String entry = input.nextLine();
                    String[] names = entry.split(" ");
                    if (!nameIndex.containsKey(names[0]) || !nameIndex.containsKey(names[1])) {
                        System.out.println("One of these names is not in the adjacency matrix! Try again...");
                        continue;
                    }
                    int index1 = nameIndex.get(names[0]);
                    int index2 = nameIndex.get(names[1]);
                    if (friends[index1][index2] == 1) {
                        System.out.println("Yes, " + names[0] + " and " + names[1] + " are friends!");
                    } else {
                        System.out.println("No, " + names[0] + " and " + names[1] + " are not friends.");
                    }
                }
            }
        }
        System.out.println("Exiting...");
    }
}