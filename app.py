import streamlit as st
# import tomllib
# import pathlib
import gspread

import pandas as pd


# credentials = {
#     "type": st.secrets["type"],
#     "project_id": st.secrets["project_id"],
#     "private_key_id": st.secrets["private_key_id"],
#     "private_key": st.secrets["private_key"],
#     "client_email": st.secrets["client_email"],
#     "client_id": st.secrets["client_id"],
#     "auth_uri": st.secrets["auth_uri"],
#     "token_uri": st.secrets["token_uri"],
#     "auth_provider_x509_cert_url": st.secrets["auth_provider_x509_cert_url"],
#     "client_x509_cert_url": st.secrets["client_x509_cert_url"]
# }


# path = pathlib.Path(".streamlit/secrets.toml")
# tomlData= tomllib.loads(path.read_text()) 
# credentials=tomlData['credentials']

credentials=st.secrets['credentials']

sa = gspread.service_account_from_dict(credentials)

sh = sa.open("fddetails")

wks = sh.worksheet("Sheet1")
# print(wks.get_all_records())

df = pd.DataFrame(wks.get_all_records())

st.title("FD App")

st.write("## Enter FD Details")


fdForOptions = ['', 'PAPA', 'MUMMY', 'MANOJ', 'ANU', 'KANCHU']

fdForName = st.selectbox("FD For", fdForOptions)

initialValue = st.text_input("Enter Initial Value")

interestRate = st.text_input("Enter Interest Rate")

maturityValue = st.text_input("Enter Maturity Value")

bankOptions = ['', 'Utkarsk Bank']

bankName = st.selectbox("Select Bank", bankOptions)

fdOpeingdate = st.date_input("Select Opeing date").strftime("%d-%m-%Y")

fdMaturitydate = st.date_input("Select Maturity date").strftime("%d-%m-%Y")

fdNo = st.text_input("Enter FD No")

if st.button('SAVE'):
    data = [fdNo, fdOpeingdate, initialValue, interestRate,
            maturityValue, fdMaturitydate, fdForName]
    # st.write(fdOpeingdate.strftime("%d-%m-%Y"))
    n_rows, n_cols = df.shape
    row_pos = n_rows+2
    for i in range(n_cols):
        wks.update_cell(row_pos, i+1, data[i])


st.markdown("---")

# https://www.markdownguide.org/cheat-sheet/
st.markdown(">Papa")

st.table(df)
# https://katex.org/docs/supported.html
