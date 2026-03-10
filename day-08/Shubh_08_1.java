import java.util.*;
import java.io.*;

public class Shubh_08_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input/d8.in"));
        in.useDelimiter("[,\\s]");
        ArrayList<Box> boxes = new ArrayList<>();
        int count = 0;
        while (in.hasNext()) {
            Box b = new Box(count, in.nextLong(), in.nextLong(), in.nextLong());
            boxes.add(b);
        }

        UF uf = new UF(boxes.size());

        Queue<Edge> q = new PriorityQueue<>(Comparator.comparingDouble(e -> e.dist));
        for (int i = 0; i < boxes.size(); i++) {
            for (int j = i + 1; j < boxes.size(); j++) {
                Edge e = new Edge(i, j, boxes.get(i).dist(boxes.get(j)));
                q.add(e);
            }
        }
        
        int cnt = 0;
        while (cnt < 1000 && !q.isEmpty()) {
            Edge e = q.poll();
            System.out.println(e);
            if (!uf.connected(e.a, e.b)) {
                uf.union(e.a, e.b);
            }
                cnt++;
        }

        TreeSet<Integer> sizes = new TreeSet<>(Comparator.reverseOrder());
        for (int i = 0; i < boxes.size(); i++) {
            sizes.add(uf.sizeof(i));
        }
        System.out.println(sizes);
        System.out.println(sizes.pollFirst()*sizes.pollFirst()*sizes.pollFirst());
    }

    static record Edge(int a, int b, double dist) {
    }

    static record Box(int id, long x, long y, long z) {
        double dist(Box b) {
            return Math.sqrt(Math.pow(x - b.x, 2) + Math.pow(y - b.y, 2) + Math.pow(z - b.z, 2));
        }
    }

    static class UF {
        int[] parent, size;

        UF(int s) {
            parent = new int[s];
            size = new int[s];
            for (int i = 0; i < s; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        int find(int a) {
            if (parent[a] != a) {
                parent[a] = find(parent[a]);
            }
            return parent[a];
        }

        void union(int a, int b) {
            int rootA = find(a);
            int rootB = find(b);
            if (rootA != rootB) {
                // connect max index to min
                if (rootA > rootB) {
                    parent[rootA] = rootB;
                    size[rootB] += size[rootA];
                } else {
                    parent[rootB] = rootA;
                    size[rootA] += size[rootB];
                }
            }
        }

        boolean connected(int a, int b) {
            return find(a) == find(b);
        }

        int sizeof(int a) {
            return size[find(a)];
        }
    }
}