package accounts_test;

import accounts.*;
import org.junit.Test;
import users.AccountFileAndValue;

import java.io.File;

import static org.junit.Assert.assertEquals;

public class AccountToStringTest {

    @Test
    public void testBankString(){
        String bank = "Bank of America";
        String type = "Savings";
        double interest = 1.5;
        int account = 123456789;
        BankAccount bankAccount = new BankAccount(bank, type, account, interest);
        double deposit = 1586.32;
        bankAccount.credit(deposit);
        String str = bankAccount.toString();
        String data = str.substring(2,str.length()-1);
        assertEquals(str.charAt(0), 'B');
        String[] dataList = data.split(",");
        assertEquals(dataList[0], type);
        assertEquals(dataList[1], Integer.toString(account));
        assertEquals(dataList[2], bank);
        assertEquals(dataList[3], Double.toString(deposit));
        assertEquals(dataList[4], Double.toString(interest));
        System.out.println(str);
        AccountFileAndValue<BankAccount> acc = new AccountFileAndValue<BankAccount>(bankAccount, bankAccount.getValue());
    }

    @Test
    public void testCreditCardString(){
        CreditCardAccount account = new CreditCardAccount();
        account.setIssuer("AMEX");
        String test = account.toString();
        assertEquals(test.length(), 7);
        File file = new File("fileWriteTest.txt");
        String number = "1111 2222 3333 4444";
        String cvc = "012";
        int month = 10;
        int year = 25;
        double limit = 7200;
        String name = "Gold";
        account.addCard(name,number,cvc,month,year,0,limit);
        String str = account.toString();
        String data = str.substring(2,str.length()-1);
        assertEquals(str.charAt(0), 'C');
        String[] dataList = data.split(",");
        assertEquals(account.getIssuer(), dataList[0]);
        String[] card = dataList[1].split(";");
        assertEquals(card[0],name);
        assertEquals(card[1], number);
        assertEquals(card[2], cvc);
        assertEquals(card[3], Integer.toString(month));
        assertEquals(card[4], Integer.toString(year));
        assertEquals(card[5], String.format("%.2f",account.getValue()));
        assertEquals(card[6], Double.toString(limit));
        assertEquals(dataList.length, 2);
        assertEquals(card.length, 7);
        number = "5555 6666 7777 8888";
        cvc = "345";
        month = 11;
        limit = 3400;
        name = "Platinum";
        account.addCard(name,number,cvc,month,year,0, limit);
        str = account.toString();
        data = str.substring(2,str.length()-1);
        dataList = data.split(",");
        assertEquals(dataList.length, 3);
        card = dataList[2].split(";");
        assertEquals(card[0],name);
        assertEquals(card[1], number);
        assertEquals(card[2], cvc);
        assertEquals(card[3], Integer.toString(month));
        assertEquals(card[4], Integer.toString(year));
        assertEquals(card[5], String.format("%.2f",account.getValue()));
        assertEquals(card[6], Double.toString(limit));
        System.out.println(str);
    }

    @Test
    public void testInvestmentString(){
        String firm = "Vanguard";
        int number = 123456789;
        String type = "Brokerage";
        InvestmentAccount account = new InvestmentAccount(firm,number,type,0);
        double investment = 1234.56;
        account.credit(investment);
        String str = account.toString();
        String data = str.substring(2,str.length()-1);
        assertEquals(str.charAt(0), 'I');
        String[] dataList = data.split(",");
        assertEquals(dataList[0], firm);
        assertEquals(dataList[1], Integer.toString(number));
        assertEquals(dataList[2], type);
        assertEquals(dataList[3], Double.toString(investment));
        assertEquals(dataList.length, 4);
        double contribution = 5000;
        type = "Roth IRA";
        account.setAccountType(type);
        account.retirementContributions(contribution);
        str = account.toString();
        data = str.substring(2,str.length()-1);
        assertEquals(str.charAt(0), 'I');
        dataList = data.split(",");
        assertEquals(dataList.length, 5);
        assertEquals(dataList[2], type);
        assertEquals(dataList[3], String.format("%.2f",contribution + investment));
        assertEquals(dataList[4], String.format("%.2f",contribution));
        System.out.println(str);
        File file = new File("fileWriteTest.txt");
        AccountFileAndValue<InvestmentAccount> acc = new AccountFileAndValue<InvestmentAccount>(account, account.getValue());
    }

}
