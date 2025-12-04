import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Shubh_03_1 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner in = new Scanner(new File("input/d3.in"));
        int tot = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            // yay O(n^2)
            int max = 0;
            for (int i = 0; i < line.length()-1; i++) {
                for (int j = i+1; j < line.length(); j++) {
                    int s = Integer.parseInt(line.charAt(i) + "" + line.charAt(j));
                    // System.out.println(s);
                    max = Math.max(max, s);
                }
            }
            tot += max;
        }
        System.out.println(tot);
    }
}