public class calc {

//    package aliya.calculator;

import java.util.stream.DoubleStream;

    public class Calculator {
        public static double add(double... numbers) {
            return DoubleStream.of(numbers)
                    .sum();
        }

        public static double multiply(double... numbers) {
            return DoubleStream.of(numbers)
                    .reduce(1, (a, b) -> a * b);
        }
    }


}
