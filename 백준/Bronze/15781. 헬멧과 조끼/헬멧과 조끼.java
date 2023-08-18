import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        long[] head = new long[n];
        long[] wear = new long[m];

        for(int i=0; i<n; i++) head[i] = sc.nextLong();
        for(int i=0; i<m; i++) wear[i] = sc.nextLong();

        Arrays.sort(head);
        Arrays.sort(wear);

        System.out.println(head[n-1]+wear[m-1]);
    }
}