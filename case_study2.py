
import base64
import json
import sys
import pandas as pd
import pprint
import streamlit as st

# about = pd.DataFrame({'Member name':['Dalveer Kaur', 'Priyanka Sharma', 'Saghithya S. Nateson','Surya Bansal','Vrajeshkumar Bhatt'],
#                                        'ID':[500208166,500208166,500203662,500210660,500209114],
#                                        'Tasks':['Coding','CLI Formatting','File Handling','Coding','Web GUI'],
#                                        'Contribution':['20%','20%','20%','20%','20%']})
st.set_page_config(
    page_title="AISC1000 Python Case Study 2",
    page_icon="🧊"
    # base="dark"
    # primaryColor="#5f9cfb"
    # backgroundColor="#011131"
    # textColor="#ffffff"
 )


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    background-repeat: no-repeat;
    }   
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background(r'bg_img.jpg')


# '''
# # Code used to store our dictionary into a txt file
# pl_dict = {
#             'joel':{'Wins':41, 'Losses':3, 'Ties':22},
#             'elizabeth':{'Wins':32,'Losses':14,'Ties': 17},
#             'mike':{'Wins':8,'Losses':19,'Ties': 11}
#             }

# json.dump(pl_dict, open("player_stats.txt",'w'))
# '''
# st.set_page_config(page_title="AISC1000 Python Case Study 2", page_icon="🐞", layout="centered")

# Reading the dictionary stored in the file


# print("\n############### GAME STATS PROGRAM ###############")

# def opt1():
#     while(True):
#         x=input("\nEnter a player name or enter 'exit' to return to options menu: ").lower().strip()
#         if(x in pl_dict.keys()):
#             print("Wins\t:",pl_dict[x]["Wins"])
#             print("Losses\t:",pl_dict[x]["Losses"])
#             print("Ties\t:",pl_dict[x]["Ties"])
#             opt1()

#         elif x=='exit':
#             options()
            
#         else:
#             print("Player does not exist in the list! Kindly enter again.")            
#             opt1()

# def opt2():
#     name = text_input("Enter player name\t: ").lower().strip()
#     while True:
#         # try:
#         #     wins = int(input("Enter player wins\t: ").strip())
#         #     loss = int(input("Enter player losses\t: ").strip())
#         #     ties = int(input("Enter player ties\t: ").strip())
#         #     break
#         # except:
#         #     print("Invalid data entered, Kindly enter numeric data.")
#         try:
#             wins = text_input("Enter player wins\t: ").strip()
#             loss = text_input("Enter player losses\t: ").strip()
#             ties = text_input("Enter player ties\t: ").strip()
#             break
#         except:
#             st.write("Invalid data entered, Kindly enter numeric data.")

#     pl_dict[name] = {'Wins':wins, 'Losses':loss, 'Ties':ties}
#     st.write('Player info added!')
#     # print('Player info added!')
#     # options()

# def opt3():
#     name=input("\nEnter a player name to delete from records or enter 'exit' to return to options menu: ").lower().strip()
#     if name=='exit':
#         options()
    
#     if(name in pl_dict.keys()):
#         confirm = input("Are you sure? enter 'yes' to proceed or 'exit' to return to options menu: ").lower().strip()
#         if confirm=='exit':
#             options()
            
#         elif confirm=='yes':
#             del pl_dict[name]
#             print(f"Player {name} record deleted! \nReturning to options menu...")
#             options()

#         elif x=='exit':
#             options()
            
#         else:
#             print("Player does not exist in the list! Kindly enter again.")
#             opt3()

    
# def options():
#     # Printing sorted names
#     print("\nPlayers list: ")
#     for key in sorted(pl_dict.keys()):
#         print("\t\t",key.capitalize())    

#     print("\nOptions: ")
#     print("1. View specific player's detailed stats")
#     print("2. Add a player to the list")
#     print("3. Delete a player from the list")
#     print("4. Credits")
#     print("5. Exit")

