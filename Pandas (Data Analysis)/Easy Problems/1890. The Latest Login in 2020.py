logins = logins[logins.time_stamp.dt.year == 2020].groupby('user_id', sort = False, as_index = False).max()
logins.rename(columns = {'time_stamp': 'last_stamp'}, inplace = True)