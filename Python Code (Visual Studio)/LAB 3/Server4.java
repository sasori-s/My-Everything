import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class Server4 {
	public static void main(String[] args) {
		try {
			while(true) {
				ServerSocket ss = new ServerSocket(7777);
				System.out.println("Server running at port: 7777");
				Socket socket = ss.accept();
				System.out.println("Client connected");
				
				InputStreamReader input = new InputStreamReader(new DataInputStream(socket.getInputStream()));
				BufferedReader reader = new BufferedReader(input);
				
				DataOutputStream output = new DataOutputStream(socket.getOutputStream());
				PrintWriter writer = new PrintWriter(output, true);
				
				writer.println("Choose any option: 1)add 2) subtract 3) multiply");
				String client_response = reader.readLine();
				
				
				if(client_response.equalsIgnoreCase("1")) {
					writer.println("enter the first number");
					String r1 = reader.readLine();
					writer.println("enter the second number");
					String r2 = reader.readLine();
					int i=Integer.parseInt(r1);  
					int j=Integer.parseInt(r2);
					
					int res = i + j;
					writer.println("The result is = "+ res);
				}
				else if(client_response.equalsIgnoreCase("2")){
					writer.println("enter the first number");
					String r1 = reader.readLine();
					writer.println("enter the second number");
					String r2 = reader.readLine();
					int i=Integer.parseInt(r1);  
					int j=Integer.parseInt(r2);
					
					int res = i - j;
					writer.println("The result is = "+ res);
				}
				else if(client_response.equalsIgnoreCase("3")){
					writer.println("enter the first number");
					String r1 = reader.readLine();
					writer.println("enter the second number");
					String r2 = reader.readLine();
					int i=Integer.parseInt(r1);  
					int j=Integer.parseInt(r2);
					
					int res = i * j;
					writer.println("The result is = "+ res);
				}
				else {
					writer.println("Choose a proper option.");
				}

				writer.println("goodbye");
				ss.close();
			  }
			}
		catch(Exception e) {
			System.out.println(e);
		}
	}
}
