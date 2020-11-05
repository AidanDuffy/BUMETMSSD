import java.sql.SQLOutput;
import java.util.Arrays;

public class Hw1_part1 {
	/**
	 * This method calculates the following information about a given array of integers: the average, minimum, and maximum.
	 * It then prints out that information.
	 * @param numbers is the full array of integers.
	 */
	public static void stats(int[] numbers) {
		int initial = numbers[0];
		double average = initial;
		int min = initial;
		int max = initial;

		// Within this for loop, if a number is larger than the current maximum or smaller than the minimum, those values
		// are replaced.
		for (int i = 1; i < numbers.length; i += 1) {
			if (numbers[i] > max) {
				max = numbers[i];
			} else if (numbers[i] < min) {
				min = numbers[i];
			}
				average += numbers[i]; // The loop sums up the contents of the array for the average.
		}
		average /= numbers.length; // After the for loop, the program divides the sum by the length of the array for the average.
		System.out.printf("average = %.2f, min = %d, max = %d\n", average, min, max);
	}

	/**
	 * This method creates and prints the contents of a subarray constructed from a larger, given array of integers.
	 * @param a is the full integer array.
	 * @param from is the starting index for the subarray.
	 * @param to is the last index for the subarray.
	 */
	public static void subarray(int[] a, int from, int to) {
		// error check w/o using Java's exception handling
		if (from < 0 || to >= a.length) {
			System.out.println("Index out of bound");
			return;
		}

		int[] sub = new int[to - from + 1]; // Adding the one ensures that the array includes a[to].
		sub[0] = a[from]; // The method initializes this first value to allow for the for loop to both create and print the contents of the subarray.
		System.out.print("The subarray, from index " + from + " to index " + to + ", is: " + sub[0]);

		for(int i = from + 1; i <= to; i += 1) {
			sub[i - from] = a[i];
			System.out.print(", " + a[i]);
		}
	}
	
	public static void main(String[] args) {
		
		// test 
		int[] a = {15, 25, 10, 65, 30, 55, 65};

		System.out.println("\nGiven array is: " + Arrays.toString(a));
		stats(a);
		subarray(a, 1, 4);

		// Testing with other arrays
		int[] b = {0,1,2,3,4,5,6,7,8,9};
		System.out.println("\nGiven array is: " + Arrays.toString(b));
		stats(b);
		subarray(b, 5, 10); // Return OOB
		subarray(b, -1, 4); // Return OOB
		subarray(b, 2, 6);

		int[] c = {100, 97, 83, 71, 43};
		System.out.println("\nGiven array is: " + Arrays.toString(c));
		stats(c);
		subarray(c, 0, 2);

		int[] d = {2,2,2};
		System.out.println("\nGiven array is: " + Arrays.toString(d));
		stats(d); //Testing when all three are the same
	}

}
