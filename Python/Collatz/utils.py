def normalizeSeries( series , wanted_max ):
    
    max_series = max( series )
    normalized_series = [ ]
    
    for number in series:
        
        normalized_series.append( number / max_series * wanted_max )

    return normalized_series  
    
    