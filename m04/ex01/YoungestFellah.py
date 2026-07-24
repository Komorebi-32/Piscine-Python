import pandas as pandas


def youngest_fellah(df, year):
    # Filter the rows by Year. If no rows, no game
    # Retreive min Age for Sex M and Sex F
    # Store in dict and return it
    df_men = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    if df_men.shape[0] == 0:
        print("No game this year mate")
        return None
    df_women = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    min_men = int(df_men['Age'].min())
    min_women = int(df_women['Age'].min())
    res = {
        'f': min_women,
        'm': min_men
    }
    return res
