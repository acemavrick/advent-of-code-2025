import java.util.*;
import java.io.*;

public class shubh_11_1 {
    // find number of paths from you --> out
    static long ways = 0;
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input/d11.in"));
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        while (in.hasNext()){
            String[] line = in.nextLine().split(": ");
            String root = line[0];
            ArrayList<String> nodes = new ArrayList<>(List.of(line[1].split(" ")));
            map.put(root, nodes);
        }
        // System.out.println(map);
        dfs(map, "you");
        System.out.println(ways);
    }
    
    // no cycles btw
    static void dfs(HashMap<String, ArrayList<String>> map, String curr) {
        if (curr.equals("out")) {
            ways++;
            return;
        }
        for (String s : map.get(curr)){
            dfs(map, s);
        }
    }
}