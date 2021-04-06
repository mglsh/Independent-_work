
import pandas as pd
import matplotlib.pyplot as plt
print('start')
# Красиві графіки
plt.style.use('ggplot')
# Розмір зображень
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('la-crimes.csv', sep=',', encoding='latin1', dayfirst=True,
                       parse_dates=['Date Occurred'],
                       index_col='Date Occurred'
                       )


print(fixed_df[:0])
print('It is')
fixed_df['DR Number'].plot()
plt.show()
