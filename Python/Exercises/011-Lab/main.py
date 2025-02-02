

def find_and_print_highest( list_of_tuples , top = 1 , text = "") :


    for j in range( top ) :        
        max = 0 
        max_idx = 0 
        for i , item in enumerate( list_of_tuples ) :

            if item[ 1 ] > max :
                max = item[ 1 ]
                max_idx = i 

        print( f"The item with { text } is { list_of_tuples[ max_idx ][ 0 ] } with { list_of_tuples[ max_idx ][ 1 ]}" )
        list_of_tuples.pop( max_idx )


        


country_dict= dict( )
animals_density_list = list( )
plants_density_list = list( )
green_index_list = list()

with open( "population.txt" ) as pop_file :

    for line in pop_file :
        line = line.rstrip( ) 
        country , population = line.split( ";" ) 
        population = int( population )
        country_dict[ country ] = population

    
with open( "animal_plant_count.txt" , "r" ) as other_file :

    for line in other_file :
        line.rsplit( )
        country , num_animals , num_plants = line.split( ";" ) 
        num_animals = int( num_animals )
        num_plants = int( num_plants )

        animals_density = num_animals / country_dict[ country ]
        plants_density = num_plants / country_dict[ country ]
        green_index = ( animals_density + plants_density ) / 2 * 100 

        animals_density_list.append( ( country , animals_density ) ) 
        plants_density_list.append( ( country ,  plants_density ) ) 
        green_index_list.append( ( country , green_index ) ) 


print( animals_density_list )

"""
find_and_print_highest( animals_density_list , top = 1 , text = "animal density")
find_and_print_highest( plants_density_list , top = 1 , text = "plant density" )
find_and_print_highest( green_index_list , top = 3 )
"""





