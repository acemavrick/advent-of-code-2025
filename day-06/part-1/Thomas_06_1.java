import java.util.*;
import java.io.*;

public class Thomas_06_1 {
    public static void main(String[] args) throws IOException {
        Scanner in =  new Scanner(new File("input.txt")); 

        ArrayList<ArrayList<Long>> hw = new ArrayList<>();
        long total = 0;

        while (in.hasNextLine()) {
            String line = in.nextLine();
            if (in.hasNextLine()) {
                ArrayList<Long> nums = new ArrayList<>();
                Scanner ls = new Scanner(line);
                while (ls.hasNextLong()) {
                    nums.add(ls.nextLong());
                }
                hw.add(nums);
            } else {
                Scanner ls = new Scanner(line);
                int idx = 0;
                while (ls.hasNext()) {
                    String operation = ls.next();
                    if (operation.equals("+")) {
                        long sum = 0;
                        for (int i = 0; i < hw.size(); i++) {
                            sum += hw.get(i).get(idx);
                        }
                        total += sum;
                    } else {
                        long product = 1;
                        for (int i = 0; i < hw.size(); i++) {
                            product *= hw.get(i).get(idx);
                        }
                        total += product;
                    }
                    idx++;
                }
            }
        } 

        System.out.println(total);
    }
}