import accounts.*;

import java.io.*;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class FinFree {

    static String accountFile = "C:\\Users\\Aidan\\Documents\\BUMETMSSD\\Spring-1-2021\\622\\Project\\resources\\SavedAccounts.txt"; //Ran into issues with this path, will need to resolve in the future.

    public static void main(String[] args) {
        String owner = "User"; //Eventually, will read owner name from the accounts file first.
        ArrayList<Account> accounts = readAccounts(); // This wll contain all of this user's account objects.
        boolean menu = mainMenu(owner, accounts);
        if (menu) {
            writeAccounts(accounts);
        }
    }

    public static ArrayList<Account> readAccounts() {
        ArrayList<Account> accounts = new ArrayList<>();
        File acc = new File(accountFile);
        String accFileContents = "";
        System.out.println();
        try {
            FileReader reader = new FileReader(acc);
            while(reader.ready()) {
                accFileContents += (char) reader.read();
            }
            String[] accountStrings = accFileContents.split("\n");
            for (String accountString: accountStrings) {
                String data = accountString.substring(2,accountString.length() - 1);
                String[] dataArray = data.split(",");
                switch (accountString.charAt(0)) {
                    case 'B':
                        BankAccount accountBank = new BankAccount(dataArray[2], dataArray[0], Integer.parseInt(dataArray[1]),
                                Double.parseDouble(dataArray[4]));
                        accountBank.credit(Double.parseDouble(dataArray[3]));
                        accounts.add(accountBank);
                        break;
                    case 'C':
                        CreditCardAccount accountCredit = new CreditCardAccount();
                        accountCredit.setIssuer(dataArray[0]);
                        String[] card;
                        for (int i = 1; i < dataArray.length; i += 1) {
                            card = dataArray[i].split(";");
                            accountCredit.addCard(card[0],card[1], card[2],
                                    Integer.parseInt(card[3]), Integer.parseInt(card[4]),
                                    Double.parseDouble(card[5]), Double.parseDouble(card[6]));
                        }
                        accounts.add(accountCredit);
                        break;
                    case 'I':
                        InvestmentAccount accountInvest = new InvestmentAccount(dataArray[0], Integer.parseInt(dataArray[1]),
                                dataArray[2]);
                        if (dataArray.length == 5) {
                            accountInvest.retirementContributions(Double.parseDouble(dataArray[4]));
                        }
                        accountInvest.credit(Double.parseDouble(dataArray[3]));
                        accounts.add(accountInvest);
                        break;
                    default:
                        break;
                }
            }

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        try {
            PrintWriter pw = new PrintWriter(acc);
            pw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return accounts;
    }

    public static void writeAccounts(ArrayList<Account> accounts) {
        File acc = new File(accountFile);
        for (Account account: accounts) {
            if (account instanceof BankAccount) {
                ((BankAccount)account).writeToFile(acc);
            } else if (account instanceof CreditCardAccount) {
                try {
                    ((CreditCardAccount)account).writeToFile(acc);
                } catch (NoCreditCardException e) {
                    e.printStackTrace();
                }
            } else if (account instanceof InvestmentAccount) {
                ((InvestmentAccount)account).writeToFile(acc);
            } else {
                System.out.println("FAIL");
            }
        }
    }

    public static boolean mainMenu(String owner, ArrayList<Account> accounts) {
        String menu = "Welcome to FinFree, " + owner + "! Please select from one of the options below" +
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
            }
        }
    }

}
