import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AverageFinderTest {
    @Test
    void AverageFinderTestZeroAndNegative() {
        double answer = AverageFinder.findAverage(new String[] {"0", "-2", "1", "5"});
        assertEquals(1, answer);
    }
}