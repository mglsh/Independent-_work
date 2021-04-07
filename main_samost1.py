import pandas as pd
import matplotlib.pyplot as plt

print('start')
# Красиві графіки
plt.style.use('ggplot')
# Розмір зображень
plt.rcParams['figure.figsize'] = (15, 10)

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

print('Завдання 4')  # Завдання №4
t4 = fixed_df[['Area Name', 'Reporting District']][:10].copy()
print(t4)
t41=t4.sort_values(by="Reporting District", ascending=False)
print(t41)

t4.plot('Area Name','Reporting District', kind='bar')
plt.show()
print('Завдання 5')  # Завдання №5
t5 = fixed_df[['Area Name', 'Victim Sex']][:10].copy()

print(t5.groupby('Area Name').sum())

#fixed_df[['Crime Code Description', 'Victim Sex']].plot(kind='bar')
#plt.show()
# fixed_df['DR Number'].plot()
# plt.show()
