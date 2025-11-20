# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: David Reynolds
# Section: ENGR 102
# Assignment: Lab Topic 12
# Date: 19 11 2025

import csv
import datetime
import calendar
import statistics
import matplotlib.pyplot as plt

CSV_NAME = "WeatherDataCLL.csv"

def find_col_indices(header):
    # map useful keys to index by keyword matching
    h = [c.strip().lower() for c in header]
    idx = {}
    for i, col in enumerate(h):
        if "date" in col or col.startswith("day"):
            idx["date"] = i
        if "wet" in col and "bul" in col or "wetbulb" in col or "wet bulb" in col:
            idx["wetbulb"] = i
        if "press" in col:
            idx["pressure"] = i
        if "wind" in col and "speed" in col or "avgwind" in col:
            idx["wind"] = i
        if "relative" in col and "humid" in col or col == "rh" or "humidity" in col:
            idx["rh"] = i
        if "dew" in col and "point" in col or "dewpoint" in col:
            idx["dew"] = i
        if ("avg" in col and "temp" in col) or col == "avg temp" or ("temperature" in col and "avg" in col):
            idx["avgtemp"] = i
        if "high" in col and "temp" in col or col.startswith("high"):
            idx["high"] = i
        if "low" in col and "temp" in col or col.startswith("low"):
            idx["low"] = i
        if "precip" in col or "rain" in col:
            idx["precip"] = i
    return idx

def try_float(s):
    try:
        return float(s)
    except:
        return None

def take_month_from_date(s):
    s = s.strip()
    if not s:
        return None
    # try several common formats
    fmts = ("%m/%d/%Y", "%m/%d/%y", "%Y-%m-%d", "%b %d %Y", "%d-%b-%Y")
    for f in fmts:
        try:
            dt = datetime.datetime.strptime(s, f)
            return dt.month
        except:
            pass
    # fallback: split by '/' or '-' and take first token as month
    for sep in ("/", "-", " "):
        parts = s.split(sep)
        if len(parts) >= 1 and parts[0].isdigit():
            m = int(parts[0])
            if 1 <= m <= 12:
                return m
    return None

