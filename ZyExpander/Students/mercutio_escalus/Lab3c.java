import java.util.Scanner;

public class Lab3c {
   public static void main (String [] args){
       Scanner scnr = new Scanner(System.in);
       int social = 0;
      
      System.out.println("Enter your favorite social media: enter 1 for Facebook, 2 for Twitter, 3 for Pinterest:");
      social = scnr.nextInt();
      
      if (social == 1) {
         System.out.println("Your favorite social media is Facebook.");
      }
      if (social == 2) {
         System.out.println("Your favorite social media is Twitter.");
      }
      if (social == 3) {
         System.out.println("Your favorite social media is Pinterest.");
      }
      else if ((social > 3) || (social == 0)) {
         System.out.println("Your selection is not known.");
      }
      
   }
}
       