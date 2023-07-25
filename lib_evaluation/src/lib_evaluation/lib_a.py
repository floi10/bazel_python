import pandas as pd


def get_df():
    return pd.DataFrame(
        data={
            "timestamp": [1.0, 2.0, 3.0],
            "lat": [8.0, 9.0, 10.0],
            "lon": [48.0, 49.0, 50.0]
        }
    )