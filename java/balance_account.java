public class balance_account {
    String accountholdname;
    double amount;
    double balance;

    // Changed the data type from 'main' to 'balance_account'
    void calculate(balance_account receive, double amount) {
        if (balance >= amount) {
            balance = balance - amount;
            receive.balance = receive.balance + amount;
        } else {
            System.out.println("Insufficient balance");
        }
    }

    public static void main(String[] args) {
        // Changed object types from 'main' to 'balance_account'
        balance_account a1 = new balance_account();
        balance_account a2 = new balance_account();
        
        a1.balance = 20000;
        a2.balance = 15000;

        a1.calculate(a2, 5000);
        a2.calculate(a1, 6000);

        System.out.println("a1 balance: " + a1.balance);
        System.out.println("a2 balance: " + a2.balance);
    }
}
