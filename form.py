import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)
from wtforms.validators import DataRequired

# Load the CSV files
train = pd.read_csv(r"C:\Users\Shahid\Desktop\flask_ml_project\data\train.csv")
val = pd.read_csv(r"C:\Users\Shahid\Desktop\flask_ml_project\data\val.csv")

# Combine datasets and drop 'price' column
X_train = pd.concat([train, val]).drop(columns='price')

# Define the form class
class InputForm(FlaskForm):
    airline = SelectField(
        label='Airline',
        choices=[(choice, choice) for choice in X_train.airline.unique()],
        validators=[DataRequired()]
    )
    date_of_journey = DateField(
        label="Date_of_journey",
        validators=[DataRequired()]
    )
    source = SelectField(
        label="Source",
        choices=[(choice, choice) for choice in X_train.source.unique()],
        validators=[DataRequired()]
    )
    destination = SelectField(
        label="Destination",
        choices=[(choice, choice) for choice in X_train.destination.unique()],
        validators=[DataRequired()]
    )
    dep_time = TimeField(
        label="Departur_Time",
        validators=[DataRequired()]
    )
    arrival_time = TimeField(
        label="Arrival_Time",
        validators=[DataRequired()]
    )
    duration = IntegerField(
        label="Duration",
        validators=[DataRequired()]
    )
    total_stops = IntegerField(
        label="Total Stops",
        validators=[DataRequired()]
    )
    additional_info = SelectField(
        label="Additional Info",
        choices=[(choice, choice) for choice in X_train.additional_info.unique()],
        validators=[DataRequired()]
    )
    submit = SubmitField('Predict')
