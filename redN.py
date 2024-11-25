from csv import excel

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class dataFormater:
    def __init__(self, dataset):
        self.dataset=dataset

    def prepareData(self):
        data = pd.read_excel(self.dataset)

        data['person_gender'] = data['person_gender'].map({'female': 0, 'male': 1})
        data['person_education'] = data['person_education'].map(
            {'High School': 0, 'Associate': 1, 'Bachelor': 2, 'Master': 3})
        data['person_home_ownership'] = data['person_home_ownership'].map({'RENT': 0, 'OWN': 1, 'MORTGAGE': 2})
        data['loan_intent'] = data['loan_intent'].map({'PERSONAL': 0, 'EDUCATION': 1, 'MEDICAL': 2, 'VENTURE': 3})
        data['previous_loan_defaults_on_file'] = data['previous_loan_defaults_on_file'].map({'No': 0, 'Yes': 1})
        #separar caracteristicas y etiquetas
        x = data.drop('loan_status', axis=1)
        y = data['loan_status']

        #dividir datos
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)
        x_test = scaler.transform(x_test)


"""
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Crear el modelo
model = Sequential()
model.add(Dense(12, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar el modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar el modelo
model.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))

# Evaluar el modelo
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Precisión del modelo: {accuracy*100:.2f}%')

"""