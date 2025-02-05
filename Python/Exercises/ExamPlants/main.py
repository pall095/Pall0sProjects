
def find_max( country_dict , search_key ) :

    max = 0 
    max_key = "" 

    for key , item in country_dict.items( ) :

        if item[ search_key ] > max :
            max = item[ search_key ]
            max_key = key 

    return max_key 

def find_top( country_dict , num , search_key ) :

    for i in range( num ) :

        max = 0 
        max_key = "" 

        for key , item in country_dict.items( ) :

            if item[ search_key ] > max :
                max = item[ search_key ]
                max_key = key 

        print( f"{ i + 1 }. - { max_key } - { country_dict[ max_key ][ search_key ] }")
        country_dict.pop( max_key )




country_dict = dict( )

POPULATION_KEY = 0 
ANIMALS_DENS_KEY = 1 
PLANTS_DENS_KEY = 2
GREEN_INDEX_KEY = 3


with open( "population.txt" , "r" ) as population_file :

    for line in population_file :
        line = line.rstrip( )
        country , population = line.split( ";" ) 
        country_dict[ country ] = [ int(  population ) , 0 , 0 , 0 ] 

with open( "animal_plant_count.txt" , "r" ) as data_file :

    for line in data_file :
        line = line.rstrip( )
        country , num_animals , num_plants = line.split( ";" ) 
        num_animals = int( num_animals )
        num_plants = int( num_plants )
        country_dict[ country ][ ANIMALS_DENS_KEY ] = num_animals / country_dict[ country ][ POPULATION_KEY ]
        country_dict[ country ][ PLANTS_DENS_KEY ] = num_plants / country_dict[ country ][ POPULATION_KEY ]
        country_dict[ country ][ GREEN_INDEX_KEY ] = ( country_dict[ country ][ ANIMALS_DENS_KEY ] + country_dict[ country ][ PLANTS_DENS_KEY ] ) / 2 * 100

max_animals_key = find_max( country_dict , ANIMALS_DENS_KEY )
max_plants_key = find_max( country_dict , PLANTS_DENS_KEY )

print( f"The country with highest density of animals is: { max_animals_key } with { country_dict[ max_animals_key ][ ANIMALS_DENS_KEY ] }")
print( f"The country with highest density of plants is: { max_plants_key } with { country_dict[ max_plants_key ][ PLANTS_DENS_KEY ] }")
find_top( dict( country_dict ) , 3 , GREEN_INDEX_KEY )

print( country_dict )

