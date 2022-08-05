import java.io.*;
import java.net.*;
import java.util.Date;

public class Server1 {
	public static void main(String[] args) {
		try {
			while(true) {
				ServerSocket ss = new ServerSocket(7777);
				System.out.println("Server running at port: 7777");
				Socket socket = ss.accept();
				System.out.println("Client connected");

				String today = new Date().toString();

				DataOutputStream output = new DataOutputStream(socket.getOutputStream());
				PrintWriter writer = new PrintWriter(output, true);

				writer.println(today);

				ss.close();
			  }
			}
		catch(Exception e) {
			System.out.println(e);
		}
	}
}
