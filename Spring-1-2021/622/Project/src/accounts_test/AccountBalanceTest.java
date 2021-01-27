package accounts_test;

import accounts.BankAccount;
import accounts.CreditCardAccount;
import accounts.InvestmentAccount;
import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotEquals;

public class AccountBalanceTest {

    @Test
    public void testBank(){
        String bank = "Bank of America";
        String type = "Savings";
        double interest = 1.5;
        int account = 123456789;
        BankAccount bankAccount = new BankAccount(bank, type, account, interest);
        assertEquals(bankAccount.getValue(), 0.0,0);
        assertEquals(bankAccount.getBank(),bank);
        double deposit = 1586.32;
        bankAccount.credit(deposit);
        assertEquals(bankAccount.getValue(),deposit, 0);
        bankAccount.debit(deposit);
        assertEquals(bankAccount.getValue(),0, 0);
    }

    @Test
    public void testCreditCard(){
        CreditCardAccount account = new CreditCardAccount();
        account.setIssuer("AMEX");
        String number = "1111 2222 3333 4444";
        String cvc = "012";
        int month = 10;
        int year = 25;
        double limit1 = 7200;
        String name = "Gold";
        account.addCard(name,number,cvc,month,year,0,limit1);
        number = "5555 6666 7777 8888";
        cvc = "345";
        month = 11;
        double limit2 = 3400;
        name = "Platinum";
        account.addCard(name,number,cvc,month,year,0, limit2);
        double limits = limit1 + limit2;
        assertEquals(limits,account.checkTotalRemainingSpendingLimit(),0);
        assertEquals(0,account.checkAmountDue(),0);
        assertEquals(0,account.getCurrentCard(),0);
        assertEquals(account.checkSpendingLimit(),limit1,0);
        account.credit(5000);
        assertEquals(account.checkRemainingLimit(),limit1-5000,0);
        account.setCurrentCard(1);
        account.credit(1000);
        assertEquals(account.getValue(),6000,0);
        assertEquals(account.checkAmountDue(),1000,0);
        assertEquals(account.checkTotalRemainingSpendingLimit(), limits-6000,0);
        account.displayBalancesAndLimits();
    }

    @Test
    public void testInvestment(){
        String firm = "Vanguard";
        int number = 123456789;
        String type = "Brokerage";
        InvestmentAccount account = new InvestmentAccount(firm,number,type,0);
        assertEquals(account.firm,firm);
        double contribution = 5000;
        account.retirementContributions(contribution);
        assertNotEquals(contribution,account.getContributions());
        type = "Roth IRA";
        account.setAccountType(type);
        account.retirementContributions(contribution);
        double amount = 100.53;
        account.credit(amount);
        assertEquals(contribution,account.getContributions(),0);
        assertEquals(contribution+amount,account.getValue(),0);
        account.debit(amount);
        assertEquals(contribution,account.getValue(),0);
    }

}
