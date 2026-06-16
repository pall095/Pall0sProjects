import pandas as pd
import pandasql


GROUP_DF = pd.read_csv(r"csv_files\GROUP.csv")
GUIDE = pd.read_csv(r"csv_files\GUIDE.csv")
GUIDED_TOUR = pd.read_csv(r"csv_files\GUIDED_TOUR.csv")
TOUR_TYPE = pd.read_csv(r"csv_files\TOUR_TYPE.csv")

POINT_A = pandasql.sqldf(
    """
    WITH MonumentSummary AS ( 
        SELECT
            TR.Monument,
            COUNT(*) AS NumVisits,
            SUM(G.NumberParticipants) AS TotalVisitors
        FROM TOUR_TYPE AS TR
        JOIN GUIDED_TOUR AS GR
            ON GR.TourTypeCode = TR.TourTypeCode
        JOIN GROUP_DF AS G
            ON G.GRCode = GR.GRCode
        GROUP BY TR.Monument
    ) 

    SELECT VM.Monument
    FROM MonumentSummary AS VM
    WHERE VM.NumVisits >= 10
      AND VM.TotalVisitors = (
            SELECT MAX(TotalVisitors)
            FROM MonumentSummary
            WHERE NumVisits >= 10
      )
    """,
    globals()
)

print(POINT_A)