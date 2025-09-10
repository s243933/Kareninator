import pandas as pd
import os
import streamlit as st



col1,col2 = st.columns(2)

def showPhoto(photo, pathsImages):
    filename = os.path.basename(photo)
    col1.subheader(f"{st.session_state.counter+1}/{len(pathsImages)}")
    col1.image(photo, caption=f"{filename}")
    # col1.write(f"Index as a session_state attribute: {st.session_state.counter}")
    
    ## Increments the counter to get next photo
    st.session_state.counter += 1
    if st.session_state.counter >= len(pathsImages):
        st.write("You have rated all images. Thank you!")
        st.session_state.counter = len(pathsImages) - 1  # Prevent going out of bounds


def store_rating(photo, rating, pathsImages):
    st.session_state['current_rating'] = rating
    st.session_state['current_photo'] = photo

    st.session_state['data'].append({"Image": os.path.basename(photo), "Rating": rating})

    showPhoto(photo, pathsImages)

    

# Get list of images in folder
folderWithImages = r"C:\Users\desus\OneDrive - Danmarks Tekniske Universitet\Fall_2025\Cognitive_Modelling\Kareninator\data"
pathsImages = [os.path.join(folderWithImages,f) for f in os.listdir(folderWithImages)]

# col1.subheader("List of images in folder")
# col1.write(pathsImages)

if 'counter' not in st.session_state:
    col1.write("Click the button to start the rating process...")
    st.session_state.counter = 0

# Select photo a send it to button
photo = pathsImages[st.session_state.counter]
col2.subheader("Rate the image")

def get_data():
    if 'data' not in st.session_state:
        st.session_state['data'] = []
    return st.session_state['data']

# rating = col2.text_input("Rating (0-5)")
rating = col2.slider("foo", 0, 5)



show_btn = col2.button("Show next pic ⏭️",on_click=store_rating,args=([photo, rating, pathsImages]))

# if show_btn and 0 <= int(rating) <= 5:
#     photoname = os.path.basename(photo)
#     get_data().append({"Image": photoname, "Rating": rating})
# else:
#     col2.warning("Please enter a valid rating between 0 and 5.")

rating_df = pd.DataFrame(get_data())
print(rating_df)