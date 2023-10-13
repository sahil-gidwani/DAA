import java.util.*;

public class MultiThreadedMergeSort {
    private static final int THREAD_THRESHOLD = 4; // Adjust the threshold as needed

    public static void mergeSort(int[] arr) {
        if (arr.length <= THREAD_THRESHOLD) {
            Arrays.sort(arr);
            return;
        }

        int mid = arr.length / 2;
        int[] left = new int[mid];
        int[] right = new int[arr.length - mid];

        System.arraycopy(arr, 0, left, 0, mid);
        System.arraycopy(arr, mid, right, 0, arr.length - mid);

        // Create and start two threads for sorting left and right halves
        Thread leftThread = new Thread(() -> mergeSort(left));
        Thread rightThread = new Thread(() -> mergeSort(right));

        leftThread.start();
        rightThread.start();

        try {
            leftThread.join();
            rightThread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        merge(arr, left, right);
    }

    private static void merge(int[] arr, int[] left, int[] right) {
        int i = 0, j = 0, k = 0;
        while (i < left.length && j < right.length) {
            if (left[i] < right[j]) {
                arr[k++] = left[i++];
            } else {
                arr[k++] = right[j++];
            }
        }

        while (i < left.length) {
            arr[k++] = left[i++];
        }

        while (j < right.length) {
            arr[k++] = right[j++];
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};

        System.out.println("Original array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        mergeSort(arr);

        System.out.println("\nSorted array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}
