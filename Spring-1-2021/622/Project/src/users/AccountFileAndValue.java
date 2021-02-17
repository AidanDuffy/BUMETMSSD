package users;

import accounts.*;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;

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

    public boolean writeToFile(File file) throws NoCreditCardException {
        String in_braces = file_str.substring(2,file_str.length() - 1);
        if (in_braces.split(",").length == 1) {
            throw new NoCreditCardException();
        }
        try {
            DataOutputStream dataOutputStream = new DataOutputStream(new FileOutputStream(file.getAbsolutePath()));
            DataInputStream dataInputStream = new DataInputStream(new FileInputStream(file.getAbsolutePath()));
            byte[] bytes = new byte[(int)file.length()];
            dataInputStream.read(bytes);
            byte[] toStringByte = account.toString().getBytes(StandardCharsets.UTF_8);
            byte[] combined = new byte[bytes.length + toStringByte.length];
            for (int i = 0; i < bytes.length; i += 1) {
                combined[i] = bytes[i];
            }
            for (int i = 0; i < toStringByte.length; i += 1) {
                combined[i + bytes.length] = bytes[i];
            }
            dataOutputStream.write(combined);
            return true;
        } catch (IOException e) {
            System.out.println("An error occurred when trying to write credit card account info.");
            e.printStackTrace();
        }
        return false;
    }
}
