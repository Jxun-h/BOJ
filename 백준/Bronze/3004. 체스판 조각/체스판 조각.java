import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int res = 0;
        if(n % 2 == 0) res = (1 + n / 2) * (1 + n / 2);
        else res = (1 + n / 2) * ((1 + n / 2) + 1);
        System.out.println(res);
    }
}