from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (

mean_absolute_error,

r2_score

)

import pandas as pd


def train_model(df):

    features=[

    "Sales",

    "Units",

    "Cost",

    "Gross Profit"

    ]

    X=df[features]

    y=df["Lead_Time"]

    X_train,X_test,y_train,y_test=(

    train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42

    )

    )

    model=RandomForestRegressor(

    random_state=42

    )

    model.fit(

    X_train,

    y_train

    )

    pred=model.predict(X_test)

    metrics={

    "MAE":

    mean_absolute_error(

    y_test,

    pred

    ),

    "R2":

    r2_score(

    y_test,

    pred

    )

    }

    return model,metrics