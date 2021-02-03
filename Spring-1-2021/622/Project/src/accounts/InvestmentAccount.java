package accounts;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class InvestmentAccount extends Account{

    public String firm;
    protected int accountNumber;
    public String accountType; //Determines if it is a brokerage, margin, or retirement account, etc.
    public double contributions;

    public InvestmentAccount(String firm, int accountNumber, String accountType) {
        this.firm = firm;
        this.accountNumber = accountNumber;
        this.accountType = accountType;
    }

    public InvestmentAccount(String firm, int accountNumber, String accountType, double contributions) {
        this(firm, accountNumber, accountType);
        this.contributions = contributions;
    }

    @Override
    public void credit(double amount) {
        this.value += amount;
    }

    @Override
    public void debit(double amount) {
        this.value -= amount;
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public String getAccountType() {
        return accountType;
    }

    public double getContributions() {
        return contributions;
    }

    public String getFirm() {
        return firm;
    }

    @Override
    public String getOwner() {
        return owner;
    }

    @Override
    public double getValue() {
        return value;
    }

    public void retirementContributions(double contributions) {
        if (getAccountType().contains("IRA") || getAccountType().contains("401(k)")) {
            setContributions(getContributions() + contributions);
            credit(contributions);
        }
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setAccountType(String accountType) {
        this.accountType = accountType;
    }

    public void setContributions(double contributions) {
        this.contributions = contributions;
    }

    public void setFirm(String firm) {
        this.firm = firm;
    }

    @Override
    public void setOwner(String owner) {
        this.owner = owner;
    }

    @Override
    public void setValue(double amount) {
        this.value = value;
    }

    @Override
    public String toString() {
        String data;
        if (getAccountType().contains("IRA") || getAccountType().contains("401(k)")) {
            data = "I{" + firm + "," + accountNumber +
                    "," + accountType + "," + value + "," + contributions +
                    '}';
        } else {
            data = "I{" + firm + "," + accountNumber +
                    "," + accountType + "," + value + '}';
        }
        return data;
    }

    @Override
    public boolean writeToFile(File file) {
        String data = toString();
        try {
            FileReader reader = new FileReader(file.getName());
            String current = "";
            while (reader.ready()) {
                current += Character.toString(reader.read());
            }
            current += "\n";
            reader.close();
            FileWriter writer = new FileWriter(file.getName());
            writer.append(current).append(data);
            writer.close();
            return true;
        } catch (IOException e) {
            System.out.println("An error occurred when trying to write investment account info.");
            e.printStackTrace();
        }
        return false;
    }
}
