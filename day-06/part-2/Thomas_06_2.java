import java.util.*;
import java.io.*;

public class Thomas_06_2 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt")); 

        ArrayList<String> al = new ArrayList<>();

        int maxLen = 0;

        while (in.hasNextLine()) {
            String line = in.nextLine();
            al.add(line);
            maxLen = Math.max(maxLen, line.length());
        }

        for (int i = 0; i < al.size(); i++) {
            al.set(i, String.format("%-" + maxLen + "s", al.get(i)));
        }

        long total = 0;

        ArrayList<Long> nums = new ArrayList<>();
        for (int i = maxLen-1; i >= 0; i--) {
            String num = "";
            for (int j = 0; j < al.size()-1; j++) {
                char c = al.get(j).charAt(i);
                if (c != ' ') {
                    num += al.get(j).charAt(i);
                }
            }
            nums.add(Long.parseLong(num));

            char operator = al.get(al.size()-1).charAt(i);
            if (operator == '+') {
                long sum = 0;
                for (int j = nums.size()-1; j >= 0; j--) {
                    sum += nums.remove(j);
                }
                total += sum;
            } else if (operator == '*') {
                long product = 1;
                for (int j = nums.size()-1; j >= 0; j--) {
                    product *= nums.remove(j);
                }
                total += product;
            }

            if (operator != ' ') i--;
        }

        System.out.println(total);
    }
    
}
