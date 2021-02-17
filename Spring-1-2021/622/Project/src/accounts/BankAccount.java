package accounts;

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

    public BankAccount(String bank, String accountType, int accountNumber,double balance, double interestRate) {
        this.bank = bank;
        this.accountNumber = accountNumber;
        this.accountType = accountType;
        this.interestRate = interestRate;
        this.value = balance;
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
}
