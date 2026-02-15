import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Categorizer {

    private Map< String , Collection< String > > categoriesDict ;

    public static Categorizer of( String filePath ) throws Exception{

        BufferedReader br = new BufferedReader( new FileReader( filePath ) ) ;
        String line ;
        String category = br.readLine( ).split( ":" )[ 0 ] ; 
        List< String > keywords = new ArrayList<>() ;
        Map< String , Collection< String > > categoriesMap = new HashMap<>( ) ;

        while( ( line = br.readLine( ) ) != null ){
            
            if( line.isEmpty() ){
                continue ; 
            }

            if( line.contains( ":" ) ){
                if( keywords.size() == 0 ){
                    continue ; 
                }else{
                    categoriesMap.put( category ,  keywords ) ;
                    category = line.split( ":" )[ 0 ] ;
                    keywords = new ArrayList<>() ;
                }
            }else{
                keywords.add( line ) ;
            }
            
        }

        if( keywords.size() > 0 ){
            categoriesMap.put(category, keywords) ;
        }

        br.close();
        return new Categorizer( categoriesMap ) ;

    }
    
    public Categorizer( Map< String , Collection< String > > categoriesDict ){
        this.categoriesDict = categoriesDict ; 
    }


    public String findCategory( Expense exp ){
    
        for( String key : this.categoriesDict.keySet() ){
            if( categoriesDict.get( key ).contains( exp.getDescription( ) ) ){
                return key ;
            }    
        }

        if( exp.getAmount() >= 0 ){
            return "GENERIC_GAIN" ;
        }else{
            return "GENERIC_EXPENSE" ;
        }

    } 
}
