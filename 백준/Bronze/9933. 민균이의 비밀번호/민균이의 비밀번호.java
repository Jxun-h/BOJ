import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=0; i<n;i++){
            String temp = sc.next();
            list.add(temp);
        }
        boolean flag = false;

        for(int i=0; i<n; i++){
            String str = list.get(i);
            for(int j=0; j<n; j++){
                StringBuffer rstr = new StringBuffer();
                rstr.append(list.get(j));
                rstr.reverse();
                if(str.equals(rstr.toString())) {
                    flag = true;
                    break;
                }
            }
            if(flag){
                int idx = (int) (str.length()/2);
                System.out.printf("%d %s", str.length(), str.charAt(idx));
                break;
            }
        }
    }
}