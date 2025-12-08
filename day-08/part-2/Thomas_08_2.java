import java.util.*;
import java.io.*;

public class Thomas_08_2 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input.txt")); 

        ArrayList<double[]> points = new ArrayList<>();

        while (in.hasNext()) {
            String line = in.next();

            double x = Double.parseDouble(line.split(",")[0]);
            double y = Double.parseDouble(line.split(",")[1]);
            double z = Double.parseDouble(line.split(",")[2]);

            points.add(new double[]{x, y, z});
        }

        ArrayList<int[]> pairs = new ArrayList<>();

        for (int i = 0; i < points.size(); i++) {
            for (int j = i+1; j < points.size(); j++) {
                pairs.add(new int[]{i, j});
            }
        }

        Collections.sort(pairs, (int[] a, int[] b) -> {
            double dist_a = Math.pow(points.get(a[0])[0] - points.get(a[1])[0], 2) + Math.pow(points.get(a[0])[1] - points.get(a[1])[1], 2) + Math.pow(points.get(a[0])[2] - points.get(a[1])[2], 2);
            double dist_b = Math.pow(points.get(b[0])[0] - points.get(b[1])[0], 2) + Math.pow(points.get(b[0])[1] - points.get(b[1])[1], 2) + Math.pow(points.get(b[0])[2] - points.get(b[1])[2], 2);
            return Double.compare(dist_a, dist_b);
        });

        UnionFind uf = new UnionFind(points.size());

        for (int i = 0; i < pairs.size(); i++) {
            uf.union(pairs.get(i)[0], pairs.get(i)[1]);
            if (uf.components == 1) {
                System.out.println((long)(points.get(pairs.get(i)[0])[0] * points.get(pairs.get(i)[1])[0]));
                break;
            }
        }
    } 
}

class UnionFind {
    int[] store;
    int[] count;
    int components;

    public UnionFind(int N) {
        store = new int[N];
        count = new int[N];
        components = N;
        Arrays.fill(count, 1);
        for (int i = 0; i < store.length; i++) store[i] = i;
    }

    public int find(int a) {
        if (store[a] == a) return a;
        return find(store[a]);
    }

    public void union(int a, int b) {
        int a_parent = find(a);
        int b_parent = find(b);

        if (a_parent != b_parent) {
            if (count[a_parent] > count[b_parent]) {
                store[b_parent] = a_parent;
                count[a_parent] += count[b_parent];
            } else {
                store[a_parent] = b_parent;
                count[b_parent] += count[a_parent];
            }
            components--;
        }
    }
}
