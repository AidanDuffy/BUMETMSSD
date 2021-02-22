import accounts.*;
import users.User;

import java.io.*;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.stream.Stream;

public class FinFree {

    static String accountFile = "C:\\Users\\Aidan\\Documents\\BUMETMSSD\\Spring-1-2021\\622\\Project\\resources\\SavedAccounts.txt"; //Ran into issues with this path, will need to resolve in the future.

    public static void main(String[] args) {
        User user = new User("Temporary"); //Eventually, will read owner name from the accounts file first.
        File file = new File(accountFile);
        user.readAccounts(file);
        boolean menu = Menu.mainMenu(user);
        if (menu) {
            user.writeAccounts(file);
        }
    }

}
