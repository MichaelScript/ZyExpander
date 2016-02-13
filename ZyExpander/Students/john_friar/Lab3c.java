import java.util.Scanner;
public class Lab3c
{
    public static void main(String[] args)
    {
        int year = 0;
        Scanner scnr = new Scanner(System.in);
        System.out.println("Enter your favorite social media: enter 1 for Facebook, 2 for Twitter, 3 for Pinterest:");
        year= scnr.nextInt();
        if (year==1) 
        {
            System.out.println( "Your favorite social media is Facebook."); 
        }
        else if(year==2)
        {
            System.out.println("Your favorite social media is Twitter.");
        }
        else if(year==3)
        {
             System.out.println("Your favorite social media is Pinterest.");  
        }
        else
        System.out.println("Your selection is not known.");
    }
}