import streamlit as st
from snowflake.snowpark.context import get_active_session
import snowflake.snowpark.exceptions

session = get_active_session()

@st.cache_data()
def get_usage():
    usage_query = f"""
    INSERT INTO STREAMLIT_DB.SIS.SIS_USAGE (TS, DB_NAME, SCH_NAME, STREAMLIT_APP, USER_NAME)
    VALUES
        (CURRENT_TIMESTAMP(), '{session.get_current_database().replace('"', ""}', '{session.get_current_schema().replace('"', "")}', 'EXAMPLE_SIS_APP', '{st.experimental_user["user_name"]}' )
    """

    try:
        usage_data = session.sql(usage_query).collect()
        st.success("Data was written to the SIS_USAGE table.")
    except:
        st.error("Data was not written to the SIS_USAGE table.")

def main():
    st.title("Example Streamlit App")

    get_usage()

main()
