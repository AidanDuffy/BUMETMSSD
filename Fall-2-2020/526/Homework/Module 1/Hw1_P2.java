import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Hw1_P2 {

    /**
     * The main method reads the information of salaried employees from an input text file. It creates SalariedEmployee
     * objects and stores them in an array.
     * @param args
     * @throws FileNotFoundException in case of error with the Scanner.
     */
    public static void main(String[] args) throws FileNotFoundException {
        File employees = new File("employee_input.txt");
        Scanner fileReader = new Scanner(employees);
        int id = 0;
        double salary = 0;
        String name = "";
        String line = ""; // This represents the current line that the Scanner has read in.
        //This represents the current index of the last comma so the method knows where the next instance variables are.
        int current = 0;
        int count = 0; //Keeps track of how many employees we've added to the empArray.
        SalariedEmployee[] empArray = new SalariedEmployee[10];
        while (fileReader.hasNextLine()) {
            line = fileReader.nextLine();
            for (int i = 1; i < line.length(); i += 1) {
                if (id == 0) {
                    if (line.substring(i-1,i).equals(",")) {
                        id = Integer.valueOf(line.substring(0, i-1));
                        current = i + 1;
                    }
                } else if (id != 0 && name.equals("") && i > current) {
                    if(line.substring(i-1, i).equals(",")) {
                        name = line.substring(current, i-1);
                        current = i + 1;
                    }
                } else if (!name.equals("") && salary == 0 && i > current) {
                    salary = Double.valueOf(line.substring(current));
                    current = 0;
                }
            }
            SalariedEmployee emp = new SalariedEmployee(id, name, salary);
            empArray[count] = emp;
            id = 0;
            name = "";
            salary = 0;
            count += 1;
        }
        //Tests
        employeesAbove(empArray, 70000);
        employeesAbove(empArray, 100000);
        employeesAbove(empArray, 0);
    }

    /**
     * This method selects employees from the given array who earn more than the given salary threshold amount and then
     * displays their employee information (ID, name, and annual and monthly salary.
     * @param empyArray is the array of SalariedEmployee objects.
     * @param threshold is the salary threshold.
     */
    public static void employeesAbove(SalariedEmployee[] empyArray, double threshold) {
        System.out.println("Employees earning more than $" + (int)threshold + ":\n");
        for (SalariedEmployee emp:empyArray) {
            if (emp.getAnnualSalary() >= threshold) {
                System.out.printf("\tEmployee ID: " + emp.getEmpId() + "\n\tName: " + emp.getName() + "\n\tAnnual Salary: " +
                        "%.2f\n\tMonthly Pay: %.2f\n\n", emp.getAnnualSalary(), emp.getAnnualSalary()/12);
            }
        }
    }
}
