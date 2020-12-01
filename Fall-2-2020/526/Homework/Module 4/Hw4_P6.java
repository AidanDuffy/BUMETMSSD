

public class Hw4_P6 {

    public static void main(String[] args) {
        System.out.println("HI");
        /**
         * create a HashMap instance myMap
         * create an ArrayList instance myArrayList
         * create a LinkedList instance myLinkedList
         * Repeat the following 10 times and calculate average total insertion time and average total
         * search time for each data structure
         * generate 100,000 random integers in the range [1, 1,000,000] and store them in the
         * array of integers insertKeys[ ]
         * // begin with empty myHap, myArrayList, and myLinkedList each time
         * // Insert keys one at a time but measure only the total time (not individual insert
         * // time)
         * // Use put method for HashMap
         * // Use add method for ArrayList and LinkedList
         * insert all keys in insertKeys [ ] into myMap and measure the total insert time
         * insert all keys in insertKeys [ ] into  myArrayList and measure the total insert time
         * insert all keys in insertKeys [ ] into myLinkedList and measure the total insert time
         * generate 100,000 random integers in the range [1, 2,000,000] and store them in the
         * array searchKeys[ ].
         * // Search keys one at a time but measure only total time (not individual search
         * // time)
         * // Use containsKey method for HashMap
         * // Use contains method for ArrayList and Linked List
         * search myMap for all keys in searchKeys[ ] and measure the total search time
         * search myArrayList for all keys in searchKeys[ ] and measure the total search time
         * search myLinkedList for all keys in searchKeys[ ] and measure the total search time
         * Print your output on the screen using the following format:
         * Number of keys = 100000
         * HashMap average total insert time = xxxxx
         * ArrayList average total insert time = xxxxx
         * LinkedList average total insert time = xxxxx
         * HashMap average total search time = xxxxx
         * ArrayList average total search time = xxxxx
         * LinkedList average total search time = xxxxx
         * You can generate n random integers between 1 and N in the following way:
         * Random r = new Random(System.currentTimeMillis() );
         * for i = 0 to n – 1
         *     a[i] = r.nextInt(N) + 1
         * When you generate random numbers, it is a good practice to reset the seed. When you first create
         * an instance of the Random class, you can pass a seed as an argument, as shown below:
         * Random r = new Random(System.currentTimeMillis());
         * You can pass any long integer as an argument. The above example uses the current time as a
         * seed.
         * Later, when you want to generate another sequence of random numbers using the same Random
         * instance, you can reset the seed as follows:
         *  r.setSeed(System.currentTimeMillis());
         * You can also use the Math.random( ) method. Refer to a Java tutorial or reference manual on
         * how to use this method.
         * We cannot accurately measure the execution time of a code segment. However, we can estimate
         * it by measuring an elapsed time, as shown below:
         *  long startTime, endTime, elapsedTime;
         * startTime = System.currentTimeMillis();
         * // code segment
         * endTime = System.currentTimeMillis();
         * elapsedTime = endTime ‐ startTime;
         * We can use the elapsedTime as an estimate of the execution time of the code segment. 
         */
    }

}