import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns=["p","l","k"], index=["f","s"])

df1.mean().mean()
print(df1)
type(df1)
dir(df1)

print()

df2 = pandas.DataFrame([{"name":"sahil"},{"name":"ankit"}])
print(df2)

type(df2)