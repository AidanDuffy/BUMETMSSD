public class SalariedEmployee extends Employee {

    //SalariedEmployee subclass adds one field
    private double salary;

    public SalariedEmployee(int empID, String name, double salary) {
        super(empID, name);
        this.salary = salary;
    }

    /**
     * @return the monthly version of the annual salary.
     */
    public double monthlyPayment() {
        return this.salary/12;
    }

    public void employeeInfo() {
        System.out.printf("Employee Information: Name: %s, ID: %d, Annual Salary: %d, and Monthly Salary: %d",
                this.getName(), this.getEmpId(), this.salary, this.monthlyPayment());
    }

    // get methods

    /**
     * @return the annual salary
     */
    public double getAnnualSalary() { return this.salary;}

    // set methods

    /**
     * @param salary is set to the annual salary value for the Employee.
     */
    public void setAnnualSalary(double salary) {
        this.salary = salary;
    }
}
