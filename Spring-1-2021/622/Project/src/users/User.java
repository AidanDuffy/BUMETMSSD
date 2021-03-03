package users;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.util.ArrayList;
import accounts.*;
import main.FinFree;

public class User implements Runnable{

    String owner;
    String password;
    ArrayList<AccountFileAndValue> accounts;

    public User(String user, String password) {
        owner = user;
        try {
            password = UserPassword.createPassHash(password);
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (InvalidKeySpecException e) {
            e.printStackTrace();
        }
        accounts = new ArrayList<>();
    }

    public void addAccount(Account account) {
        double val = account.getValue();
        AccountFileAndValue acc = new AccountFileAndValue(account, val);
        accounts.add(acc);
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
            Account acc = (Account) a.getAccount();
            if (type == 0 && acc instanceof BankAccount) {
                account_by_type.add((BankAccount) a.account);
            } else if (type == 1 && acc instanceof CreditCardAccount) {
                account_by_type.add((CreditCardAccount) a.account);
            } else if (type == 2 && acc instanceof InvestmentAccount) {
                account_by_type.add((InvestmentAccount) a.account);
            }
        }
        return account_by_type;
    }

    public String[] getAllAccountValues() {
        ArrayList<Account> accs = getAccounts();
        String[] res = new String[accs.size()];
        for (int i = 0; i < accs.size(); i += 1) {
            Account a = accs.get(i);
            String temp = "";
            if (a instanceof BankAccount) {
                temp += ((BankAccount) a).bank + " " + ((BankAccount) a).accountType + ": " + String.format("%.2f",a.getValue());
            } else if (a instanceof CreditCardAccount) {
                temp += ((CreditCardAccount) a).issuer + String.format(": %.2f", a.getValue());
            } else if (a instanceof InvestmentAccount) {
                temp += ((InvestmentAccount) a).firm + " " + ((InvestmentAccount) a).accountType + ": " + String.format("%.2f",a.getValue());
            }
            res[i] = temp;
        }
        return res;
    }

    public String getPassword() {
        return password;
    }

    public double getNetCash() {
        double cash = 0.0;
        for (Account a: (ArrayList<Account>) getAccountsByType(0)) {
            cash += a.getValue();
        }
        return cash;
    }

    public double getNetDebt() {
        double debt = 0.0;
        for (Account a: (ArrayList<Account>) getAccountsByType(1)) {
            debt += a.getValue();
        }
        return debt;
    }

    public String getName() {
        return owner;
    }

    public double getNetWorth() {
        double worth = this.getNetCash() - this.getNetDebt();
        for (Account a: (ArrayList<Account>) getAccountsByType(2)) {
            worth += a.getValue();
        }
        return worth;
    }

    public void readAccounts() {
        accounts = new ArrayList<>();
        String bank = FinFree.readAccount(getName(), 0);
        String credit = FinFree.readAccount(getName(), 1);
        String invest = FinFree.readAccount(getName(), 2);
        if (bank != (null)) {
            String data = bank.substring(2, bank.length() - 2);
            String[] dataArray = data.split(",");
            BankAccount accountBank = new BankAccount(dataArray[2], dataArray[0], Integer.parseInt(
                    dataArray[1]), Double.parseDouble(dataArray[4]));
            accountBank.credit(Double.parseDouble(dataArray[3]));
            AccountFileAndValue<BankAccount> bankFileAndValue = new AccountFileAndValue
                    <BankAccount>(accountBank, accountBank.getValue());
            accounts.add(bankFileAndValue);
        }
        if (credit != (null)) {
            String data = credit.substring(2, bank.length() - 2);
            String[] dataArray = data.split(",");
            CreditCardAccount accountCredit = new CreditCardAccount();
            accountCredit.setIssuer(dataArray[0]);
            String[] card;
            for (int i = 1; i < dataArray.length; i += 1) {
                card = dataArray[i].split(";");
                accountCredit.addCard(card[0], card[1], card[2],
                        Integer.parseInt(card[3]), Integer.parseInt(card[4]),
                        Double.parseDouble(card[5]), Double.parseDouble(card[6]));
            }
            AccountFileAndValue<CreditCardAccount> creditFileAndValue = new AccountFileAndValue
                    <CreditCardAccount>(accountCredit, accountCredit.getValue());
            accounts.add(creditFileAndValue);
        }
        if (invest != (null)) {
            String data = invest.substring(2, bank.length() - 2);
            String[] dataArray = data.split(",");
            InvestmentAccount accountInvest = new InvestmentAccount(dataArray[0],
                    Integer.parseInt(dataArray[1]), dataArray[2]);
            if (dataArray.length == 5) {
                accountInvest.retirementContributions(Double.parseDouble(dataArray[4]), false);
            }
            accountInvest.credit(Double.parseDouble(dataArray[3]));
            AccountFileAndValue<InvestmentAccount> investFileAndValue = new AccountFileAndValue
                    <InvestmentAccount>(accountInvest, accountInvest.getValue());
            accounts.add(investFileAndValue);
        }
    }

    @Override
    public void run() {
        while (true) {
            try {
                this.readAccounts();
                Thread.sleep(30000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public void writeAccounts() {
        for (AccountFileAndValue a: this.accounts) {
           try {
               a.writeToFile(owner);
           } catch (NoCreditCardException e) {
               e.printStackTrace();
           }
        }
    }
}

