import java.util.Arrays;
import java.util.Random;

public class SortingComparison {

    /**
     * This is the insertionSort method from our textbook.
     * @param data is the array being sorted.
     */
    public static void insertionSort(int[] data) {
        int n = data.length;
        for (int k = 1; k < n; k++) {
            int cur = data[k];
            int j = k;
            while (j > 0 && data[j - 1] > cur) {
                data[j] = data[j - 1];
                j--;
            }
            data[j] = cur;
        }
    }

    /**
     * This is the textbook's implementation of the merge algorithm.
     * @param S1 is one half of the array.
     * @param S2 is the other half of the array.
     * @param S is the final array.
     */
    public static void merge(int[] S1, int[] S2, int[] S) {
        int i = 0, j = 0;
        while (i + j < S.length) {
            if (j == S2.length || (i < S1.length && Integer.compare(S1[i], S2[j]) < 0))
                S[i+j] = S1[i++];
            else
                S[i+j] = S2[j++];
        }
    }

    /**
     * This is the textbook's mergeSort implementation.
     * @param data is the starting array.
     */
    public static void mergeSort(int[] data) {
        int n = data.length;
        if (n < 2) return;
        int mid = n/2;
        int[] S1 = Arrays.copyOfRange(data,0,mid);
        int[] S2 = Arrays.copyOfRange(data,mid,n);

        mergeSort(S1);
        mergeSort(S2);

        merge(S1,S2,data);
    }

    /**
     * This is the implementation of quicksort from the textbook with a few modifications.
     * @param data is the integer array to be sorted.
     * @param a is the lower bound index.
     * @param b is the upper bound index.
     */
    public static void quickSort(int[] data, int a, int b) {
        if (a >= b) return;
        int left = a;
        int right = b - 1;
        int pivot = data[b];
        int temp;
        while (left <= right) {
            while (left <= right && Integer.compare(data[left], pivot) < 0) {
                left += 1;
            }
            while (left <= right && Integer.compare(data[right], pivot) > 0) {
                right -= 1;
            }
            if (left <= right) {
                temp = data[left];
                data[left] = data[right];
                data[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        temp = data[left];
        data[left] = data[b];
        data[b] = temp;
        quickSort(data, a ,left - 1);
        quickSort(data, left + 1, b);
    }

    /**
     * This is the heap sort implementation from geeks for geeks, the website.
     * @param arr is the integer array.
     */
    public static void heapSort(int arr[])
    {
        int n = arr.length;

        // Build heap (rearrange array)
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);

        // One by one extract an element from heap
        for (int i=n-1; i>=0; i--)
        {
            // Move current root to end
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;

            // call max heapify on the reduced heap
            heapify(arr, i, 0);
        }
    }

    /**
     * This is the heapify method implementation from geeks for geeks.
     * To heapify a subtree rooted with node i which is
     * an index in arr[]. n is size of heap
     * @param arr is the integer array
     * @param n is the heap size
     * @param i is the current node in the array.
     */
    public static void heapify(int arr[], int n, int i)
    {
        int largest = i;  // Initialize largest as root
        int l = 2*i + 1;  // left = 2*i + 1
        int r = 2*i + 2;  // right = 2*i + 2

        // If left child is larger than root
        if (l < n && arr[l] > arr[largest])
            largest = l;

        // If right child is larger than largest so far
        if (r < n && arr[r] > arr[largest])
            largest = r;

        // If largest is not root
        if (largest != i)
        {
            int swap = arr[i];
            arr[i] = arr[largest];
            arr[largest] = swap;

            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }

    public static void main(String[] args) {
        final int SMALLEST_SIZE = 10000;
        long insertionTimes[] = new long[10];
        long mergeTimes[] = new long[10];
        long heapTimes[] = new long[10];
        long quickTimes[] = new long[10];

        int[] numbers;
        int[] data;

        Random r = new Random();
        long startTime = 0;
        long endTime = 0;
        long elapsedTime = 0;

        for (int i = 1; i <= 10; i += 1) {
            numbers = new int[i*SMALLEST_SIZE];
            /**
             * This for loop will generate a new array of random ints.
             */
            r.setSeed(System.currentTimeMillis());
            for (int j = 0; j < i*SMALLEST_SIZE; j += 1) {
                numbers[j] = r.nextInt(1000000) + 1;
            }
            /**
             * This is the insertion sort block.
             */
            data = numbers.clone();
            startTime = System.currentTimeMillis();
            insertionSort(data);
            endTime = System.currentTimeMillis();
            elapsedTime = endTime - startTime;
            insertionTimes[i-1] = elapsedTime;

            /**
             * This is the merge sort block.
             */
            data = numbers.clone();
            startTime = System.currentTimeMillis();
            mergeSort(data);
            endTime = System.currentTimeMillis();
            elapsedTime = endTime - startTime;
            mergeTimes[i-1] = elapsedTime;

            /**
             * This is the quick sort block.
             */
            data = numbers.clone();
            startTime = System.currentTimeMillis();
            quickSort(data,0, data.length-1);
            endTime = System.currentTimeMillis();
            elapsedTime = endTime - startTime;
            quickTimes[i-1] = elapsedTime;

            /**
             * This is the heap sort block.
             */
            data = numbers.clone();
            startTime = System.currentTimeMillis();
            heapSort(data);
            endTime = System.currentTimeMillis();
            elapsedTime = endTime - startTime;
            heapTimes[i-1] = elapsedTime;
        }
        System.out.println("Insertion Sort Times: " + Arrays.toString(insertionTimes));
        System.out.println("Merge Sort Times: " + Arrays.toString(mergeTimes));
        System.out.println("Quick Sort Times: " + Arrays.toString(quickTimes));
        System.out.println("Heap Sort Times: " + Arrays.toString(heapTimes));
    }
}