#     while True:
#         opt = input('\nEnter option number: ')
#         if opt == '1':
#             opt1()
#             options()
            
#         elif opt == '2':
#             opt2()
#             options()

#         elif opt == '3':
#             opt3()
#             options()

#         elif opt == '4':
#             print('\n2022S-T1 AISC1000 - Python 01\nWeek 10 - Case Study 2')
#             print('Course Professor - Mr. Qasim Ali\n')
#             credits_df = pd.DataFrame({'Member name':['Dalveer Kaur', 'Priyanka Sharma', 'Saghithya S. Nateson','Surya Bansal','Vrajeshkumar Bhatt'],
#                                        'ID':[500208166,500208166,500203662,500210660,500209114],
#                                        'Tasks':['Coding','CLI Formatting','File Handling','Coding','Web GUI'],
#                                        'Contribution':['20%','20%','20%','20%','20%']})

#             print(credits_df)
            
#         elif opt == '5' :
#             print("Saving updated player dict...")
#             json.dump(pl_dict, open("player_stats.txt",'w'))
#             print("Good Bye!")

#             sys.exit()

#         else:
#             print("Invalid input! Enter again... ")

pl_dict = json.load(open(r"player_stats.txt"))
st.session_state.data = pl_dict
# options()
def get_data():
    pl_dict = json.load(open(r"player_stats.txt"))
    return pl_dict
    
st.markdown("<h1 style='text-align: center; color: blue;'>Game Stats Program</h1>", unsafe_allow_html=True)
st.title("Python Case Study 2")

tab1, tab2, tab3 = st.tabs(["Display All Players", "Edit Player data","Credits"])

with tab1:
    if st.button('Refresh Data'):
        pl_dict = json.load(open(r"player_stats.txt"))
        st.session_state.data = pl_dict
    st.dataframe(st.session_state.data)

with tab2:
    add = st.expander("Add New Player Here")
    with add:
        form = st.form(key="add",clear_on_submit = True)
        with form:
            cols = st.columns((1,1))
            name = cols[0].text_input("Enter player name\t: ").lower().strip()
            wins = cols[1].number_input("Enter player wins\t: ",min_value = 0,step = 1)
            loss = cols[1].number_input("Enter player losses\t: ",min_value = 0,step = 1)
            ties = cols[1].number_input("Enter player ties\t: ",min_value = 0,step = 1)
            submitted = st.form_submit_button(label="Submit")

            # except:
            #     st.write("Invalid data entered, Kindly enter numeric data.")

        if submitted:
            print(type(name))
            if len(name) == 0:
                st.warning('You can not leave name empty')
            elif name.isnumeric() == True:
                st.warning('Invalid input, please try it again')
            
            else:
                pl_dict = st.session_state.data
                pl_dict[name] = {'Wins':wins, 'Losses':loss, 'Ties':ties}

                json.dump(pl_dict, open(r"player_stats.txt",'w'))
                st.session_state.data = pl_dict
                st.success('Player '+ name +' added successfully!')
                st.balloons()

    delete = st.expander("Delete player")
    with delete:
        form = st.form(key="delete", clear_on_submit = True)
        with form:
            cols = st.columns((1))
            del_name = cols[0].selectbox("Name of the Player", [ _ for _ in st.session_state.data.keys()])
            deleted = st.form_submit_button(label="Submit")
        if deleted:
            pl_dict = st.session_state.data
            del pl_dict[del_name]
            json.dump(pl_dict, open(r"player_stats.txt",'w'))
            st.session_state.data = pl_dict
            st.success('Player '+ name +' deleted successfully!')


with tab3:
    st.write(pd.DataFrame({'Member name':['Dalveer Kaur', 'Priyanka Sharma', 'Saghithya S. Nateson','Surya Bansal','Vrajeshkumar Bhatt'],
                                       'ID':[500208166,500208166,500203662,500210660,500209114],
                                       'Tasks':['Coding','CLI Formatting','File Handling','Coding','Web GUI'],
                                       'Contribution':['20%','20%','20%','20%','20%']}))
