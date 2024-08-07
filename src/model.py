import pickle

def load_model():
    with open('C:/Users/Jonathan Sutton/Desktop/Machine Learning Ops & Interviews/mlops-aula02/models/model.pkl','rb') as file:
        model = pickle.load(file)
    return model


def load_encoder():
    with open('C:/Users/Jonathan Sutton/Desktop/Machine Learning Ops & Interviews/mlops-aula02/models/ohe.pkl','rb') as file:
        encoder = pickle.load(file)
    return encoder