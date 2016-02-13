import java.util.Scanner;

   public class Lab3c {
      public static void main (String [] args) {
         Scanner scnr = new Scanner(System.in);
   
         int favMedia = scnr.nextInt();
         System.out.println("Enter your favorite social media: enter 1 for Facebook, 2 for Twitter, 3 for Pinterest:");
         
         switch (favMedia) {
            case 1:
               System.out.println("Your favorite social media is Facebook.");
               break;
            
            case 2:
               System.out.println("Your favorite social media is Twitter.");
               break;
            
            case 3:
               System.out.println("Your favorite social media is Pinterest.");
               break;
               
            default:
               System.out.println("Your selection is not known.");
         }
      }
   }