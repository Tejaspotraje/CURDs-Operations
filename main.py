import mysql.connector
import streamlit as st

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="Hero@3189",
      database="crud_new1"
  )
mycursor = mydb.cursor()
print("Connected successfully.")

def main():
    st.title("CRUDs operations with mysql")
    options=st.sidebar.selectbox("Select an operation",("Create","Read","Update","Delete"))
    if options=="Create":
        st.subheader("Create Record")
        name=st.text_input("Enter Name")
        email=st.text_input("Enter Email")
        if st.button("Create"):
            sql="insert into user(name,email) values(%s,%s)"
            val=(name,email)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record created Successfully")

    elif options=="Read":
        st.subheader("Read Record")
        mycursor.execute("select*from user")
        result=mycursor.fetchall()
        for row in result:
            st.write(row)

    elif options=="Update":
        st.subheader("Update Record")
        id=st.number_input("Enter the id")
        name=st.text_input("Enter the new name")
        email=st.text_input("Enter the new Email")
        if st.button("Update"):
            sql="update user set name=%s,email=%s,id=%s"
            val=(name,email,id)
            mycursor.execute(sql,val) 
            mydb.commit()
            st.success("Record Updated Successfully")

    elif options=="Delete":
        st.subheader("Delete Record")
        id=st.number_input("Enetr the id")
        if st.button("Delete"):
            sql="delete from user where id=%s"
            val=(id,)
            mycursor.execute(sql,val)
            mydb.commit()
            st.success("Record deleted Sucessfully")
if __name__ == "__main__":
    main()