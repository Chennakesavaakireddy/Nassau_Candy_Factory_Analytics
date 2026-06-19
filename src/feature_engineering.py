import pandas as pd


def prepare_data(df):

    # Convert dates safely

    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce"
    )

    # Remove invalid dates

    df = df.dropna(
        subset=[
            "Order Date",
            "Ship Date"
        ]
    )

    # Lead time

    df["Lead_Time"] = (

        df["Ship Date"]

        - df["Order Date"]

    ).dt.days

    # Remove negative lead times

    df = df[

        df["Lead_Time"] >= 0

    ]

    # Profit Margin

    df["Profit Margin"] = (

        df["Gross Profit"]

        /

        df["Sales"]

    )

    # Handle division by zero

    df["Profit Margin"] = (

        df["Profit Margin"]

        .replace(

            [float("inf"), -float("inf")],

            0

        )

        .fillna(0)

    )

    return df
