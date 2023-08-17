import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String star = "*";
        String sp = " ";
        int n = sc.nextInt();
        int starcnt = 1;

        for(int i=n-1; i>-1; i--){
            StringBuilder Pspace = new StringBuilder("");
            StringBuilder Pstar = new StringBuilder("");
            for(int j=0; j<i; j++){
                Pspace.append(sp);
            }
            for(int j=0;j<starcnt;j++){
                Pstar.append(star);
            }
            System.out.printf("%s%s\n", Pspace, Pstar);
            starcnt += 2;
        }
    }
}