def read_info(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        idx = find_col_indices(header)
        # require at least date
        if "date" not in idx:
            raise RuntimeError("Date column not found in CSV header.")
        rows = list(reader)

    dates = []
    wetbulb = []
    pressure = []
    wind = []
    rh = []
    dew = []
    avgtemp = []
    high = []
    low = []
    precip = []

    for r in rows:
        dates.append(r[idx["date"]].strip() if idx["date"] < len(r) else "")
        def val(key):
            return try_float(r[idx[key]]) if key in idx and idx[key] < len(r) else None
        wetbulb.append(val("wetbulb"))
        pressure.append(val("pressure"))
        wind.append(val("wind"))
        rh.append(val("rh"))
        dew.append(val("dew"))
        avgtemp.append(val("avgtemp"))
        high.append(val("high"))
        low.append(val("low"))
        precip.append(val("precip"))

    return {
        "dates": dates,
        "wetbulb": wetbulb,
        "pressure": pressure,
        "wind": wind,
        "rh": rh,
        "dew": dew,
        "avgtemp": avgtemp,
        "high": high,
        "low": low,
        "precip": precip
    }

def plot_line_wetbulb_pressure(d):
    x = list(range(len(d["dates"])))
    # filter points where values exist
    wb_x, wb_y = zip(*[(i, v) for i, v in enumerate(d["wetbulb"]) if v is not None]) if any(d["wetbulb"]) else ([],[])
    p_x, p_y = zip(*[(i, v) for i, v in enumerate(d["pressure"]) if v is not None]) if any(d["pressure"]) else ([],[])
    fig, ax1 = plt.subplots()
    ax1.plot(wb_x, wb_y, color="tab:blue", label="Avg Wet Bulb (°)")
    ax1.set_xlabel("Day index")
    ax1.set_ylabel("Avg Wet Bulb", color="tab:blue")
    ax1.tick_params(axis='y', labelcolor='tab:blue')
    ax2 = ax1.twinx()
    ax2.plot(p_x, p_y, color="tab:red", label="Avg Pressure (units)")
    ax2.set_ylabel("Avg Pressure", color="tab:red")
    ax2.tick_params(axis='y', labelcolor='tab:red')
    # reduce x tick labels crowding: show date strings every N ticks if available
    if len(d["dates"]) > 0:
        step = max(1, len(d["dates"]) // 10)
        ax1.set_xticks(list(range(0, len(d["dates"]), step)))
        ax1.set_xticklabels([d["dates"][i] for i in range(0, len(d["dates"]), step)], rotation=45, ha='right')
    fig.tight_layout()
    fig.suptitle("Avg Wet Bulb and Avg Pressure over Time", y=1.02)

def plot_hist_wind(d):
    wind_vals = [v for v in d["wind"] if v is not None]
    plt.figure()
    plt.hist(wind_vals, bins=10, edgecolor='black')
    plt.xlabel("Average Wind Speed")
    plt.ylabel("Number of Days")
    plt.title("Histogram of Average Wind Speed")

def plot_scatter_rh_dew(d):
    pairs = [(r, dp) for r, dp in zip(d["rh"], d["dew"]) if r is not None and dp is not None]
    if pairs:
        x, y = zip(*pairs)
    else:
        x = y = []
    plt.figure()
    plt.scatter(x, y)
    plt.xlabel("Average Relative Humidity (%)")
    plt.ylabel("Average Dew Point")
    plt.title("Relative Humidity vs Dew Point")

def plot_monthly_stats(d):
    # aggregate by month across all years
    months = {m: {"avgtemps": [], "highs": [], "lows": [], "precips": []} for m in range(1,13)}
    for date_str, at, hi, lo, pr in zip(d["dates"], d["avgtemp"], d["high"], d["low"], d["precip"]):
        m = parse_month_from_date(date_str)
        if m is None:
            continue
        if at is not None:
            months[m]["avgtemps"].append(at)
        if hi is not None:
            months[m]["highs"].append(hi)
        if lo is not None:
            months[m]["lows"].append(lo)
        if pr is not None:
            months[m]["precips"].append(pr)

    month_names = [calendar.month_abbr[i] for i in range(1,13)]
    mean_avgtemps = []
    max_highs = []
    min_lows = []
    mean_precips = []
    for m in range(1,13):
        data = months[m]
        mean_avgtemps.append(statistics.mean(data["avgtemps"]) if data["avgtemps"] else 0)
        max_highs.append(max(data["highs"]) if data["highs"] else 0)
        min_lows.append(min(data["lows"]) if data["lows"] else 0)
        mean_precips.append(statistics.mean(data["precips"]) if data["precips"] else 0)

    x = list(range(len(month_names)))
    fig, ax1 = plt.subplots()
    bars = ax1.bar(x, mean_avgtemps, color="skyblue", label="Mean Avg Temp")
    ax1.set_xticks(x)
    ax1.set_xticklabels(month_names)
    ax1.set_ylabel("Mean Average Temperature")
    ax1.set_title("Monthly Mean Avg Temp with High/Low Range and Mean Precipitation")

    # draw error bars from mean avg temp to min/max (indicate highest high & lowest low)
    lower_err = [mean_avgtemps[i] - min_lows[i] for i in range(12)]
    upper_err = [max_highs[i] - mean_avgtemps[i] for i in range(12)]
    ax1.errorbar(x, mean_avgtemps, yerr=[lower_err, upper_err], fmt='none', ecolor='red', capsize=5, label="Low/High range")

    # precip on secondary axis
    ax2 = ax1.twinx()
    ax2.plot(x, mean_precips, color="green", marker='o', label="Mean Total Precip")
    ax2.set_ylabel("Mean Total Precipitation")
    fig.tight_layout()
    # legend combining both axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper left')

def main():
    data = read_info(CSV_NAME)
    plot_line_wetbulb_pressure(data)
    plot_hist_wind(data)
    plot_scatter_rh_dew(data)
    plot_monthly_stats(data)
    plt.show()

if __name__ == "__main__":
    main()