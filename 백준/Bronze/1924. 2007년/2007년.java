import java.time.DayOfWeek;
import java.time.LocalDate;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        LocalDate date = LocalDate.of(2007, x, y);
        DayOfWeek dayOfWeek = date.getDayOfWeek();
        StringBuffer dow = new StringBuffer(dayOfWeek.toString());
        System.out.println(dow.substring(0, 3));
    }
}