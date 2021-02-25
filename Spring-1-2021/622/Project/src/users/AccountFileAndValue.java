package users;

import accounts.*;
import main.FinFree;



public class AccountFileAndValue<T> {

    T account;
    String file_str;
    double value;

    public AccountFileAndValue(T acc, double val, String str) {
        account = acc;
        file_str = str;
        value = val;
    }

    public AccountFileAndValue(T acc, double val) {
        account = acc;
        file_str = acc.toString();
        value = val;
    }

    public double getValue() {
        return value;
    }

    public void update(double value) {
        this.value = value;
        this.file_str = account.toString();
    }

    public T getAccount() {
        return this.account;
    }

    public void writeToFile(String owner) throws NoCreditCardException {
        String in_braces = file_str.substring(2,file_str.length() - 2);
        if (in_braces.split(",").length == 1) {
            throw new NoCreditCardException();
        }
        int type = -1;
        if (account instanceof BankAccount) {
            type = 0;
        } else if (account instanceof CreditCardAccount) {
            type = 1;
        } else if (account instanceof InvestmentAccount) {
            type = 2;
        }
        FinFree.updateAccount(owner, type, file_str);
    }
}
