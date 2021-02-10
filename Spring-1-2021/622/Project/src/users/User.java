package users;

import java.io.*;
import java.util.ArrayList;
import accounts.*;

public class User {

    String owner;
    ArrayList<AccountFileAndValue> accounts;

    public User(String user) {
        owner = user;
        accounts = new ArrayList<>();
    }

    public void addAccount(Account account) {
        double val = account.getValue();
        if (account instanceof BankAccount) {
            AccountFileAndValue<BankAccount> acc = new AccountFileAndValue<BankAccount>((BankAccount) account,val);
            accounts.add(acc);
        } else if (account instanceof CreditCardAccount) {
            AccountFileAndValue<CreditCardAccount> acc = new AccountFileAndValue<CreditCardAccount>((CreditCardAccount) account,val);
            accounts.add(acc);
        } else if (account instanceof InvestmentAccount) {
            AccountFileAndValue<InvestmentAccount> acc = new AccountFileAndValue<InvestmentAccount>((InvestmentAccount) account,val);
            accounts.add(acc);
        }
    }

    public ArrayList<Account> getAccounts() {
        ArrayList<Account> plain_accs = new ArrayList<>();
        for (AccountFileAndValue a: this.accounts) {
            plain_accs.add((Account) a.account);
        }
        return plain_accs;
    }

    public ArrayList<Account> getAccountsByType(int type) {
        ArrayList<Account> account_by_type = new ArrayList<>();
        for (AccountFileAndValue a: this.accounts) {
            if (type == 0 && a.account instanceof BankAccount) {
                account_by_type.add((BankAccount) a.account);
            } else if (type == 1 && a.account instanceof CreditCardAccount) {
                account_by_type.add((CreditCardAccount) a.account);
            } else if (type == 2 && a.account instanceof InvestmentAccount) {
                account_by_type.add((InvestmentAccount) a.account);
            }
        }
        return account_by_type;
    }

    public double getNetCash() {
        double cash = 0.0;
        for (AccountFileAndValue a: this.accounts) {
            if (a.account instanceof BankAccount) {
                cash += a.getValue();
            }
        }
        return cash;
    }

    public double getNetDebt() {
        double debt = 0.0;
        for (AccountFileAndValue a: this.accounts) {
            if (a.account instanceof CreditCardAccount) {
                debt += a.getValue();
            }
        }
        return debt;
    }

    public String getName() {
        return owner;
    }

    public double getNetWorth() {
        double worth = getNetCash() - getNetDebt();
        for (AccountFileAndValue a: this.accounts) {
            if (a.account instanceof InvestmentAccount) {
                worth += a.getValue();
            }
        }
        return worth;
    }

    public void readAccounts(File file) {
        String accFileContents = "";
        try {
            FileReader reader = new FileReader(file);
            while(reader.ready()) {
                accFileContents += (char) reader.read();
            }
            String[] accountStrings = accFileContents.split("\n");
            for (String accountString: accountStrings) {
                String data = accountString.substring(2,accountString.length() - 1);
                String[] dataArray = data.split(",");
                switch (accountString.charAt(0)) {
                    case 'B':
                        BankAccount accountBank = new BankAccount(dataArray[2], dataArray[0], Integer.parseInt(
                                dataArray[1]), Double.parseDouble(dataArray[4]));
                        accountBank.credit(Double.parseDouble(dataArray[3]));
                        AccountFileAndValue<BankAccount> bankFileAndValue = new AccountFileAndValue
                                <BankAccount>(accountBank, accountBank.getValue());
                        accounts.add(bankFileAndValue);
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
                        AccountFileAndValue<CreditCardAccount> creditFileAndValue = new AccountFileAndValue
                                <CreditCardAccount>(accountCredit, accountCredit.getValue());
                        accounts.add(creditFileAndValue);
                        break;
                    case 'I':
                        InvestmentAccount accountInvest = new InvestmentAccount(dataArray[0],
                                Integer.parseInt(dataArray[1]), dataArray[2]);
                        if (dataArray.length == 5) {
                            accountInvest.retirementContributions(Double.parseDouble(dataArray[4]));
                        }
                        accountInvest.credit(Double.parseDouble(dataArray[3]));
                        AccountFileAndValue<InvestmentAccount> investFileAndValue = new AccountFileAndValue
                                <InvestmentAccount>(accountInvest, accountInvest.getValue());
                        accounts.add(investFileAndValue);
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
            PrintWriter pw = new PrintWriter(file);
            pw.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public void writeAccounts(File file) {
        for (AccountFileAndValue a: this.accounts) {
           try {
               a.writeToFile(file);
           } catch (NoCreditCardException e) {
               e.printStackTrace();
           }
        }
    }
}

