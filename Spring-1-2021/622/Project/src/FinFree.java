import accounts.*;
import users.User;

import java.io.*;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class FinFree {

    static String accountFile = "C:\\Users\\Aidan\\Documents\\BUMETMSSD\\Spring-1-2021\\622\\Project\\resources\\SavedAccounts.txt"; //Ran into issues with this path, will need to resolve in the future.

    public static void main(String[] args) {
        User user = new User("Temporary"); //Eventually, will read owner name from the accounts file first.
        File file = new File(accountFile);
        user.readAccounts(file);
        boolean menu = mainMenu(user);
        if (menu) {
            user.writeAccounts(file);
        }
    }

    public static boolean mainMenu(User user) {
        String name = user.getName();
        String menu = "Welcome to FinFree, " + name + "! Please select from one of the options below" +
                "\n\n\t1.Check monthly net income\n\t2. Check net income year to date\n\t3. Check monthly spending" +
                "\n\t4. Check net worth\n\t5. Check bank account balance\n\t6. Check investment account value" +
                "\n\t7. Check credit card account balance\n\t8. Add a new account\n\t0. Exit";
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println(menu);
            int option = 0;
            try {
                option = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Please enter an integer!");
                continue;
            }
            if (option > 8 || option < 0) {
                System.out.println("Please enter a valid integer!");
                continue;
            } else if (option == 0) {
                return true;
            } else if (option == 5) {
                System.out.println("Your net worth is " + Double.toString(user.getNetWorth()));
                return true;
            } else if (option == 5) {
                System.out.println("Your cash balance in your bank accounts is currently " + Double.toString(user.getNetCash()));
                return true;
            }
        }
    }

}
