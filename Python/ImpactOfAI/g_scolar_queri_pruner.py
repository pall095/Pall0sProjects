from scholarly import scholarly
import pandas as pd
import time
import random

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
    except Exception as e:
        print(f"Error fetching result {i}: {e}")
        time.sleep(20)
        continue

    # -----------------------------
    # HUMAN-LIKE DELAY
    # -----------------------------
    delay = random.uniform(3, 8)
    print(f"Sleeping for {delay:.2f} seconds...")
    time.sleep(delay)

    # occasional longer pause (simulate reading)
    if i % 10 == 0 and i != 0:
        long_delay = random.uniform(15, 30)
        print(f"Long pause: {long_delay:.2f} seconds...")
        time.sleep(long_delay)

    bib = result.get("bib", {})

    year = bib.get("pub_year")
    citations = result.get("num_citations", 0)

    # --- sanitize values ---
    try:
        year = int(year)
    except (TypeError, ValueError):
        year = None

    citations = int(citations) if citations is not None else 0

    # -----------------------------
    # FILTER LOGIC
    # -----------------------------
    if year is None:
        exclude = "yes"
        num_excluded += 1 
    
    elif year < 2010 or citations < 50:
        exclude = "yes"
        num_excluded += 1 

    elif 2010 <= year <= 2015 and citations >= 150:
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

# -----------------------------
# SAVE OUTPUT
# -----------------------------
output = pd.DataFrame(rows)
output.to_excel("results.xlsx", index=False)

# -----------------------------
# SUMMARY
# -----------------------------
print("\n--- SUMMARY ---")
print(f"Num Accepted: {num_accepted}")
print(f"Num Check: {num_check}")
print(f"Num Excluded: {num_excluded}")
print(f"Total collected: {len(rows)}")