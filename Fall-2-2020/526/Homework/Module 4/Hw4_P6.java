import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Random;

public class Hw4_P6 {

    public static void main(String[] args) {
        final int NUM_KEYS = 100000; //For all intents and purposes, this is the "N" for any big-Oh analysis.

        HashMap myMap = new HashMap();
        ArrayList myArrayList = new ArrayList();
        LinkedList myLinkedList = new LinkedList();

        long startTime, endTime, elapsedTime;

        Random r = new Random();

        int[] insertKeys = new int[NUM_KEYS];
        int[] searchKeys = new int[NUM_KEYS];

        /**
         * These two double arrays will keep a running average of the insert/search times for the 3 data structures.
         * [0] will be the hash map, [1] will be the array list, and [2] will be the linked list.
         */
        double[] insertTimes = new double[3];
        double[] searchTimes = new double[3];

        for (int i = 0; i < 10; i += 1) {
            r.setSeed(System.currentTimeMillis());
            for (int j = 0; j < NUM_KEYS; j += 1) {
                insertKeys[j] = r.nextInt(1000000) + 1;
                searchKeys[j] = r.nextInt(2000000) + 1;
            }
            /**
             * This outer loop allowed me to keep the code compact and succinct. Otherwise, I would have needed
             * to write the inner for loops six times, two for each type of data structure.
             */
            for (int dataStruct = 0; dataStruct < 3; dataStruct += 1) {
                /**
                 * The following for loop provides an estimate of insert time of 100K elements
                 * into the various data structures.
                 */
                startTime = System.currentTimeMillis();
                for (int h = 0; h < NUM_KEYS; h += 1) {
                    if (dataStruct == 0) { //HashMap
                        myMap.put(insertKeys[h],i);
                    } else if (dataStruct == 1) { //ArrayList
                        myArrayList.add(insertKeys[h]);
                    } else { //LinkedList
                        myLinkedList.add(insertKeys[h]);
                    }

                }
                endTime = System.currentTimeMillis();
                elapsedTime = endTime - startTime;
                insertTimes[dataStruct] = (insertTimes[dataStruct]*i + elapsedTime)/(i+1);
                /**
                 * The following for loop provides an estimate of search time of 100K elements
                 * into the various data structures.
                 */
                startTime = System.currentTimeMillis();
                for (int h = 0; h < NUM_KEYS; h += 1) {
                    if (dataStruct == 0) { //HashMap
                        myMap.containsKey(searchKeys[h]);
                    } else if (dataStruct == 1) { //ArrayList
                        myArrayList.contains(searchKeys[h]);
                    } else { //LinkedList
                        myLinkedList.contains(searchKeys[h]);
                    }

                }
                endTime = System.currentTimeMillis();
                elapsedTime = endTime - startTime;
                searchTimes[dataStruct] = (searchTimes[dataStruct]*i + elapsedTime)/(i+1);
            }
            myMap = new HashMap();
            myArrayList = new ArrayList();
            myLinkedList = new LinkedList();
        }
        /**
         * The rest of the program will be printing out the observations.
         */

        System.out.println("Number of keys = " + String.valueOf(NUM_KEYS) + "\n");
        System.out.println("HashMap average total insert time = " + String.valueOf(insertTimes[0]));
        System.out.println("ArrayList average total insert time = " + String.valueOf(insertTimes[1]));
        System.out.println("LinkedList average total insert time = " + String.valueOf(insertTimes[2]) + "\n");
        System.out.println("HashMap average total search time = " + String.valueOf(searchTimes[0]));
        System.out.println("ArrayList average total search time = " + String.valueOf(searchTimes[1]));
        System.out.println("LinkedList average total search time = " + String.valueOf(searchTimes[2]));
    }

}