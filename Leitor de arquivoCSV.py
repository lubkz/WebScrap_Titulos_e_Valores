import pandas as pd

arquivo = "C:/Users/Lucass/Downloads/customers-100.csv"

df = pd.read_csv(arquivo)

df["Status"] = ""

df.loc[df["Subscription Date"] < "2021-01-01", "Status"] = "Antigo"
df.loc[df["Subscription Date"] > "2021-01-01", "Status"] = "Novo"

df.to_csv("C:/Users/Lucass/Downloads/customers_atualizado.csv", index=False)

print(df)


