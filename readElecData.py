import pandas

df = pandas.read_excel("DuffieldData.xlsx")
df = df.pivot(index="pointTitle", columns="slottime_GMT", values="value")
df.to_csv("DuffieldDataPivot.csv")