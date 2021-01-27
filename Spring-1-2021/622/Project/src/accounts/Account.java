package accounts;
//An account tied to a specific user, which contains assets of some value,
//either owned or owed.

public abstract class Account {
    //Pedagogical: (1) Attributes, (2) Constructors, (3) Methods,
    // are ordered alphabetically by type.

    protected String owner = "owner not determined";
    protected double value = 0.0; // Value starts at 0.

    public Account() {
    }

    //Pedagogical: all types of accounts have a way to increase or decrease value.
    public abstract void debit(double amount);
    public abstract void credit(double amount);
    public abstract String getOwner();
    public abstract double getValue();
    public abstract void setOwner(String owner);
    public abstract void setValue(double amount);
}
