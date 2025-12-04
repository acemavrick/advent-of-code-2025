import java.util.*;
import java.io.*;

public class Thomas_03_2 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        long joltage = 0;
        while (in.hasNext()) {
            String bank = in.next();

            long[] arr = new long[bank.length()];
            arr[bank.length()-12] = Long.parseLong(bank.substring(bank.length()-12));

            for (int i = bank.length()-12-1; i >= 0; i--) {
                arr[i] = arr[i+1];
                String test = Long.toString(arr[i]);
                for (int j = 0; j < 12; j++) {
                    arr[i] = Math.max(arr[i], Long.parseLong("" + bank.charAt(i) + test.substring(0, j) + test.substring(j+1)));
                }
            } 

            joltage += arr[0];
        }

        System.out.println(joltage);
    }
}
