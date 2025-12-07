import java.util.*;
import java.io.*;

public class Thomas_05_2 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt")); 

        ArrayList<long[]> al = new ArrayList<>();

        long count = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            if (line.equals("")) break;
            long a = Long.parseLong(line.split("-")[0]);
            long b = Long.parseLong(line.split("-")[1]);

            count += b - a + 1;
            al.add(new long[]{a, b});
        }

        for (int i = 0; i < al.size(); i++) {
            for (int j = i+1; j < al.size(); j++) {
                long reduce = Math.min(al.get(i)[1], al.get(j)[1]) - Math.max(al.get(i)[0], al.get(j)[0]) + 1;
                if (reduce > 0) {
                    al.get(j)[0] = Math.min(al.get(i)[0], al.get(j)[0]);
                    al.get(j)[1] = Math.max(al.get(i)[1], al.get(j)[1]);
                    count -= reduce;
                    break;
                }
            }
        }

        System.out.println(count);
    } 
}

