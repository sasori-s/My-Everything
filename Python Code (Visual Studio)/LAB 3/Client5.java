import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client5 {
	public static void main(String[] args) {
//		String name = "anindya r";
//		String x = "";
//		
//		for(int i = 0; i < name.length(); i++) {
//			int ascii = name.charAt(i);
//			String a = String.valueOf(ascii);
//			x= x + a;
//		}
//		System.out.println(x);
		try {
			Socket s = new Socket("localhost",7777);

			InputStreamReader input = new InputStreamReader(new DataInputStream(s.getInputStream()));
			BufferedReader reader = new BufferedReader(input);
			
			DataOutputStream output = new DataOutputStream(s.getOutputStream());
			PrintWriter writer = new PrintWriter(output, true);

			Scanner sc = new Scanner(System.in);
			while(true) {
				System.out.println("Say something to the server: ");
				String in = sc.nextLine();
				
				writer.println(in);
				String response = reader.readLine();
				System.out.println("From server: "+ response);
				
				if (response.equalsIgnoreCase("goodbye"))
					break;
			}
			
			s.close();
			
		}catch(Exception e) {
			System.out.println(e);
		}
	}
}
