package accounts;

public class NoCreditCardException extends Exception{
    NoCreditCardException() {
    }

    public String toString(){
        return "Error! This credit card account contains no credit cards, so it is invalid and will not be written to the accounts file!";
    }
}
