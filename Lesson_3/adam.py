questions = [
    "1. What is the average number of kills per player level?",
    "2. How does total damage correlate with total kills?",
    "3: Total bomb plants and defuses by map",
    "4. What is the average headshot percentage for players with more than 20 kills?",
    "5. Which map has the highest average number of kills per match?",
    "6. What is the distribution of player levels?",
    "7. Do players with more assists tend to have more kills?",
    "9. Which player has the highest headshot percentage?",
    "10. What is the average number of rounds played per match per map?"
    ]

import polars as pl

df = pl.read_csv("Data/csgo_data.csv")

# avg_kills_per_player = (df.group_by("vlLevel")
#      .agg(pl.col("qtKill").mean().alias("Average_Kills_Per_Player"))
# )
# print(avg_kills_per_player)


# correlation = df.select(pl.corr("vlDamage","qtKill").alias("correlation"))
# print("\n Question 2: Correlation between total damge and total kills:")
# print(correlation)


# Total_bomb_plants = (df.group_by("descMapName")
# .agg([pl.col("qtBombePlant").sum().alias("Total_bomb_plants"), pl.col("qtBombeDefuse").sum().alias("Total_bomb_Defuse")])
# )

# print("\n Question 1:Total bomb plants and defuses by map?")
# print(Total_bomb_plants)
#qtBombeDefuse

# avg_headshot_percentage_20 = (
#     df.filter(pl.col("qtKill") >= 20)
#     .select(pl.col("qtHs").mean().alias("Average_Headshot_Percentage"))
# )
# print(avg_headshot_percentage_20)


# map_with_avg_kills = (df.group_by("descMapName").agg(pl.col("qtKill").mean().alias("map_with_avg_kills"))).sort("map_with_avg_kills", descending = True)
# print("\n Which map has the highest average number of kills per match?")
# print(map_with_avg_kills)


# correlation = df.select(pl.corr("qtAssist","qtKill").alias("correlation"))
# print("\n Question 7: Do players with more assists tend to have more kills?")
# print(correlation)

# avg_number_of_deaths = (df.group_by("qtDeath")
#     .agg(pl.col("qtClutchWon").mean().alias("Average_Kills_Per_Player"))
# )
# print(avg_number_of_deaths)

# highest_headshot_percentage = (df.group_by("idPlayer").agg(pl.col("qtHs").mean().alias("highest_headshot_percentage"))).sort("highest_headshot_percentage", descending = True)
# print("\n Which player has the highest headshot percentage?")

# print(highest_headshot_percentage)


avg_number_of_rounds_played_per_match_per_map = (df.group_by("descMapName")
     .agg(pl.col("qtRoundsPlayed").mean().alias("avg_number_of_rounds_played_per_match_per_map"))
 )
print(avg_number_of_rounds_played_per_match_per_map)