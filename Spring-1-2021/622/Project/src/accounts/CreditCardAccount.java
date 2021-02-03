package accounts;

import accounts.creditcard.CreditCard;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class CreditCardAccount extends Account{

    protected int currentCard;
    private ArrayList<CreditCard> listOfCards;
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

    public void addCard(String name, String number, String cvc, int expMonth, int expYear, double value, double creditLimit) {
        CreditCard card = new CreditCard(name, number,cvc,expMonth,expYear,value, creditLimit);
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

    public void displayBalancesAndLimits() {
        System.out.println("Card Balances | Card Limits");
        System.out.println("For all " + getIssuer() + " cards");
        for (CreditCard card: this.listOfCards) {
            double remaining = card.getCreditLimit() - card.getValue();
            System.out.println(card.getName());
            System.out.println("\t\tBalance: " + card.getValue() + " | Remaining Limit: " + remaining);
        }
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

    @Override
    public String toString() {
        String data = "C{" + issuer;
        for(CreditCard card: this.listOfCards) {
            data += "," + card.toString();
        }
        data += "}";
        return data;
    }

    @Override
    public boolean writeToFile(File file) throws NoCreditCardException {
        if (this.getCurrentCard() == -1) {
            throw new NoCreditCardException();
        }
        String data = this.toString();
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
            System.out.println("An error occurred when trying to write credit card account info.");
            e.printStackTrace();
        }
        return false;
    }
}
