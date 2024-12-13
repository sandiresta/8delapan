import streamlit as st

st.title("About the Group")
st.write("This page provides information about the group members.")

group_members = [
    {"Name": "Ruddi Sutomi", "Role": "FMU Leader", "Email": "ruddi.sutomi@michelin.com"},
    {"Name": "Sandi Resta", "Role": "DM ZP Leader", "Email": "sandi.resta@michelin.com"},
    {"Name": "Raden Asep Ahmad Fadillah", "Role": "2W BU Leader", "Email": "raden.fadillah@michelin.com"},
]

for member in group_members:
    st.subheader(member["Name"])
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")