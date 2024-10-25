import matplotlib as plt
#Display 3 plot with the temperature forecast for Lisbon, new york and Sydney for the
days = [1, 2, 3, 4, 5]
Lisbon = [10, 12, 14, 16, 18]
New_York = [20, 22, 24, 26, 28]
Sydney = [30, 32, 34, 36, 38]
plt.plot(days, Lisbon, label='Lisbon')
plt.plot(days, New_York, label='New York')
plt.plot(days, Sydney, label='Sydney')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.title('Temperature forecast')
plt.legend()
iris_df['species']