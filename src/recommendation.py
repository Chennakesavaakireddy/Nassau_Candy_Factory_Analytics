def recommend_factory(

df,

product,

region,

priority

):

    scenario=[]

    factories=[

    "Lot's O' Nuts",

    "Wicked Choccy's",

    "Sugar Shack",

    "Secret Factory",

    "The Other Factory"

    ]

    current=df[

    df["Product Name"]

    ==product

    ]

    lead=current["Lead_Time"].mean()

    profit=current["Gross Profit"].mean()

    for i,f in enumerate(factories):

        score=(

        (lead-(i*0.5))*0.6

        +

        (profit+(i*50))*0.4

        )

        scenario.append({

        "Factory":f,

        "Score":score

        })

    return sorted(

    scenario,

    key=lambda x:x["Score"],

    reverse=True

    )