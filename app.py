{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ab1bf37c",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install prediction\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "02d8c327",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from sklearn import preprocessing\n",
    "import pickle \n",
    "import numpy as np\n",
    "# from prediction import predict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0192423f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Title\n",
    "st.title(\"Stroke Prediction\")\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "67758573",
   "metadata": {},
   "outputs": [],
   "source": [
    "# model=pickle.load(open('rf_model','rb'))\n",
    "# encoder_dict = pickle.load(open(\"pd.get_dummies\",'rb'))\n",
    "\n",
    "\n",
    "# def_main():\n",
    "# Selection og gemder\n",
    "gender=st.selectbox(\"Gender:\", \n",
    "                    ['Male','Female','Others'])\n",
    "st.write(\"Your gender is:\", gender)\n",
    "\n",
    "#age\n",
    "age=st.text_input(\"Enter your age\", \"Enter a valid number.\")\n",
    "\n",
    "\n",
    "#hypertension\n",
    "hypertension=st.selectbox(\"Do you have hypertension:\",\n",
    "                         [0,1])\n",
    "heart_disease=st.selectbox(\"Do you have any heart disease:\",\n",
    "                          [0,1])\n",
    "ever_married=st.selectbox(\"Are you married:\",['Yes','No'])\n",
    "work_type=st.selectbox(\"Work Type:\",\n",
    "                      ['Private','Self_employed','Govet_job','Never_worked','children'])\n",
    "Residence=st.selectbox(\"Residence:\",['Rural','Urban'])\n",
    "avg_glucose_level=st.text_input(\"Enter avg_glucose_level\",'Enter a valid value')\n",
    "smoking_status=st.selectbox(\"Smkoing Status:\",\n",
    "                            ['formerly smoked','never smoked','smokes','Unknown'])\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "77e4a949",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-04-23 18:43:34.861 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Admin\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.button(\"Predict\")\n",
    "#     stroke=rf_model\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b496ef05",
   "metadata": {},
   "outputs": [],
   "source": [
    "# def predict(arr):\n",
    "#     # Load the model\n",
    "#     with open('final_model.sav', 'rb') as f:\n",
    "#         model = pickle.load(f)\n",
    "#     classes = {0:'No Stroke',1:'Stroke'}\n",
    "#     # return prediction as well as class probabilities\n",
    "#     preds = model.predict_proba([arr])[0]\n",
    "#     return (classes[np.argmax(preds)], preds)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b47f985a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install model_methods"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "48893ca8",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "# from model_methods import predict\n",
    "# classes = {0:'No Stroke',1:'Stroke'}\n",
    "# class_labels = list(classes.values())\n",
    "# st.title(\"Stroke or no stroke\")\n",
    "# st.markdown('**Objective** : Given details about the flower we try to predict the species.')\n",
    "# st.markdown('The model can predict if it belongs to the following three Categories : **setosa, versicolor, virginica** ')\n",
    "# def predict_class():\n",
    "#     data = list(map(float,['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',\n",
    "#        'work_type', 'Residence_type', 'avg_glucose_level','smoking_status']))\n",
    "#     result, probs = predict(data)\n",
    "#     st.write(\"The predicted class is \",result)\n",
    "#     if st.button(\"Predict\"):\n",
    "#         predict_class()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e6a18004",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
