

public class Employee {
	// instance variables
	private int empId;
	private String name;
	
	// constructor
	public Employee() { }
	
	public Employee(int empId, String name) {
		this.empId = empId;
		this.name = name;
	}
	
	// get methods
	public int getEmpId() { return empId;}
	public String getName() { return name;}
	
	// set methods
	public void setEmpId(int empId) {
		this.empId = empId;
	}
	public void setName(String name) {
		this.name = name;
	}
}
