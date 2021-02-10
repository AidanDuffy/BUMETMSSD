package users;

import accounts.*;

import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

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

    public boolean writeToFile(File file) throws NoCreditCardException {
        String in_braces = file_str.substring(2,file_str.length() - 1);
        if (in_braces.split(",").length == 1) {
            throw new NoCreditCardException();
        }
        try {
            String test = file.getAbsolutePath();
            FileReader reader = new FileReader(file.getAbsolutePath());
            String current = "";
            while (reader.ready()) {
                current += Character.toString(reader.read());
            }
            current += "\n";
            reader.close();
            FileWriter writer = new FileWriter(file.getName());
            writer.append(current).append(file_str);
            writer.close();
            return true;
        } catch (IOException e) {
            System.out.println("An error occurred when trying to write credit card account info.");
            e.printStackTrace();
        }
        return false;
    }
}
