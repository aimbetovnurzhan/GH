import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    ban_map = users.set_index('users_id')['banned']
    is_not_banned = (trips['client_id'].map(ban_map) == 'No') & \
                    (trips['driver_id'].map(ban_map) == 'No')
    df = trips[is_not_banned].copy()
    df = df[df['request_at'].between('2013-10-01', '2013-10-03')]
    if df.empty:
        return pd.DataFrame(columns=['Day', 'Cancellation Rate'])
    
    result = df.groupby('request_at').apply(
        lambda x: round(
            (x['status'] != 'completed').sum() / len(x),
            2
        )
    ).reset_index()
    result.columns = ['Day', 'Cancellation Rate']
    return result


    # trips['canceled'] = ((trips['status'] != 'completed') & (trips['baninfo'] == 'ok')).groupby(trips['Day']).transform('sum')
    # trips.groupby('Day').apply(lambda x: ((x['status'] != 'completed') & (x['baninfo'] == 'ok')).sum()).reindex(trips['Day']).values

    # trips['all_by_date'] = (trips['baninfo'] == 'ok').groupby(trips['Day']).transform('sum')
    # trips.groupby('Day')['baninfo'].transform(lambda x:  (x == 'ok').sum())
    # print(val1)
