package users;

import javax.crypto.*;
import javax.crypto.interfaces.PBEKey;
import javax.crypto.spec.PBEKeySpec;
import java.io.UnsupportedEncodingException;
import java.math.BigInteger;
import java.security.*;
import java.security.spec.InvalidKeySpecException;

public class UserPassword {

    public static final String PBKDF2_ALGORITHM = "PBKDF2WithHmacSHA1";
    public static final int SALT_BYTES_USED = 32;
    public static final int HASH_BYTES_USED = 32;
    public static final int TOTAL_PBKDF2_ITERATIONS = 1000;

    private static boolean checkEquals(byte[] hash, byte[] temp) {
        int difference = hash.length ^ temp.length;
        for (int i = 0; i < Math.max(hash.length,temp.length); i += 1) {
            difference |= hash[i] ^ temp[i];
        }
        return (difference == 0);
    }

    public static boolean checkPassword(String password, String hash_given) throws InvalidKeySpecException, NoSuchAlgorithmException{
        char[] password_char = (password.toCharArray());
        String[] parameters = hash_given.split(":");
        int iter = Integer.parseInt(parameters[0]);
        byte[] salt = dehexify(parameters[1]);
        byte[] hash = dehexify(parameters[2]);
        byte[] temp = pbkdf2(password_char,salt,iter,hash.length);
        return checkEquals(hash, temp);
    }

    public static String createPassHash(String password) throws NoSuchAlgorithmException, InvalidKeySpecException {
        char[] password_char = (password.toCharArray());
        SecureRandom secureRandom = new SecureRandom();
        byte[] salt = new byte[SALT_BYTES_USED];
        secureRandom.nextBytes(salt);
        byte[] hash = pbkdf2(password_char,salt,TOTAL_PBKDF2_ITERATIONS, HASH_BYTES_USED);
        return TOTAL_PBKDF2_ITERATIONS + ":" + hexify(salt) + ":" + hexify(hash);
    }

    private static byte[] dehexify(String hex) {
        byte[] bin = new byte[hex.length()/2];
        for (int i = 0; i < bin.length; i += 1) {
            bin[i] = (byte) Integer.parseInt(hex.substring(2*i, 2*i + 2), 16);
        }
        return bin;
    }

    private static String hexify(byte[] hex) {
        BigInteger big = new BigInteger(1, hex);
        String result = big.toString(16);
        int padding = (hex.length*2) - result.length();
        if (padding > 0) {
            return String.format("%0" + padding + "d",0) + hex;
        } else {
            return result;
        }
    }

    private static byte[] pbkdf2(char[] password, byte[] salt, int iter, int num_of_bytes) throws InvalidKeySpecException, NoSuchAlgorithmException {
        PBEKeySpec key = new PBEKeySpec(password, salt, iter, num_of_bytes*8);
        SecretKeyFactory factory = SecretKeyFactory.getInstance(PBKDF2_ALGORITHM);
        return factory.generateSecret(key).getEncoded();
    }
}
