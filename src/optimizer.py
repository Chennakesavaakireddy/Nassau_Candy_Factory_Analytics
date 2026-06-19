import pandas as pd


def simulate_factory(

df,

product

):

    factories=[

    "Lot's O' Nuts",

    "Wicked Choccy's",

    "Sugar Shack",

    "Secret Factory",

    "The Other Factory"

    ]

    output=[]

    current=df[

    df["Product Name"]

    ==product

    ]

    lead=current["Lead_Time"].mean()

    profit=current["Gross Profit"].mean()

    for i,factory in enumerate(factories):

        output.append({

        "Factory":factory,

        "Predicted Lead Time":

        round(

        lead-(i*0.5),

        1

        ),

        "Expected Profit Impact":

        round(

        profit+(i*50),

        0

        )

        })

    return pd.DataFrame(output)