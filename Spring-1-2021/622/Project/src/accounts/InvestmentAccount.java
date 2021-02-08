package accounts;

public class InvestmentAccount extends Account {

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
}
