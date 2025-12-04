import java.util.*;
import java.io.*;

public class Thomas_04_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt"));

        ArrayList<String> al = new ArrayList<>();
        while (in.hasNext()) {
            al.add(in.next()); 
        }

        int N = al.size();
        int M = al.get(0).length();

        char[][] grid = new char[N][M];

        for (int i = 0; i < N; i++) {
            grid[i] = al.get(i).toCharArray();
        }

        int[] dx = {0, 1, 0, -1, 1, -1, -1, 1};
        int[] dy = {1, 0, -1, 0, 1, -1, 1, -1};

        int accessible = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (grid[i][j] == '@') {
                    int count = 0;
                    for (int k = 0; k < 8; k++) {
                        int nx = j + dx[k];
                        int ny = i + dy[k];

                        if (nx >= 0 && nx < M && ny >= 0 && ny < N) {
                            if (grid[ny][nx] == '@') {
                                count++;
                            }         
                        }
                    }
                    if (count < 4) {
                        accessible++;
                    }
                }
            }
        }

        System.out.println(accessible);
    }
}