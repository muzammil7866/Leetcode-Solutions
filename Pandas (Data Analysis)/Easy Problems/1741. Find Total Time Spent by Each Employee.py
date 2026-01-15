df['total_time'] = df['out_time'] - df['in_time']
df = df.groupby(['event_day', 'emp_id'], as_index = False).sum()
df.drop(columns = ['in_time', 'out_time'], inplace = True)
df.rename(columns = {'event_day': 'day'}, inplace = True)