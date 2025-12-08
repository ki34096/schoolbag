import re
import os
from datetime import datetime

INPUT_FOLDER = "matches"
OUTPUT_FOLDER = "matches"

def normalize_field(value):
    return value.strip().replace("  ", " ")

def extract_coordinates(text):
    # ищем формат 38.26695, -0.66333
    match = re.search(r"([-+]?\d+\.\d+)[,\s]+([-+]?\d+\.\d+)", text)
    if match:
        return match.group(1), match.group(2)
    return "", ""

def convert_file(filename):
    path = os.path.join(INPUT_FOLDER, filename)
    with open(path, "r", encoding="utf-8") as f:
        data = f.read()

    # match title
    title_line = re.search(r"(.+vs.+)", data, re.IGNORECASE)
    match_name = normalize_field(title_line.group(1)) if title_line else "Unknown vs Unknown"

    teams = re.split(r"vs|VS|Vs", match_name)
    home = normalize_field(teams[0])
    away = normalize_field(teams[1])

    # date
    date_line = re.search(r"(\d{4}-\d{2}-\d{2})", data)
    date = date_line.group(1) if date_line else ""

    # time & timezone
    time_line = re.search(r"(\d{2}:\d{2}).*UTC([+-]\d+)", data)
    kickoff = time_line.group(1) if time_line else ""
    timezone = "UTC" + time_line.group(2) if time_line else ""

    # coordinates
    lat, lon = extract_coordinates(data)

    # weather
    weather_eng = "Unknown"
    temp = ""
    weather_note = ""

    if "солне" in data.lower():
        weather_eng = "Clear"
        weather_note = "sunny"
    if "обла" in data.lower():
        weather_eng = "Cloudy"
        weather_note = "cloudy"

    temp_line = re.search(r"(\+?\d+)°", data)
    if temp_line:
        temp = temp_line.group(1)

    # build standardized file
    match_id = f"{home[:3].upper()}-{away[:3].upper()}-{date.replace('-', '')}"

    output = f"""# MATCH INFO
Match_ID: {match_id}
Match: {match_name}
Tournament: La Liga
Stage: Regular season

Date: {date}
Kickoff_local: {kickoff}
Timezone: {timezone}

Stadium:
City:
Location: {lat}, {lon}

Weather: {weather_eng}
Temperature_C: {temp}
Weather_note: {weather_note}

# TEAMS
HomeTeam: {home}
AwayTeam: {away}

# SCORE
FinalScore:
"""

    out_name = filename.replace(".txt", "_formatted.txt")
    out_path = os.path.join(OUTPUT_FOLDER, out_name)

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output)

    return out_name


def main():
    for file in os.listdir(INPUT_FOLDER):
        if file.endswith(".txt") and "_formatted" not in file:
            new_file = convert_file(file)
            print(f"Converted: {file} -> {new_file}")

if __name__ == "__main__":
    main()

