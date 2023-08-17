import java.util.Objects;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while(true){
            int[] arr = new int[26];
            String str = sc.nextLine();
            if (Objects.equals(str, "*")) break;

            for(int i=0; i<str.length(); i++){
               int idx = str.charAt(i) - 97;
               if(idx > -1) arr[idx] += 1;
            }

            boolean flag = true;
            for(int i=0; i<26; i++){
                if(arr[i] == 0) {
                    flag = false;
                    break;
                }
            }

            if(flag) System.out.println("Y");
            else System.out.println("N");
        }
    }
}