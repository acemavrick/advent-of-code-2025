import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Shubh_01_1 {
    static void main() throws FileNotFoundException {
        Scanner in = new Scanner(new File("day1-1.in"));
        int dial = 50;
        int pwd = 0;
        while (in.hasNextLine()) {
            String line = in.nextLine();
            char a = line.charAt(0);
            int r = Integer.parseInt(line.substring(1));
            if (a == 'R') {
                dial = Math.floorMod(dial + r, 100);
            } else {
                dial = Math.floorMod(dial - r, 100);
            }
            if (dial == 0) pwd++;
        }
        System.out.println(pwd);
    }
}
