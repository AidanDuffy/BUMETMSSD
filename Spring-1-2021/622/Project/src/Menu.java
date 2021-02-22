import accounts.Account;
import accounts.BankAccount;
import accounts.CreditCardAccount;
import accounts.InvestmentAccount;
import users.User;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.stream.Stream;

public class Menu extends Thread {

    public static boolean bankBalance(User user) {
        ArrayList<Account> banks = user.getAccountsByType(0);
        if (banks.size() > 1) {
            System.out.println("Please select the bank account you'd like to check:");
            int acc = selectAccount(banks);
            System.out.println("The value of that account is " + banks.get(acc).getValue());
        } else if (banks.size() == 1) {
            System.out.println("You have only one bank account with a current balance of " + banks.get(0).getValue());
        } else {
            System.out.println("You have no bank accounts tied to this user!");
        }
        return true;
    }

    public static boolean investmentValue(User user) {
        ArrayList<Account> invest = user.getAccountsByType(2);
        if (invest.size() > 1) {
            System.out.println("Please select the investment account you'd like to check:");
            int acc = selectAccount(invest);
            System.out.println("The value of that account is " + invest.get(acc).getValue());
        } else if (invest.size() == 1) {
            System.out.println("You have only one investment account with a current balance of " + invest.get(0).getValue());
        } else {
            System.out.println("You have no investment accounts tied to this user!");
        }
        return true;
    }

    public static boolean creditDebt(User user) {
        ArrayList<Account> credit = user.getAccountsByType(1);
        if (credit.size() > 1) {
            System.out.println("Please select the credit card account you'd like to check:");
            int acc = selectAccount(credit);
            System.out.println("The value of that account is " + credit.get(acc).getValue());
        } else if (credit.size() == 1) {
            System.out.println("You have only one credit card account with a current balance of " + credit.get(0).getValue());
        } else {
            System.out.println("You have no credit card accounts tied to this user!");
        }
        return true;
    }

    public static boolean addAccount(User user) {
        Scanner scanner = new Scanner(System.in);
        int type = -1;
        try {
            System.out.println("Please enter the account type.");
            type = scanner.nextInt();
        } catch (InputMismatchException e) {
            System.out.println("Please enter an integer!");
            return false;
        }
        System.out.println("Please ensure all of the following is correct before you enter!");
        if (type == 0) {
            String bank = scanner.nextLine();
            System.out.println("Enter 1 for Savings, 2 for Checking, 3 for CD");
            int accType = scanner.nextInt();
            String accTypeStr = "";
            if (accType == 1) {
                accTypeStr = "Savings";
            } else if (accType == 2) {
                accTypeStr = "Checking";
            } else if (accType == 3) {
                accTypeStr = "CD";
            }
            System.out.println("What is the current balance?");
            double balance = scanner.nextDouble();
            System.out.println("What is the interest rate?");
            double rate = scanner.nextDouble();
            System.out.println("What is the account number (enter as an integer, no dashes)?");
            int number = scanner.nextInt();
            BankAccount bankAccount = new BankAccount(bank, accTypeStr, number, balance, rate);
            System.out.println("Added!");
        } else if (type == 1) {
            System.out.println("Enter 1 for a new credit card account (new issuer) and 2 for a new credit card for an existing account.");
            int newType = scanner.nextInt();
            if (newType == 1) {

            } else if (newType == 2) {

            }
        } else if (type == 2) {

        }
        return true;
    }

