
def proportion_by_sport(df, year, sport, gender):
    df_filter = df[(df['Year'] == year) & (df['Sport'] == sport)]