import java.util.*;
import java.io.*;

public class shubh_11_2 {
    // find number of paths from you --> out
    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(new File("input/d11.in"));
        HashMap<String, ArrayList<String>> map = new HashMap<>();
        while (in.hasNext()){
            String[] line = in.nextLine().split(": ");
            String root = line[0];
            ArrayList<String> nodes = new ArrayList<>(List.of(line[1].split(" ")));
            map.put(root, nodes);
        }
        
        HashMap<String, Long> cache = new HashMap<>();
        
        // System.out.println(map);
        HashSet<String> all = cull(map, "out");
        HashSet<String> validFFT = cull(map, "fft");
        HashSet<String> validDAC = cull(map, "dac");
        System.out.println(validFFT);
        System.out.println(validDAC);
        
        cache.clear();
        long svr2fft = dfs(validFFT, map, "svr", "fft", cache);        
        cache.clear();
        long fft2dac = dfs(validDAC, map, "fft", "dac", cache);
        cache.clear();
        long dac2out = dfs(all, map, "dac", "out", cache);
        long way1 = svr2fft * fft2dac * dac2out;
        System.out.println(way1);
        
        cache.clear();
        long svr2dac = dfs(validDAC, map, "svr", "dac", cache);
        cache.clear();
        long dac2fft = dfs(validFFT, map, "dac", "fft", cache);
        cache.clear();
        long fft2out = dfs(all, map, "fft", "out", cache);
        long way2 = svr2dac * dac2fft * fft2out;
        System.out.println(way2);
        System.out.println();
        System.out.println(way1 + way2);
    }
    
    // no cycles btw
    static long dfs(Set<String> valid, HashMap<String, ArrayList<String>> map, String curr, String target, HashMap<String, Long> cache) {
        if (curr.equals(target)) {
            // System.out.println(visited);
            return 1;
       }
        if (cache.containsKey(curr)) return cache.get(curr);
        long count = 0;
        for (String s : map.getOrDefault(curr, new ArrayList<>())){
            if (valid.contains(s)) count += dfs(valid, map, s, target, cache);
        }
        cache.put(curr, count);
        return count;
    }
    
    static HashSet<String> cull(HashMap<String, ArrayList<String>> map, String target) {
        // return a set of nodes that lead TO target
        HashSet<String> out = new HashSet<>();
        out.add(target);
        
        boolean changed = false;
        do {
            changed = false;
            for (String s : map.keySet()){
                if (out.contains(s)) continue;
                ArrayList<String> list = map.get(s);
                
                for (String s2 : list) {
                    if (out.contains(s2)) {
                        out.add(s);
                        changed = true;
                        break;
                    }
                }
            }
        } while (changed);
        
        // out.remove(target);
        
        return out;
    }
}