from pandas import read_csv
from bar_chart_race import bar_chart_race
from matplotlib.pyplot import rcParams
def summary(values, ranks):
    all_gdp = int(values.sum())
    ranks_gdp = ranks.sort_values().index
    s = f"总gdp为:{all_gdp},最高为:{ranks_gdp[-1]},最低为:{ranks_gdp[0]}"
    return {"x":.99,"y":.05,"s":s,"ha":"right","size":18}

rcParams["font.sans-serif"] = ["Arial Unicode MS"]
rcParams['axes.unicode_minus'] = False
df = read_csv("data/分省年度数据.csv", index_col=["时间"])
bar_chart_race(df, "分省年度数据.mp4", figsize=(16, 9),
               title="近20年各省gdp数据", steps_per_period=60,
               period_label={"x":.99,"y":.1,"ha":"right","size":18},
               period_summary_func=summary)
print("导出完成")









