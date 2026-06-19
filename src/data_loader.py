import pandas as pd


def load_data():

    df=pd.read_csv(

    "data/Nassau_Candy_Distributor.csv"

    )

    mapping=pd.read_csv(

    "data/product_factory_mapping.csv"

    )

    df=df.merge(

    mapping,

    on=[

    "Division",

    "Product Name"

    ],

    how="left"

    )

    return df,mapping