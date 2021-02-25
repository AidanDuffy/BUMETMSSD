package main;

import java.sql.*;
import java.util.concurrent.locks.ReentrantLock;

public class FinFree {

    private static final String USERNAME = "root";
    private static final String PASSWORD = "XXXX"; //I just got rid of this since it is a password I actually use sometimes...
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

    public static void addUser(String name) {
        try (Statement statement = connection.createStatement()) {
            statement.executeUpdate("INSERT INTO USERS (username) values ('" + name + "')");
        } catch (SQLException e) {
            e.printStackTrace();
        }
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

}