    public static boolean bankDepositWithdraw(User user, int option) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Account> banks = user.getAccountsByType(0);
        BankAccount bankAccount;
        if (banks.size() > 1) {
            System.out.println("Please select the bank account you'd like to deposit to/withdrawal from:");
            bankAccount = (BankAccount) banks.get(selectAccount(banks));
        } else if (banks.size() == 1) {
            bankAccount = (BankAccount) banks.get(0);
        } else {
            System.out.println("You have no bank accounts tied to this user!");
            return false;
        }
        double amount = 0;
        try {
            System.out.println("Please enter the amount (only positive) you wish to depoist/withdraw");
            amount = scanner.nextDouble();
        } catch (InputMismatchException e) {
            System.out.println("Please enter an integer or double!");
            return false;
        }
        if (option == 9) {
            bankAccount.debit(amount);
        } else {
            bankAccount.credit(amount);
        }
        return true;
    }

    public static boolean creditPurchasePayOff(User user, int option) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Account> credit = user.getAccountsByType(1);
        CreditCardAccount creditAccount;
        if (credit.size() > 1) {
            System.out.println("Please select the credit card account you'd like to deposit to/withdrawal from:");
            creditAccount = (CreditCardAccount) credit.get(selectAccount(credit));
        } else if (credit.size() == 1) {
            creditAccount = (CreditCardAccount) credit.get(0);
        } else {
            System.out.println("You have no credit accounts tied to this user!");
            return false;
        }
        double amount = 0;
        try {
            System.out.println("Please enter the amount (only positive) you wish to pay off/purchase");
            amount = scanner.nextDouble();
        } catch (InputMismatchException e) {
            System.out.println("Please enter an integer or double!");
            return false;
        }
        if (option == 9) {
            creditAccount.debit(amount);
        } else {
            creditAccount.credit(amount);
        }
        return true;
    }

    public static boolean mainMenu(User user) {
        String name = user.getName();
        String worth = "";
        String menu = "Welcome to FinFree, " + name + "! Please select from one of the options below" +
                "\n\n\t1.Check monthly net income\n\t2. Check net income year to date\n\t3. Check monthly spending" +
                "\n\t4. Check bank account balance\n\t5. Check investment account value" +
                "\n\t6. Check credit card account balance\n\t7. Add a new account\n\t8. Bank Deposit\n\t9. Bank Withdrawal" +
                "\n\t10. Pay Off Credit Card Bill\n\t11. Make a Purchase\n\t12. Display all account values\n\t0. Exit\n";
        Scanner scanner = new Scanner(System.in);
        boolean result = false;
        while (true) {
            worth = "Cash: " + String.format("%.2f\nCredit Card Debt: %.2f\nNet Worth: %.2f",user.getNetCash(),user.getNetDebt(),user.getNetWorth());
            System.out.println(worth+"\n\n" + menu);
            int option = 0;
            try {
                option = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Please enter an integer!");
                continue;
            }
            result = false;
            if (option > 12 || option < 0) {
                System.out.println("Please enter a valid integer!");
                continue;
            } else if (option == 0) {
                return true;
            } else if (option == 1) {
                System.out.println("Your monthly income is ");
                result = true;
            } else if (option == 2) {
                System.out.println("Your YTD income is ");
                result = true;
            } else if (option == 3) {
                System.out.println("You have spent ? this month.");
                result = true;
            } else if (option == 4) {
                result = bankBalance(user);
            }else if (option == 5) {
                result = investmentValue(user);
            } else if (option == 6) {
                result = creditDebt(user);
            } else if (option == 7) {
                result = addAccount(user);
            } else if (option == 8 || option == 9) {
                result = bankDepositWithdraw(user, option);
            } else if (option == 10 || option == 11) {
                result = creditPurchasePayOff(user, option);
            } else if (option == 12) {
                String[] str = user.getAllAccountValues();
                Stream<String> stream = Stream.of(str);
                stream.forEach(s -> System.out.printf("%s\n",s));
                System.out.println();
            }
        }
    }

    public static int selectAccount(ArrayList<Account> accounts) {
        int result = 0;
        String name = "";
        for (int i = 1; i <= accounts.size(); i += 1) {
            Account a = accounts.get(i-1);
            if (a instanceof BankAccount) {
                name = ((BankAccount) a).getBank() + " " + ((BankAccount) a).accountType;
            } else if (a instanceof CreditCardAccount) {
                name = ((CreditCardAccount) a).issuer;
            } else if (a instanceof InvestmentAccount) {
                name = ((InvestmentAccount) a).firm + " " + ((InvestmentAccount) a).accountType;
            }
            System.out.println(i + ". " + name);
        }
        Scanner scanner = new Scanner(System.in);
        while (true) {
            try {
                result = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("Please enter an integer!");
                continue;
            }
            if (result < 1 || result > accounts.size()) {
                System.out.println("Please enter a valid integer!");
                continue;
            } else {
                return result;
            }
        }
    }
}
