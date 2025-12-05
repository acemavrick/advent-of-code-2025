import java.util.*;
import java.io.*;

public class Thomas_05_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt")); 

        ArrayList<long[]> al = new ArrayList<>();

        while (in.hasNextLine()) {
            String line = in.nextLine();
            if (line.equals("")) break;
            long a = Long.parseLong(line.split("-")[0]);
            long b = Long.parseLong(line.split("-")[1]);

            al.add(new long[]{a, b});
        }

        long count = 0;
        while (in.hasNextLong()) {
            long num = in.nextLong();

            for (long[] range : al) {
                if (num >= range[0] && num <= range[1]) {
                    count++;
                    break;
                }
            }
        }
        System.out.println(count);
    } 
}
