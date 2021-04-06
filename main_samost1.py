import pandas as pd
import matplotlib.pyplot as plt

print('start')
# Красиві графіки
plt.style.use('ggplot')
# Розмір зображень
plt.rcParams['figure.figsize'] = (15, 5)

fixed_df = pd.read_csv('la-crimes.csv', sep=',', encoding='latin1',
                       parse_dates=['Date Reported'], dayfirst=True,
                       index_col='Date Reported', )

print('Завдання 1')  # Завдання №1
compile_count = fixed_df['Crime Code Description'].value_counts()
print(compile_count[:10])
compile_count[:10].plot(kind='bar')
plt.show()

print('Завдання 2')  # Завдання №2
t2 = fixed_df[['Crime Code Description', 'Victim Sex']][:10].copy()
print(t2)
print(t2.groupby('Victim Sex').sum())

print('Завдання 3')  # Завдання №3
t3 = fixed_df['Victim Descent'].value_counts()
print(t3[:1])



#fixed_df[['Crime Code Description', 'Victim Sex']].plot(kind='bar')
#plt.show()
# fixed_df['DR Number'].plot()
# plt.show()
