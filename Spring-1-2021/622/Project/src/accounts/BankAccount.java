package accounts;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class BankAccount extends Account {

    public String accountType; //This determines if the account is checking, savings, or a CD.
    protected int accountNumber;
    public String bank;
    public double interestRate;

    public BankAccount(String bank, String accountType, int accountNumber, double interestRate) {
        this.bank = bank;
        this.accountNumber = accountNumber;
        this.accountType = accountType;
        this.interestRate = interestRate;
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

    public String getBank() {
        return bank;
    }

    public double getInterestRate() {
        return interestRate;
    }

    @Override
    public String getOwner() {
        return owner;
    }

    @Override
    public double getValue() {
        return value;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public void setAccountType(String accountType) {
        this.accountType = accountType;
    }

    public void setBank(String bank) {
        this.bank = bank;
    }

    public void setInterestRate(double interestRate) {
        this.interestRate = interestRate;
    }

    @Override
    public void setOwner(String owner) {
        this.owner = owner;
    }

    @Override
    public void setValue(double amount) {
        this.value = amount;
    }

    @Override
    public String toString() {
        return "B{" + accountType +
                "," + accountNumber +
                "," + bank +
                "," + value +
                "," + interestRate +
                '}';
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
            System.out.println("An error occurred when trying to write bank account info.");
            e.printStackTrace();
        }
        return false;
    }
}
