import java.util.*;
import java.io.*;

public class Thomas_01_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        int dial = 50;
        int count = 0;

        while (in.hasNext()) {
            String instruction = in.next();
            char direction = instruction.charAt(0);
            int magnitude = Integer.parseInt(instruction.substring(1));

            if (direction == 'L') {
                dial = Math.floorMod(dial - magnitude, 100);
            } else {
                dial = Math.floorMod(dial + magnitude, 100);
            }

            if (dial == 0) {
                count++;
            }
        }

        System.out.println(count);
    }
}