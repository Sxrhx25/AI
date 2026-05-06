import streamlit as st




X = df.iloc[:, :-1].values
Y = df.iloc[:, -1].values
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,t
