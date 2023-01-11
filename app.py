import streamlit as st

  
import gspread 

import pandas as pd

sa = gspread.service_account(filename='authcred.json')
sh = sa.open("fddetails")

wks = sh.worksheet("Sheet1")
# print(wks.get_all_records())

df=pd.DataFrame(wks.get_all_records())

st.title("FD App")

st.write("## Enter FD Details")

fdForOptions=['','PAPA','MUMMY','MANOJ','ANU','KANCHU']

fdForName=st.selectbox("FD For", fdForOptions)

initialValue=st.text_input("Enter Initial Value")

interestRate=st.text_input("Enter Interest Rate")

maturityValue=st.text_input("Enter Maturity Value")

bankOptions=['','Utkarsk Bank']

bankName=st.selectbox("Select Bank", bankOptions)

fdOpeingdate=st.date_input("Select Opeing date")

fdMaturitydate=st.date_input("Select Maturity date")

fdNo=st.text_input("Enter FD No")

result=st.button('SAVE')

st.markdown("---")

#https://www.markdownguide.org/cheat-sheet/
st.markdown(">Papa")

st.table(df)
#https://katex.org/docs/supported.html



