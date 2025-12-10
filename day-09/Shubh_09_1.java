import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;

public class Shubh_09_1 {
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input/d9.in"));
        ArrayList<Coord> coords = new ArrayList<>();
        in.useDelimiter("[,\\s]");
        while (in.hasNext()) {
            coords.add(new Coord(in.nextLong(), in.nextLong()));
        }
        long maxarea = 0;
        for (int i = 0; i < coords.size()-1; i++) {
            for (int j = i+1; j < coords.size(); j++) {
                long ar = coords.get(i).area(coords.get(j));
                maxarea = Math.max(ar, maxarea);
            }
        }
        System.out.println(maxarea);
    }

    record Coord(long x, long y) {
        long area(Coord r) {
            long maxx = Math.max(x, r.x);
            long maxy = Math.max(y, r.y);
            long minx = Math.min(x, r.x);
            long miny = Math.min(y, r.y);
            return (maxx-minx + 1) * (maxy - miny + 1);
        }
        double distTo(Coord r) {
            return Math.hypot(x - r.x, y - r.y);
        }
    }
}
