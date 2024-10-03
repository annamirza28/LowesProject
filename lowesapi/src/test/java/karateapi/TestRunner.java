package karateapi;

import com.intuit.karate.junit5.Karate;

public class TestRunner {

	 @Karate.Test
	    Karate testSample() {

	        return  Karate.run().relativeTo(getClass());

	    }

}


