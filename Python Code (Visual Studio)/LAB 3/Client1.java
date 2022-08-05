import java.io.*;
import java.net.*;

public class Client1 {
	public static void main(String[] args) {
		try {
			Socket s = new Socket("localhost",7777);

			InputStreamReader input = new InputStreamReader(new DataInputStream(s.getInputStream()));
			BufferedReader reader = new BufferedReader(input);

			System.out.println("Response = "+ reader.readLine());
			
			s.close();
			
		}catch(Exception e) {
			System.out.println(e);
		}
	}
}
