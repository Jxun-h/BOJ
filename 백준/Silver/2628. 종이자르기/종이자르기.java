import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int w = sc.nextInt();
        int h = sc.nextInt();
        int n = sc.nextInt();

        ArrayList<Integer> cut0 = new ArrayList<>();
        ArrayList<Integer> cut1 = new ArrayList<>();

        cut0.add(0);
        cut1.add(0);

        for(int i=0; i<n; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();

            if(a==0) cut0.add(b);
            else cut1.add(b);
        }

        Collections.sort(cut0);
        Collections.sort(cut1);

        int[] Length_h = new int[cut0.size()];
        int[] Length_w = new int[cut1.size()];

        for(int i=1; i<cut0.size(); i++){
            Length_h[i - 1] = cut0.get(i) - cut0.get(i-1);
        }
        Length_h[cut0.size() - 1] = h - cut0.get(cut0.size() - 1);

        for(int i=1; i<cut1.size(); i++){
            Length_w[i - 1] = cut1.get(i) - cut1.get(i-1);
        }
        Length_w[cut1.size() - 1] = w - cut1.get(cut1.size() - 1);

        int ans = -1;
        for(int i=0; i<Length_h.length; i++){
            for(int j=0; j<Length_w.length; j++){
                ans = Math.max(ans, Length_h[i] * Length_w[j]);
            }
        }

        System.out.println(ans);
    }
}
