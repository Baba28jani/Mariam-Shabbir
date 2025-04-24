import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(page_title="File converter", layout ="wide")
st.title("File converter & cleaner")
st.write("Upload csv or excel files, clean data, and convert formats.")

files = st.file_uploader("Upload CSV or Excel files ." , type=["csv", "xlsx"], accept_multiple_files=True)

if files:
    for file in files :
        ext = file.name.split(".")[-1].lower()
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"{file.name} = Preview")
        st.dataframe(df.head())

        if st.checkbox(f"Remove Duplicates = (file.name)"):
            df = df.drop_duplicates()
            st.success("Duplicates Removed")
            st.dataframe(df.head())

            if st.checkbox(f"Fill Missing values = {file.name}"):
               df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
            st.success("Missing values filled with  mean")
            st.dataframe(df.head())

            selected_columns =st.multiselect(f"Select Columns - {file.name}" , df.columns, default=df.columns)
            df = df[selected_columns]
            st.dataframe(df.head())
            if st.checkbox(f"Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
                  st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])
                

            format_choice = st.radio(f"Convert {file.name} to:", ["csv", "Excel"], key=file.name)
            if st.button(f"Download {file.name} as {format_choice}"):
                    output = BytesIO()
                    if format_choice == "csv":
                        df.to_csv(output, index=False)
                        mine = "text/csv"
                        new_name = file.name.replace(ext, "csv")

                    else:
                        df.to_excel(output, index=False, engine='openpyxl')
                        mine = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        new_name = file.name.replace(ext, "xlsx")

                    output.seek(0)
                    st.download_button(
    label=f"Download {file.name} as {format_choice}",
    data=output,
    file_name=new_name,
    mime=mine
)

            st.success("Processing Complete!")