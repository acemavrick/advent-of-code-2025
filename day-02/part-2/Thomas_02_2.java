import java.util.*;
import java.io.*;

public class Thomas_02_2 {
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
                boolean add = false;

                for (int j = 1; j <= str.length() / 2; j++) {
                    if (str.length() % j == 0) {
                        boolean valid = false;
                        for (int k = j; k < str.length(); k += j) {
                            if (!str.substring(k-j, k).equals(str.substring(k, k+j))) {
                                valid = true;
                            }
                        }
                        if (!valid) add = true;
                    }
                }

                if (add) {
                    sum += i;
                }
            }
        }

        System.out.println(sum);
    }
}
