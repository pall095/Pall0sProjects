from scholarly import scholarly
import pandas as pd

QUERY = 'allintitle: ("trust" OR "automation" OR "ai" OR "calibration" OR "practical" OR "artificial intelligence" OR "experimental")'
MAX_RESULTS = 200

rows = []

search_query = scholarly.search_pubs(QUERY)
num_accepted = 0 
num_check = 0 
num_excluded = 0 

for i in range(MAX_RESULTS):
    try:
        result = next(search_query)
    except StopIteration:
        break

    bib = result.get("bib", {})

    year = bib.get("pub_year")
    citations = result.get("num_citations", 0)

    # --- make sure values are usable ---
    try:
        year = int(year)
    except (TypeError, ValueError):
        year = None

    citations = int(citations) if citations is not None else 0

    if year is None:
        exclude = "true"   # or decide differently
        num_excluded += 1 
    
    elif year < 2010 or citations < 50:
        exclude = "yes"
        num_excluded += 1 

    elif 2010 <= year <= 2015 and citations >= 150 :
        exclude = "check"
        num_check += 1 
    
    else:
        exclude = "no"
        num_accepted += 1 

    rows.append({
        "Author": bib.get("author"),
        "Title": bib.get("title"),
        "Year": year,
        "Num Citations": citations,
        "Exclude": exclude
    })

output = pd.DataFrame(rows)

output.to_excel("reuslts.xlsx", index=False)
print( f"Num Accepted: { num_accepted }" )
print( f"Num Check: { num_check }" )
print( f"Num Excluded: { num_excluded }" )