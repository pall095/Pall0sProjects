import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;


public class Expense {

    private LocalDate date ;
    private String description ; 
    private Double amount ; 
    private String category ; 

    public Expense( LocalDate date , String description , Double amount , String category ){
        this.date = date ; 
        this.description = description ; 
        this.amount = amount ; 
        this.category = category ;
    }

    public String getDescription( ){
        return this.description ;
    }

    public LocalDate getDate( ){
        return this.date ;
    }

    public Double getAmount( ){
        return this.amount ; 
    } 

    public String getCategory( ){
        return this.category ; 
    } 

    public void setCategory( String category ){
        this.category = category ; 
    }


    @Override
    public String toString( ){
        StringBuilder s = new StringBuilder() ;
        s.append( "Date: " + this.date.toString( ) + "\n" ) ;
        s.append( "Description: " + this.description  +"\n" ) ;
        s.append( "Amount: " + this.amount.toString( ) + "\n" ) ;
        s.append("Categories: " + this.category + "\n" ) ;
        return s.toString( ) ;
    }

    public String toCsv( ){
        StringBuilder s = new StringBuilder() ;
        s.append( this.date.toString( ) + "," ) ;
        s.append( this.description  +"," ) ;
        s.append( this.amount.toString( ) + "," ) ;
        s.append( this.category + "," ) ;
        return s.toString( ) ;
    }


}
