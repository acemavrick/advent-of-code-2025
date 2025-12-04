import java.util.*;
import java.io.*;

public class Thomas_02_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        String input = in.next();
        String[] ranges = input.split(",");

        long sum = 0;

        for (String range : ranges) {
            long a = Long.parseLong(range.split("-")[0]);
            long b = Long.parseLong(range.split("-")[1]);

            for (long i = a; i <= b; i++) {
                String str = Long.toString(i);

                if (str.length() % 2 == 0 && str.substring(0, str.length() / 2).equals(str.substring(str.length() / 2))) {
                    sum += i; 
                }
            }
        }

        System.out.println(sum);
    }
}
