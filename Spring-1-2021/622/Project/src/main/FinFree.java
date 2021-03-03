package main;

import users.User;
import users.UserPassword;

import java.security.NoSuchAlgorithmException;
import java.security.spec.InvalidKeySpecException;
import java.sql.*;
import java.util.concurrent.locks.ReentrantLock;


public class FinFree {

    private static final String USERNAME = "root";
    private static final String PASSWORD = "Whatcdptpbtn44%"; //I just got rid of this since it is a password I actually use sometimes...
    private static final String CONN_STRING = "jdbc:mysql://localhost:3306/finfree";
    static Connection connection = null;
    static ReentrantLock accLock = new ReentrantLock();

    public static void main(String[] args) {
        System.out.println("Connecting database...");
        try {
            connection = DriverManager.getConnection(CONN_STRING, USERNAME, PASSWORD);
            System.out.println("Database connected!");
        } catch (SQLException e) {
            System.out.println("FAIL");
            throw new IllegalStateException("Cannot connect the database!", e);
        }
        Menu menu = new Menu();
        menu.run();
    }

    public static void addUser(String name, String password) {
        try (Statement statement = connection.createStatement()) {
            String hashedSalted = UserPassword.createPassHash(password);
            statement.executeUpdate("INSERT INTO LOGINS (username, password) values ('" + name + "','" + hashedSalted + "')");
            statement.executeUpdate("INSERT INTO USERS (username) values ('" + name + "')");
        } catch (SQLException | NoSuchAlgorithmException | InvalidKeySpecException e) {
            e.printStackTrace();
        }
    }

    public static boolean checkUserInfo(String username, String password) {
        ResultSet rs = null;
        boolean valid = false;
        String res = "";
        String accs = "";
        try (Statement statement = connection.createStatement()) {
            rs = statement.executeQuery("SELECT * FROM users INNER JOIN logins ON users.username = logins.username WHERE logins.username= '" + username + "';");
            while (rs.next()) {
                accs += rs.getString(1);
            }
            rs = statement.executeQuery("SELECT password FROM LOGINS WHERE username = '" + username + "';");
            while (rs.next()) {
                res += rs.getString(1);
            }
            valid = (UserPassword.checkPassword(password,res) && !accs.equals("null"));
        } catch (SQLException | InvalidKeySpecException | NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
        return valid;
    }

    public static void updateAccount(String name, int type, String account) {
        int count = 0;
        while (accLock.isLocked()){
            if (count == 0) {
                System.out.println("Please wait...");
                count += 1;
            }
        }
        accLock.lock();
        try (Statement statement = connection.createStatement()) {
            if (type == 0) {
                statement.executeUpdate("UPDATE users SET bank = '" + account + "' WHERE username = '" + name + "';");
            }
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            accLock.unlock();
        }
    }

    public static String readAccount(String name, int type) {
        int count = 0;
        while (accLock.isLocked()){
            if (count == 0) {
                System.out.println("Please wait...");
                count += 1;
            }
        }
        accLock.lock();
        ResultSet rs = null;
        String result = "";
        try (Statement statement = connection.createStatement()) {
            if (type == 0) {
                rs = statement.executeQuery("SELECT bank FROM users WHERE username = '" + name + "';");
            } else if (type == 1) {
                rs = statement.executeQuery("SELECT credit FROM users WHERE username = '" + name + "';");
            } else if (type == 2) {
                rs = statement.executeQuery("SELECT invest FROM users WHERE username = '" + name + "';");
            }
            while (rs.next()) {
                result += rs.getString(1);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            accLock.unlock();
            if (result.equals("null")) {
                return null;
            } else {
                return result;
            }
        }
    }

    private String getAllUserLogins(User user) {
        ResultSet rs = null;
        String logins = "";
        if(user.getName().equals("admin") && checkUserInfo(user.getName(),user.getPassword())) {
            try (Statement statement = connection.createStatement()) {
                rs = statement.executeQuery("SELECT * FROM logins GROUP BY username;");
                while (rs.next()) {
                    logins += rs.getString(1);
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return logins;
    }

}
