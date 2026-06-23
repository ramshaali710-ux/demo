
import streamlit as st
import time

st.set_page_config(
    page_title="Loading Demo",
    page_icon="⏳"
)

st.title("⏳ Loading & Progress Demo")
st.caption("Professional loading for your apps!")

st.header("Type 1 — Simple Spinner")
if st.button("Test Spinner"):
    with st.spinner("Loading data..."):
        time.sleep(2)
    st.success("Done!")

st.divider()

st.header("Type 2 — Progress Bar")
if st.button("Test Progress Bar"):
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress.progress(i + 1)
    st.success("Complete!")

st.divider()

st.header("Type 3 — Status Messages")
if st.button("Test Status"):
    with st.status("Working...") as status:
        st.write("Searching database...")
        time.sleep(1)
        st.write("Processing results...")
        time.sleep(1)
        st.write("Almost done...")
        time.sleep(1)
        status.update(
            label="Complete!",
            state="complete"
        )
    st.success("All done!")
