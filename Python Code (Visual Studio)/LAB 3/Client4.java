import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client4 {
	public static void main(String[] args) {
		try {
			Socket s = new Socket("localhost",7777);

			InputStreamReader input = new InputStreamReader(new DataInputStream(s.getInputStream()));
			BufferedReader reader = new BufferedReader(input);
			
			DataOutputStream output = new DataOutputStream(s.getOutputStream());
			PrintWriter writer = new PrintWriter(output, true);

			Scanner sc = new Scanner(System.in);
			
			while(true) {
				String response = reader.readLine();
				System.out.println("From server - "+ response);
				if (response.equalsIgnoreCase("goodbye")) {
					break;
				}
				String in = sc.nextLine();
				writer.println(in);	
			}
			
			s.close();
			
		}catch(Exception e) {
			System.out.println(e);
		}
	}
}
