import java.util.*;
import java.io.*;

public class Thomas_07_2 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        ArrayList<char[]> grid = new ArrayList<>();
        while (in.hasNext()) {
            grid.add(in.next().toCharArray());
        }

        long[][] timelines = new long[grid.size()][grid.get(0).length];

        for (int i = 1; i < grid.size(); i++) {
            for (int j = 0; j < grid.get(i).length; j++) {
                if (grid.get(i-1)[j] == 'S' || grid.get(i-1)[j] == '|') {
                    if (grid.get(i-1)[j] == 'S') {
                        timelines[i-1][j] = 1;
                    }

                    if (grid.get(i)[j] == '^') {
                        grid.get(i)[j-1] = '|';
                        grid.get(i)[j+1] = '|';
                        timelines[i][j-1] += timelines[i-1][j];
                        timelines[i][j+1] += timelines[i-1][j];
                    } else {
                        grid.get(i)[j] = '|';
                        timelines[i][j] += timelines[i-1][j];
                    }
                }
            }
        }

        long sum = 0;
        for (int i = 0; i < timelines[timelines.length-1].length; i++) {
            sum += timelines[timelines.length-1][i];
        }
        System.out.println(sum);
    }
}
