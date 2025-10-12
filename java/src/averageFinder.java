public class AverageFinder {
    public static void main(String[] args) {
        System.out.println("Average finder");
        double avg = findAverage(args);
        System.out.println("The average is " + avg); // Literally string + string literal
    }

    static double findAverage(String[] input) {
        if (input.length == 0) {
            return 0;
        }

        int result = 0;

        for (String s : input) {
            result += Integer.parseInt(s);
        }

        return result / input.length; // in math you can't divide by 0
    }
}
