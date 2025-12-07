import java.util.*;
import java.io.*;

public class Thomas_07_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        ArrayList<char[]> grid = new ArrayList<>();
        while (in.hasNext()) {
            grid.add(in.next().toCharArray());
        }

        int count = 0;
        for (int i = 1; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).length; j++) {
                if (grid.get(i-1)[j] == 'S' || grid.get(i-1)[j] == '|') {
                    if (grid.get(i)[j] == '^') {
                        grid.get(i)[j-1] = '|';
                        grid.get(i)[j+1] = '|';
                        count++;
                    } else {
                        grid.get(i)[j] = '|';
                    }
                }
            }
        }
        System.out.println(count);
    }
}
