
import streamlit as st
import pandas as pd
import altair as alt

from src.classes.DdManager import DbManager


INVESTMENT_TYPE = "Investments"
LIQUIDITY_TYPE = "Liquitidy"


@st.cache_resource
def get_db_manager():
    return DbManager("entries_test.csv")


def main():

    st.title("Financial Statistics")

    manager = get_db_manager()

    df = manager.db_frame.copy()

    # ---------------------------------------------------------
    # Prepare data
    # ---------------------------------------------------------

    df["date"] = pd.to_datetime(df["date"])
    df["amount"] = pd.to_numeric(df["amount"])

    # If there are multiple entries for the same source/date,
    # keep the last one.
    df = (
        df.sort_values("date")
        .drop_duplicates(
            subset=["date", "source"],
            keep="last"
        )
    )

    # ---------------------------------------------------------
    # Total wealth
    # ---------------------------------------------------------

    st.header("Total wealth")

    total_df = (
        df.groupby("date")["amount"]
        .sum()
        .sort_index()
    )

    st.line_chart(
        total_df,
        y_label="€"
    )

    # ---------------------------------------------------------
    # Investments
    # ---------------------------------------------------------

    st.header("Investments")

    investments = df[
        df["type"] == INVESTMENT_TYPE
    ]

    investment_sources = sorted(
        investments["source"].unique().tolist()
    )

    selected_investments = st.multiselect(
        "Investment sources",
        investment_sources,
        default=investment_sources
    )

    if selected_investments:

        investment_df = investments[
            investments["source"].isin(selected_investments)
        ]

        # Convert to wide format
        investment_chart = (
            investment_df
            .pivot_table(
                index="date",
                columns="source",
                values="amount",
                aggfunc="last"
            )
            .sort_index()
        )

        # Calculate total from selected sources only
        investment_chart["Total investments"] = (
            investment_chart[selected_investments]
            .sum(axis=1)
        )

        # Convert back to long format for Altair
        investment_long = (
            investment_chart
            .reset_index()
            .melt(
                id_vars="date",
                var_name="source",
                value_name="amount"
            )
        )

        # Separate source lines from total
        source_lines = (
            alt.Chart(
                investment_long[
                    investment_long["source"] != "Total investments"
                ]
            )
            .mark_line()
            .encode(
                x=alt.X("date:T", title=None),
                y=alt.Y("amount:Q", title="€"),
                color=alt.Color(
                    "source:N",
                    title="Investment source"
                ),
                tooltip=[
                    alt.Tooltip("date:T", title="Date"),
                    alt.Tooltip("source:N", title="Source"),
                    alt.Tooltip("amount:Q", title="Amount", format=",.2f")
                ]
            )
        )

        # Total gets its own series
        total_line = (
            alt.Chart(
                investment_long[
                    investment_long["source"] == "Total investments"
                ]
            )
            .mark_line(
                strokeWidth=3
            )
            .encode(
                x="date:T",
                y="amount:Q",
                color=alt.value("black"),
                tooltip=[
                    alt.Tooltip("date:T", title="Date"),
                    alt.Tooltip("amount:Q", title="Total", format=",.2f")
                ]
            )
        )

        st.altair_chart(
            source_lines + total_line,
            use_container_width=True
        )

    else:
        st.info("Select at least one investment source.")

    # ---------------------------------------------------------
    # Liquidity
    # ---------------------------------------------------------

    st.header("Liquidity")

    liquidity = df[
        df["type"] == LIQUIDITY_TYPE
    ]

    liquidity_sources = sorted(
        liquidity["source"].unique().tolist()
    )

    selected_liquidity = st.multiselect(
        "Liquidity sources",
        liquidity_sources,
        default=liquidity_sources
    )

    if selected_liquidity:

        liquidity_df = liquidity[
            liquidity["source"].isin(selected_liquidity)
        ]

        # Convert to wide format
        liquidity_chart = (
            liquidity_df
            .pivot_table(
                index="date",
                columns="source",
                values="amount",
                aggfunc="last"
            )
            .sort_index()
        )

        # Calculate total from selected sources only
        liquidity_chart["Total liquidity"] = (
            liquidity_chart[selected_liquidity]
            .sum(axis=1)
        )

        # Convert back to long format for Altair
        liquidity_long = (
            liquidity_chart
            .reset_index()
            .melt(
                id_vars="date",
                var_name="source",
                value_name="amount"
            )
        )

        # Source lines
        source_lines = (
            alt.Chart(
                liquidity_long[
                    liquidity_long["source"] != "Total liquidity"
                ]
            )
            .mark_line()
            .encode(
                x=alt.X("date:T", title=None),
                y=alt.Y("amount:Q", title="€"),
                color=alt.Color(
                    "source:N",
                    title="Liquidity source"
                ),
                tooltip=[
                    alt.Tooltip("date:T", title="Date"),
                    alt.Tooltip("source:N", title="Source"),
                    alt.Tooltip("amount:Q", title="Amount", format=",.2f")
                ]
            )
        )

        # Total line
        total_line = (
            alt.Chart(
                liquidity_long[
                    liquidity_long["source"] == "Total liquidity"
                ]
            )
            .mark_line(
                strokeWidth=3
            )
            .encode(
                x="date:T",
                y="amount:Q",
                color=alt.value("black"),
                tooltip=[
                    alt.Tooltip("date:T", title="Date"),
                    alt.Tooltip("amount:Q", title="Total", format=",.2f")
                ]
            )
        )

        st.altair_chart(
            source_lines + total_line,
            use_container_width=True
        )

    else:
        st.info("Select at least one liquidity source.")


if __name__ == "__main__":
    main()
