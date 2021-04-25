// Problem Statement: https://algo.monster/problems/nearest_cities

import java.util.*;

public class nearest_cities {

    public static double distance(int x1, int y1, int x2, int y2) {
        return Math.sqrt(Math.pow(Math.abs(x1 - x2), 2) + Math.pow(Math.abs(y1 - y2), 2));
    }

    public static String[] solve(int numOfCities, String[] cities, int[] xCoordinates, int[] yCoordinates,
                                 int numOfQueries, String[] queries) {

        // Create necessary data structures
        String[] output = new String[numOfQueries];
        HashMap<Integer, ArrayList<Integer>> xMap = new HashMap<>();
        HashMap<Integer, ArrayList<Integer>> yMap = new HashMap<>();
        HashMap<String, Integer> cityIndices = new HashMap<>();
        HashMap<String, String> cache = new HashMap<>();

        // Fill x, y, and cityIndices hashmaps
        for (int i = 0; i < numOfCities; ++i) {
            cityIndices.put(cities[i], i);
            ArrayList<Integer> current = new ArrayList<>();
            if (xMap.containsKey(xCoordinates[i])) {
                current = xMap.get(xCoordinates[i]);
            }
            current.add(i);
            xMap.put(xCoordinates[i], current);
            current = new ArrayList<>();
            if (yMap.containsKey(yCoordinates[i])) {
                current = yMap.get(yCoordinates[i]);
            }
            current.add(i);
            yMap.put(yCoordinates[i], current);
        }

        // Compute distances for each query
        for (int i = 0; i < numOfQueries; ++i) {
            // Check the cache
            if (cache.containsKey(queries[i])) {
                output[i] = cache.get(queries[i]);
                continue;
            }

            // Create and load necessary variables
            int cityIndex = cityIndices.get(queries[i]);
            int x = xCoordinates[cityIndex];
            int y = yCoordinates[cityIndex];
            String name = null;
            double smallestDistance = Double.MAX_VALUE;
            List<Integer> currentCities = xMap.get(x);
            currentCities.addAll(yMap.get(y));

            // Linear search on each query within both hashmaps to find the closest city
            if (!currentCities.isEmpty()) {
                for (int c : currentCities) {
                    if (c == cityIndex) {
                        continue;
                    }
                    String currentCity = cities[c];
                    int currentX = xCoordinates[c];
                    int currentY = yCoordinates[c];
                    double currentDistance = distance(x, y, currentX, currentY);
                    if (currentDistance < smallestDistance || (currentDistance == smallestDistance &&
                            currentCity.compareTo(Objects.requireNonNull(name)) < 0)) {
                        smallestDistance = currentDistance;
                        name = currentCity;
                    }
                }
            }
            // Set the output value to the closest city with a common x or y (and null if no such city exists)
            output[i] = name;

            // Cache values in cache for future use
            cache.put(queries[i], name);
        }
        return output;
    }

    public static void main(String[] args) {
        // Test case 1
        int numOfCities = 3;
        String[] cities = {"c1", "c2", "c3"};
        int[] xCoordinates = {3, 2, 1};
        int[] yCoordinates = {3, 2, 3};
        int numOfQueries = 3;
        String[] queries = {"c1", "c2", "c3"};
        String[] expectedOutput = {"c3", null, "c1"};
        String[] result = solve(numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries);
        System.out.println("\nTest Case 1\n");
        System.out.println("Computed Output: " + Arrays.toString(result));
        System.out.println("Expected Output: " + Arrays.toString(expectedOutput));

        // Test case 2
        numOfCities = 5;
        cities = new String[]{"green", "red", "blue", "yellow", "pink"};
        xCoordinates = new int[]{100, 200, 300, 400, 500};
        yCoordinates = new int[]{100, 200, 300, 400, 500};
        numOfQueries = 5;
        queries = new String[]{"green", "red", "blue", "yellow", "pink"};
        expectedOutput = new String[]{null, null, null, null, null};
        result = solve(numOfCities, cities, xCoordinates, yCoordinates, numOfQueries, queries);
        System.out.println("\nTest Case 2\n");
        System.out.println("Computed Output: " + Arrays.toString(result));
        System.out.println("Expected Output: " + Arrays.toString(expectedOutput));
    }
}
