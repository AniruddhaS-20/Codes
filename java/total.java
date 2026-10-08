import java.util.Scanner;
    public class total{
        public static void main(String[] args) {
            Scanner sc= new Scanner(System.in);
            System.out.println("Enter a number");
            int number=sc.nextInt();
            int total=0;
            while(number!=0){
                total=total+number;
                System.out.println("Enter a Number");
                number=sc.nextInt();
            }
            System.out.println(total);
            sc.close(); 
        }
    }