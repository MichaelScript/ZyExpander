import java.util.*;
public class Lab3c
{
   public static void main(String[] args)
   {
      Scanner scnr = new Scanner(System.in);
      System.out.println("Enter your favorite social media: enter 1 for Facebook, 2 for Twitter, 3 for Pinterest:");
      int media = scnr.nextInt();
      
      if(media == 1)
         System.out.println("Your favorite social media is Facebook.");
      else if(media == 2)
         System.out.println("Your favorite social media is Twitter.");
      else if(media == 3)
         System.out.println("Your favorite social media is Pinterest.");
      else
         System.out.println("Your selection is not known.");
   }
}