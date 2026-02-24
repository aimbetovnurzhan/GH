class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        // int[][] mtrx = new int[n][n];
        // for (int i = 0; i < n; i ++) {
        //     for (int j = 0; j < n; j ++) {
        //         mtrx[i][j] = k;
        //         k ++;
        //     }
        // }
        int i = 0, j = 0;
        for (int k = 0; k < commands.size(); k++) {
            if (commands.get(k).equals("DOWN")) i ++;
            if (commands.get(k).equals("UP")) i --;
            if (commands.get(k).equals("RIGHT")) j ++;
            if (commands.get(k).equals("LEFT")) j --;
        }
        return (i * n) + j;
    }
}