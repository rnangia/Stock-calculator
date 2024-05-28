import json
import pandas as pd

with open("close_stat.json") as f:
    close_stat = json.load(f)
# print(data["IFL"])

av_overall = pd.read_json("av_overall.json").T
# print(av_overall)

av_per_change_c2c = pd.read_json("av_per_change_c2c.json").T
# print(av_per_change_c2c)

av_per_change_low = pd.read_json("av_per_change_low.json").T
# print(av_per_change_low)

av_vol = pd.read_json("av_vol.json").T
# print(av_vol)

prob_neg = pd.read_json("prob_neg.json").T

correlations = pd.read_json("correlations.json").T

vol_correlations = pd.read_json("volatility_correlations.json").T

print(correlations)
# Finding top 10 volatile stocks over entire lifetime
top10vol = av_vol.nlargest(10, 'mean')
print("Top 10 volatile stocks over lifetime\n", top10vol)

# Finding top 10 negative returning Stocks
top10neg = prob_neg.nlargest(10, 'prob')
print("Top 10 negative returning stocks", top10neg)

with open("close_stat_ss.json") as f:
    close_stat_ss = json.load(f)
# print(data["IFL"])

av_overall_ss = pd.read_json("av_overall_ss.json").T
# print(av_overall_ss)

av_per_change_c2c_ss = pd.read_json("av_per_change_c2c_ss.json").T
# print(av_per_change_c2c_ss)

av_per_change_low_ss = pd.read_json("av_per_change_low_ss.json").T
# print(av_per_change_low_ss)

av_vol_ss = pd.read_json("av_vol_ss.json").T
# print(av_vol_ss)

prob_neg_ss = pd.read_json("prob_neg_ss.json").T

top10volss = av_vol_ss.nlargest(10, 'mean')
print("Top 10 volatile stocks over last 2 quarters\n", top10volss)

# Finding top 10 negative returning Stocks
top10negss = prob_neg_ss.nlargest(10, 'prob')
print("Top 10 negative returning stocks over last 2 quarters", top10negss)
