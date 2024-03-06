import static org.junit.Assert.*;

import org.junit.Test;

public class TestApp {
    App app= new App();
    @Test
    public void test_positive()
    {
        assertEquals(4, app.addition(2, 2));
    }
    @Test
    public void test_negative()
    {
        assertEquals(7, app.addition(-16, 23));
    }
}
