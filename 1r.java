public class FibonacciRecursive {
    public static long calculateFibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        return calculateFibonacci(n - 1) + calculateFibonacci(n - 2);
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
