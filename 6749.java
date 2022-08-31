import java.util.*;

public class Main {
		public static void main(String[] args) {
			
			Scanner sc = new Scanner(System.in);
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			int bet = intabs(a,b);
			
			System.out.print(b+bet);			
			sc.close();
		}

		private static int intabs(int a, int b) {
			int abs = Math.abs(a-b);
			return abs;
		}
		
	}