
import java.util.Arrays;

public class Hw2_P4 {
	/**
	 * This is a recursive method which reverses the contents of an int array up to a given index.
	 * @param a is an integer array which will have its contents reversed.
	 * @param n is the last index involved in the reversals
	 */
	public static void reverseFirstN(int[] a, int n) {
		
		return;
	}

	/**
	 * This is a recursive method which rearranges the order of ints stored in a given int array so
	 * that all the even ints come before all of the odd integers.
	 * @param a is the array whose contents are being rearranged.
	 */
	public static void evenBeforeOdd(int[] a) {
		return;
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

	}

}
