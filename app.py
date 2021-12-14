import streamlit as st

st.title("Carbon calculator")
st.image("download.png")
st.write("If you are a Non-vegetarian then input 1 else 2")
food = st.number_input("Food",1,3)
carbon_emission=0.0
family_members=st.number_input("Enter family members",1,20)
calories=st.number_input("Enter avg calories",1.0,100000.0)
driven_miles=st.number_input("Enter avg kms driven in a year",0,10000)
household_utilities=st.number_input("Enter number of household utilities \nThey include 1)Electricity \n2)Natural Gas \n3)Fuel \n4)oil",1,5)
total_expenditures=st.number_input("Enter total expenditures spent after the utilities",1,1000000)
if(food==1):
    carbon_emission += (calories*0.01)*family_members
else:
    carbon_emission += (calories*0.005)*family_members

if(driven_miles>0):
    carbon_emission += driven_miles*0.01
else:
    st.write("Enter valid kms driven")
if(family_members>0 and household_utilities>0 and total_expenditures>0):
    carbon_emission += (0.12*total_expenditures)*household_utilities

carbon_emission += ((0.12*total_expenditures)*household_utilities)*family_members
st.write("Your carbon emissions are "+str(carbon_emission)+" metric tonnes . ")