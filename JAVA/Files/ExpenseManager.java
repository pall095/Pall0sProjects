import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.math.BigDecimal;
import java.math.RoundingMode;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;


public class ExpenseManager {


    // Defines input and output dates formatting.
    private static final DateTimeFormatter INPUT_DATE_FORMATTER = DateTimeFormatter.ofPattern("yyyy-MM-dd H:mm:ss");
    private static final DateTimeFormatter OUTPUT_DATE_FORMATTER = DateTimeFormatter.ofPattern("yyy/MM/dd") ;
    private Collection< Expense > expenses ;

    public static ExpenseManager of( String filePath ) throws Exception{

        BufferedReader br = new BufferedReader( new FileReader( filePath ) ) ;
        Collection< Expense > expenseList = new ArrayList<>( ) ;
        
        String line;
        String[ ] parts ;
        LocalDate date ; 
        String description ; 
        Double amount ; 
        String category ; 
        Expense curreExpense ;

        br.readLine( ) ; //dumping header line.
        while( (line = br.readLine()) != null ){
            
            parts = line.split( "," ) ;
            date = LocalDate.parse( parts[ 2 ] , ExpenseManager.INPUT_DATE_FORMATTER  ) ;
            description = parts[ 4 ] ;
            amount = Double.parseDouble( parts[ 5 ] ) ;
            category = "none" ;
            curreExpense = new Expense( date , description, amount , category ) ;
            expenseList.add( curreExpense ) ;
        }
        br.close();
        return new ExpenseManager( expenseList ) ;  
    }

    
    public ExpenseManager( Collection< Expense > expenseList ){
        this.expenses = expenseList;
    }

    public void printExpenses( ){
        for( Expense e : this.expenses ){
            IO.println( e ) ;
        }
    }

    public void dumpStatistics( String outPath ) throws Exception{

        BufferedWriter out = new BufferedWriter( new FileWriter( outPath ) ) ;
        
        LocalDate firstDay = this.expenses.stream().sorted( Comparator.comparing( Expense::getDate ) ).findFirst().get().getDate() ;
        LocalDate lastDay = this.expenses.stream().sorted( Comparator.comparing( Expense::getDate ).reversed() ).findFirst().get().getDate() ; 

        Double total_out = this.expenses.stream( )
                                .filter( e -> e.getAmount( ) < 0 )
                                .collect( Collectors.summingDouble( Expense::getAmount ) ) ;
        
        Double total_in = this.expenses.stream( )
                        .filter( e -> e.getAmount( ) > 0 )
                        .collect( Collectors.summingDouble( Expense::getAmount ) ) ;

        List< String > expensePerCategory = this.expenses.stream( )
                                                .collect(
                                                    Collectors.groupingBy(
                                                        Expense::getCategory ,
                                                        Collectors.summingDouble( Expense::getAmount ) 
                                                    )
                                                )
                                                .entrySet( )
                                                .stream( )
                                                .map( e -> "Category: " + e.getKey( ) + " - Amount: " + BigDecimal.valueOf( e.getValue( ) ).setScale( 2  , RoundingMode.HALF_UP ) )
                                                .toList( ) ;

        out.write( "First day:" + firstDay ) ;
        out.newLine();
        out.write( "Last day:" + lastDay ) ;
        out.newLine();
        out.write( "Total gains:" + BigDecimal.valueOf( total_in ).setScale( 2 , RoundingMode.HALF_UP ) );
        out.newLine();
        out.write( "Total expenses:" + BigDecimal.valueOf( total_out ).setScale( 2 , RoundingMode.HALF_UP ) );
        out.newLine();
        out.write("Expense per category:");
        out.newLine();
        for( String s : expensePerCategory ){
            out.write( "\t" + s ) ;
            out.newLine( ); 
        }
        out.close( );
    }

    public void categorizeExpenses( Categorizer categorizerObj ){
        for( Expense e : this.expenses ){
            e.setCategory( categorizerObj.findCategory( e ) ) ;
        }
    }

    public void toCsv( String fileName ) throws Exception {

        BufferedWriter bw = new BufferedWriter( new FileWriter( fileName ) ) ;

        for( Expense e : this.expenses ){
            bw.write( e.toCsv( ) ) ;
            bw.newLine( ) ;
        }
        bw.close( );
    }
}
