import streamlit as st
from PIL import Image
import requests
import json



st.title('Plant identification')

model = 0
class_names = 'dummy'

st.header('please upload a plant image')

with st.sidebar:
        st.image('Myplant.jpg')
        st.title("PlantMed")
        st.markdown("Identification of plant species offers important knowledge on the categorization and properties of plants. Many plants are richly having medicinal ingredients and contain medicinal active ingredients. The manual identification of medicinal plants takes time and the assistance of plant identification experts is necessary. To solve this problem, it is essential for human beings to **_automatically recognize_** and classify medicinal plants.")



file = st.file_uploader('', type=['jpeg','jpg','png'])

if file is not None:
#     image = Image.open(file).convert('RGB')
    st.image(file, use_column_width=True)

    files = {"file": file}


    res=requests.post(url='http://127.0.0.1:8000/predict',files=files)


    st.subheader(f"Potential Name of the plant = {res.text}")
    




#     class_name, conf_score = classify(image, model, class_names)

    st.write("""   """)
#     st.write("# {}".format(class_name))

    st.sidebar.success("Potential Name of the plant :  ")

