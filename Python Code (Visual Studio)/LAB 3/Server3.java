import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Date;

public class Server3 {
	public static void main(String[] args) {
		try {
			while(true) {
				ServerSocket ss = new ServerSocket(7777);
				System.out.println("Server running at port: 7777");
				Socket socket = ss.accept();
				System.out.println("Client connected");

				ServerThread serverThread = new ServerThread(socket);
				serverThread.start();

				ss.close();
			  }
			}
		catch(Exception e) {
			System.out.println(e);
		}
	}
}
