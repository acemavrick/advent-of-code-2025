import java.util.*;
import java.io.*;

public class Thomas_03_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        int joltage = 0;
        while (in.hasNext()) {
            String bank = in.next();

            int max = 0;
            for (int i = 0; i < bank.length(); i++) {
                for (int j = i+1; j < bank.length(); j++) {
                    max = Math.max(max, (int)(bank.charAt(i)-'0') * 10 + (int)(bank.charAt(j)-'0'));
                }
            } 

            joltage += max;
        }

        System.out.println(joltage);
    }
}