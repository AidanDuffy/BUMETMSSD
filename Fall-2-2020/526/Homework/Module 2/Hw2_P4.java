
import java.util.Arrays;

public class Hw2_P4 {
	/**
	 * This is a recursive method which reverses the contents of an int array up to a given index.
	 * @param a is an integer array which will have its contents reversed.
	 * @param n is the number of elements involved in the reversals
	 */
	public static void reverseFirstN(int[] a, int n) {
		reverseFirstN(a, 0, n-1); //Added a helper method that incorporates a "low" variable like we saw in lecture
	}

	/**
	 * This is a recursive method which reverses the contents of an int array up to a given index.
	 * This is very similar to the algorithm discussed in our chapter 5 lecture.
	 * @param a is an integer array which will have its contents reversed.
	 * @param low is the lower bound for reversal.
	 * @param high is the upper bound for the reversal.
	 */
	public static void reverseFirstN(int[] a, int low, int high) {
		if (low < high) {
			int x = a[low];
			a[low++] = a[high];
			a[high--] = x;
			reverseFirstN(a, low, high);
		}
	}

	/**
	 * This is a recursive method which rearranges the order of ints stored in a given int array so
	 * that all the even ints come before all of the odd integers.
	 * @param a is the array whose contents are being rearranged.
	 */
	public static void evenBeforeOdd(int[] a) {
		evenBeforeOdd(a, a.length-1); //Sending to another helper method.
	}

	/**
	 * This is a recursive method which rearranges the order of ints stored in a given int array so
	 * that all the even ints come before all of the odd integers.
	 * @param a is the array whose contents are being rearranged.
	 * @param n is the index that is the last index under examination.
	 */
	public static void evenBeforeOdd(int[] a, int n) {
		if (n == 0) {
			return;
		}
		if (a[n] % 2 == 0) {//We want to move our even numbers to the front
			for(int i = 0; i < n; i += 1) {
				if (a[i] % 2 == 1) { //When we find the first odd value, we swap their positions so evens come first
					int x = a[i]; //Structurally, this section is identical to the method for problem 4.1
					a[i] = a[n];
					a[n--] = x;
					evenBeforeOdd(a, n);
					break;
				}
			}
		} else { //We want to keep the odd values at the end of the array
			evenBeforeOdd(a, n - 1);
		}
	}
	
	public static void main(String[] args) {

		int[] a = new int[10];
		
		for (int i=0; i<a.length; i++) {
			a[i]= (i+1) * 10;
		}
		
		System.out.println("Initial array: ");
		System.out.println(Arrays.toString(a));
		System.out.println();
		
		// make a copy and use it for testing
		int[] intArrayCopy;
		intArrayCopy = a.clone();
		
		int N = 2;
		reverseFirstN(intArrayCopy, N);
		System.out.println("\nAfter reversing first " + N + " elements: ");
		System.out.println(Arrays.toString(intArrayCopy));
		System.out.println();
		
		intArrayCopy = a.clone();
		N = 7;
		reverseFirstN(intArrayCopy, N);
		System.out.println("\nAfter reversing first " + N + " elements: ");
		System.out.println(Arrays.toString(intArrayCopy));
		System.out.println();
		
		int[] b = {10, 15, 20, 30, 25, 35, 40, 45};
		System.out.println("\nBefore rearrange: ");
		System.out.println(Arrays.toString(b));
		System.out.println();
		
		evenBeforeOdd(b);
		System.out.println("\nAfter rearrange: ");
		System.out.println(Arrays.toString(b));
		System.out.println();

		int[] c = {3,5,9,2,4,6};
		System.out.println("\nBefore rearrange: ");
		System.out.println(Arrays.toString(c));
		System.out.println();

		evenBeforeOdd(c);
		System.out.println("\nAfter rearrange: ");
		System.out.println(Arrays.toString(c));
		System.out.println();

	}

}
