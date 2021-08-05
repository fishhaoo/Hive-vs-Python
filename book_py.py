import time
import pandas as pd

start_time = time.time()
data = pd.read_csv('C:/Users/Rapid/Documents/Downloads/Books.csv', header=None)
data = data.rename(columns={0: 'BookId', 1: 'UserId', 2: 'Rating', 3: 'Timestamp'})
print(data.head())
time_load = time.time() - start_time
print("--- %.2fs seconds ---" % time_load)


''' Example 1 : compare the number of books in each rating group'''

# start counting time 
start_time = time.time()

#obtain the average rating and store to the new copy of data
avg_rating = data.groupby(data['BookId']).mean()[['Rating']]
avg_rating['BookId'] = avg_rating.index
avg_rating.reset_index(drop=True, inplace=True)

rating_0 = []
rating_1 = []
rating_2 = []
rating_3 = []
rating_4 = []
rating_5 = []

for i, value in avg_rating.iterrows():
    r = avg_rating['Rating'].iloc[i] 
    if r < 1:
        rating_0.append(avg_rating.iloc[i])
    if r>=1 and r<2:
        rating_1.append(avg_rating.iloc[i])
    if r>=2 and r<3:
        rating_2.append(avg_rating.iloc[i])
    if r>=3 and r<4:
        rating_3.append(avg_rating.iloc[i])
    if r>=4 and r<5:
        rating_4.append(avg_rating.iloc[i])
    else: 
        rating_5.append(avg_rating.iloc[i])
        
time_avg_rating = time.time() - start_time
print("--- %.2fs seconds ---" % time_avg_rating)



''' Example 2 : reviews per user '''

# start_time = time.time()
# rpu = data.groupby(data['UserId']).agg(['count'])
# time_rpu = time.time() - start_time
# print("--- %.2fs seconds ---" % time_rpu)

# print(rpu.head())

start_time = time.time()
group = data.groupby('UserId')
ct = group['BookId'].count()
print(ct.head(5))
time_new_rpu = time.time() - start_time
print("--- %.2fs seconds ---" % time_new_rpu)
