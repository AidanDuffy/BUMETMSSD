package accounts;

import accounts.creditcard.CreditCard;
import java.util.ArrayList;

public class CreditCardAccount extends Account{

    protected int currentCard;
    protected ArrayList<CreditCard> listOfCards;
    public String issuer;

    public CreditCardAccount(String owner) {
        this.listOfCards = new ArrayList<>();
        this.owner = owner;
        this.currentCard = -1;
    }

    public CreditCardAccount(){
        this.listOfCards = new ArrayList<>();
        this.currentCard = -1;
    }

    public void addCard(String number, String cvc, int expMonth, int expYear, double value, double creditLimit) {
        CreditCard card = new CreditCard(number,cvc,expMonth,expYear,value, creditLimit);
        if (getCurrentCard() == -1) {
            setCurrentCard(0);
        }
        this.listOfCards.add(card);
    }

    public double checkTotalSpendingLimit() {
        double limit = 0.0;
        for (CreditCard card:this.listOfCards) {
            limit += card.getCreditLimit();
        }
        return limit;
    }

    public double checkTotalRemainingSpendingLimit() {
        double limit = 0.0;
        for (CreditCard card:this.listOfCards) {
            limit += card.getCreditLimit() - card.getValue();
        }
        return limit;
    }

    public double checkSpendingLimit() {
        CreditCard card = this.listOfCards.get(getCurrentCard());
        return card.getCreditLimit();
    }

    public double checkRemainingLimit() {
        CreditCard card = this.listOfCards.get(getCurrentCard());
        return card.getCreditLimit() - card.getValue();
    }

    public double checkAmountDue() {
        CreditCard card = this.listOfCards.get(getCurrentCard());
        return card.getValue();
    }

    @Override
    public void debit(double amount) {
        this.value -= amount;
        CreditCard card = this.listOfCards.get(getCurrentCard());
        card.payOff(amount);
    }

    @Override
    public void credit(double amount) {
        setValue(getValue() + amount);
        CreditCard card = this.listOfCards.get(getCurrentCard());
        card.purchase(amount);
    }

    public int getCurrentCard() {
        return this.currentCard;
    }

    public String getIssuer() {
        return this.issuer;
    }

    @Override
    public String getOwner() {
        return this.owner;
    }

    @Override
    public double getValue() {
        return this.value;
    }

    public void setCurrentCard(int current) {
        this.currentCard = current;
    }

    public void setIssuer(String issuer) {
        this.issuer = issuer;
    }

    @Override
    public void setOwner(String owner) {
        this.owner = owner;
    }

    @Override
    public void setValue(double amount) {
        this.value = amount;
    }
}
