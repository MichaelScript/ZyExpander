import java.util.Scanner;

public class Lab3c {
   public static void main (String[] args){
      Scanner scnr = new Scanner(System.in);
      int userChoice = 0;
      
      System.out.println("Enter your favorite social media: enter 1 for Facebook, 2 for Twitter, 3 for Pinterest:");
      userChoice = scnr.nextInt();
      
      if (userChoice < 4) {
         if (userChoice > 0){
            if (userChoice == 1) {
               System.out.println("Your favorite social media is Facebook.");
            }
            else if (userChoice == 2) {
               System.out.println("Your favorite social media is Twitter.");
            }
            else if (userChoice == 3) {
               System.out.println("Your favorite social media is Pinterest.");
            }
         }
         else {
            System.out.println("Your selection is not known.");
         }
      }
      else {
         System.out.println("Your selection is not known.");
      }
      
      return;
   }
}