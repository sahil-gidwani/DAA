public class FibonacciIterative {
    public static long calculateFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        long fibNMinus2 = 0;
        long fibNMinus1 = 1;
        long fibN = 0;
        
        for (int i = 2; i <= n; i++) {
            fibN = fibNMinus1 + fibNMinus2;
            fibNMinus2 = fibNMinus1;
            fibNMinus1 = fibN;
        }
        
        return fibN;
    }

    public static void main(String[] args) {
        int n = 10; // Calculate the 10th Fibonacci number
        long startTime = System.nanoTime();
        long result = calculateFibonacci(n);
        long endTime = System.nanoTime();

        System.out.println("Fibonacci(" + n + ") = " + result);
        System.out.println("Time taken: " + (endTime - startTime) + " nanoseconds");
    }
}
