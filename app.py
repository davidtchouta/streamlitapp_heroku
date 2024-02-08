from pycaret.regression import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
import math

model = load_model('gradboostregModel')

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['prediction_label'][0]
    return predictions


def run():

    from PIL import Image
    image = Image.open('im.png')
    image_hospital = Image.open('chu.png')

    #st.image(image,use_column_width=60)
    st.image(image, width=380)
     

    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))

    st.sidebar.info('Cette application est conçue pour prédire les frais d\'assurance maladie')
    st.sidebar.success('https://www.pycaret.org')
    
    st.sidebar.image(image_hospital)

    st.title("Estimez vos frais d'assurance Maladie")

    if add_selectbox == 'Online':

        age = st.number_input('Age', min_value=1, max_value=100, value=25)
        sex = st.selectbox('Sex', ['male', 'female'])
        bmi = st.number_input('BMI', min_value=10, max_value=50, value=10)
        children = st.selectbox('Children', [0,1,2,3,4,5,6,7,8,9,10])
        if st.checkbox('Smoker'):
            smoker = 'yes'
        else:
            smoker = 'no'
        region = st.selectbox('Region', ['southwest', 'northwest', 'northeast', 'southeast'])

        output=""

        input_dict = {'age' : age, 'sex' : sex, 'bmi' : bmi, 'children' : children, 'smoker' : smoker, 'region' : region}
        input_df = pd.DataFrame([input_dict])

        if st.button("Predict"):
            output = predict(model=model, input_df=input_df)
            #output = '$ ' + str(output)
            output_in_thousands = math.ceil(output / 1000)
            # Convertir output en nombre entier et formater avec séparateur de milliers
            output = f"$ {output:,.0f}"  # Formaté en dollars avec séparateur de milliers
            
        
        st.success(f'The output is {output}')
        #st.success('The output is {}'.format(output))
   
    if add_selectbox == 'Batch':

        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])

        if file_upload is not None:
            data = pd.read_csv(file_upload)
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)

if __name__ == '__main__':
    run()

	# Utiliser HTML pour ajouter de l'espace vertical
    st.markdown('<br>' * 5, unsafe_allow_html=True)  # Ajustez le nombre 5 selon l'espace souhaité
    st.markdown('<p style="font-size: 15px;">Site modifié par David TCHATCHOUA </p>', unsafe_allow_html=True)