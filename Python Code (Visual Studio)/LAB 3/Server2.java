import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class Server2 {
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

				while(true) {
					String client_response = reader.readLine();
					if (client_response.equalsIgnoreCase("end game")) {
						writer.println("goodbye");
						break;
					}
					else {
						writer.println(client_response);
					}
								
				}
				ss.close();
			  }
			}
		catch(Exception e) {
			System.out.println(e);
		}
	}
}
