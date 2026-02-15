
public class Main {
    public static void main(String[] args) throws Exception {

        ExpenseManager manager = ExpenseManager.of( args[ 0 ] ) ; 
        Categorizer categorizer = Categorizer.of( args[ 1 ] ) ;
        manager.categorizeExpenses( categorizer ) ;
        manager.toCsv( args[ 2 ] ) ;
        manager.dumpStatistics( args[ 3 ] ) ;

    }
}
