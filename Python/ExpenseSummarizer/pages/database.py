import streamlit as st

from src.classes.DdManager import DbManager


def main():

    st.title("Financial Database")

    manager = DbManager("entries_test.csv")

    # ---------------------------------------------------------
    # Database
    # ---------------------------------------------------------

    st.subheader("Entries")

    st.dataframe(
        manager.db_frame,
        use_container_width=True,
        height=700
    )

    # ---------------------------------------------------------
    # Cancel entry
    # ---------------------------------------------------------

    st.subheader("Cancel entry")

    dates = manager.db_frame["date"].unique().tolist()

    selected_date = st.selectbox(
        "Date",
        options=dates
    )

    types = manager.db_frame[
        manager.db_frame["date"] == selected_date
    ]["type"].unique().tolist()

    selected_type = st.selectbox(
        "Type",
        options=types
    )

    sources = manager.db_frame[
        (manager.db_frame["date"] == selected_date)
        & (manager.db_frame["type"] == selected_type)
    ]["source"].unique().tolist()

    selected_source = st.selectbox(
        "Source",
        options=sources
    )

    if st.button("Cancel entry", type="primary"):

        manager.cancel_entry(
            selected_date,
            selected_type,
            selected_source
        )

        st.success("Entry cancelled.")

        st.rerun()


if __name__ == "__main__":
    main()