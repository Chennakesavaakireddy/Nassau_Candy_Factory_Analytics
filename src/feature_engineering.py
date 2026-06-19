import pandas as pd


def prepare_data(df):

    df["Order Date"]=pd.to_datetime(

    df["Order Date"]

    )

    df["Ship Date"]=pd.to_datetime(

    df["Ship Date"]

    )

    df["Lead_Time"]=(

    df["Ship Date"]

    -

    df["Order Date"]

    ).dt.days

    df["Profit Margin"]=(

    df["Gross Profit"]

    /

    df["Sales"]

    )

    return df