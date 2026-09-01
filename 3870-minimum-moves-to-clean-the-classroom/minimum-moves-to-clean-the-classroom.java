import java.util.*;

class Solution {
    public int minMoves(String[] classroom, int energy) {
        int m = classroom.length;
        int n = classroom[0].length();

        int startR = -1;
        int startC = -1;
        int litterCount = 0;

        // Find starting position and count litter
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                char ch = classroom[i].charAt(j);

                if (ch == 'S') {
                    startR = i;
                    startC = j;
                } else if (ch == 'L') {
                    litterCount++;
                }
            }
        }

        if (litterCount == 0) {
            return 0;
        }

        // Assign an ID to every litter cell
        int[][] litterId = new int[m][n];

        for (int i = 0; i < m; i++) {
            Arrays.fill(litterId[i], -1);
        }

        int id = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (classroom[i].charAt(j) == 'L') {
                    litterId[i][j] = id++;
                }
            }
        }

        int allCollected = (1 << litterCount) - 1;

        /*
         * visited[row][col][mask][energy]
         */
        boolean[][][][] visited =
            new boolean[m][n][1 << litterCount][energy + 1];

        Queue<int[]> queue = new LinkedList<>();

        // row, col, collectedMask, remainingEnergy
        queue.offer(new int[] {
            startR, startC, 0, energy
        });

        visited[startR][startC][0][energy] = true;

        int moves = 0;

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!queue.isEmpty()) {

            int size = queue.size();

            while (size-- > 0) {

                int[] state = queue.poll();

                int r = state[0];
                int c = state[1];
                int mask = state[2];
                int currEnergy = state[3];

                // All litter collected
                if (mask == allCollected) {
                    return moves;
                }

                for (int d = 0; d < 4; d++) {

                    int nr = r + dr[d];
                    int nc = c + dc[d];

                    // Outside grid
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                        continue;
                    }

                    // Cannot pass obstacle
                    if (classroom[nr].charAt(nc) == 'X') {
                        continue;
                    }

                    // Cannot move without energy
                    if (currEnergy == 0) {
                        continue;
                    }

                    int newEnergy = currEnergy - 1;
                    int newMask = mask;

                    char nextCell = classroom[nr].charAt(nc);

                    // Collect litter
                    if (nextCell == 'L') {
                        int litterIndex = litterId[nr][nc];
                        newMask |= (1 << litterIndex);
                    }

                    // Reset energy
                    if (nextCell == 'R') {
                        newEnergy = energy;
                    }

                    if (!visited[nr][nc][newMask][newEnergy]) {

                        visited[nr][nc][newMask][newEnergy] = true;

                        queue.offer(new int[] {
                            nr, nc, newMask, newEnergy
                        });
                    }
                }
            }

            moves++;
        }

        return -1;
    }
}