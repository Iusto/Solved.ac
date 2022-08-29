import java.util.*;

//첫 번째 줄에 집에서 학교까지의 이동 시간을 나타내는 초가 주어진다.
//두 번째 줄에 학교에서 PC방까지의 이동 시간을 나타내는 초가 주어진다.
//세 번째 줄에 PC방에서 학원까지의 이동 시간을 나타내는 초가 주어진다. 
//마지막 줄에 학원에서 집까지의 이동 시간을 나타내는 초가 주어진다


//총 이동시간 x 분 y 초를 출력한다. 첫 번째 줄에 x를, 두 번째 줄에 y를 출력한다.


public class Main {
		public static void main(String[] args) {
			
			Scanner sc = new Scanner(System.in);
			int [] arr = new int [4];
			int sum = 0;
			
			for (int i = 0; i < 4; i++) {
			arr[i] = sc.nextInt();
			sum += arr[i];
			}
			
			System.out.println(sum/60);
			System.out.println(sum%60);
			
			sc.close();
		}
		
	}