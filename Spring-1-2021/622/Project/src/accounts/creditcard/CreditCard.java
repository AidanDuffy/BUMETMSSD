package accounts.creditcard;

public class CreditCard {

    protected String number;
    protected String cvc;
    protected int expMonth;
    protected int expYear;
    protected double value;
    public double creditLimit;

    public CreditCard(String number, String cvc, int expMonth, int expYear, double value, double creditLimit) {
        this.number = number;
        this.cvc = cvc;
        this.expMonth = expMonth;
        this.expYear = expYear;
        this.value = value;
        this.creditLimit = creditLimit;
    }

    public double getCreditLimit() {
        return creditLimit;
    }

    public double getValue(){
        return this.value;
    }

    public void payOff(double value) {
        this.value -= value;
    }

    public void purchase(double value) {
        this.value += value;
    }

    public void setCreditLimit(double creditLimit) {
        this.creditLimit = creditLimit;
    }

    public void setValue(double value) {
        this.value = value;
    }
}
