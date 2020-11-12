
import java.util.Arrays;

public class Hw2_P4 {

	public static void reverseFirstN(int[] a, int n) {
		// complete this method
		// write a separate method with additional parameters, if needed
	}
	
	public static void evenBeforeOdd(int[] a) {
		// complete this method
		// write a separate method with additional parameters, if needed
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
