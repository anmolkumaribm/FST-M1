import pandas

dataframe = pandas.read_csv("sample.csv")

print("Usernames:")
print(dataframe["Usernames"])

print("username and password of the second row")
print("Username: ", dataframe["Usernames"][1], " | ", "Password: ", dataframe["Passwords"][1])

print("Usernames column in ascending orde")
print(dataframe.sort_values('Usernames'))

print("Passwords column in descending order")
print(dataframe.sort_values('Passwords', ascending=False))