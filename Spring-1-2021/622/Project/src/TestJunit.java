import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class TestJunit {
    @Test
    public void testOne() {
        int uno = 1;
        int test = AlwaysReturnsOne.one();
        assertEquals(test, uno);
    }
}
