import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Shubh_01_2 {
    static void main() throws FileNotFoundException {
        Scanner in = new Scanner(new File("day1-2.in"));
        int dial = 50;
        int pwd = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            char a = line.charAt(0);
            int r = Integer.parseInt(line.substring(1));
            // count how many times it hits 0
            if (a == 'R') {
                int fin = dial + r;
                // keep subtracting, counting how many times it overflows- hits 0
                while (fin >= 100) {
                    pwd++;
                    fin -= 100;
                }
                dial = Math.floorMod(dial + r, 100);
                if (fin != dial) throw new RuntimeException();
            } else {
                int fin = dial - r;
                while (fin < 0) {
                    pwd++;
                    fin = 100 + fin;
                }
                dial = Math.floorMod(dial - r, 100);
                if (fin != dial) throw new RuntimeException();
            }
//            if (dial == 0) pwd++;
        }
        System.out.println(pwd);
    }
}
