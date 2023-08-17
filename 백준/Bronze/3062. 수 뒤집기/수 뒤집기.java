import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0; i<n; i++){
            StringBuffer s = new StringBuffer(sc.next());
            String temp1 = s.toString();
            String temp2 = s.reverse().toString();
            String res1 = Integer.toString(Integer.parseInt(temp1) + Integer.parseInt(temp2));
            StringBuffer res2 = new StringBuffer(res1);
            if(res1.equals(res2.reverse().toString())) System.out.println("YES");
            else System.out.println("NO");
        }
    }
}