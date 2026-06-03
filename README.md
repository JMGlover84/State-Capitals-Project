# 🏛️ U.S. State Capitals Dataset — Python Project

A complete Python data project that compiles, structures, and geocodes all 50 U.S. state capitals into clean, reusable JSON datasets. The project is built entirely in a Jupyter Notebook and requires no external APIs or third-party libraries beyond Python's built-in `json` module.

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [How It Works — Step by Step](#how-it-works--step-by-step)
  - [Step 1: Building the Dataset](#step-1-building-the-dataset)
  - [Step 2: Writing to JSON](#step-2-writing-to-json)
  - [Step 3: Reading Back the JSON](#step-3-reading-back-the-json)
  - [Step 4: Adding Geographic Coordinates](#step-4-adding-geographic-coordinates)
  - [Step 5: Merging Coordinates into the Dataset](#step-5-merging-coordinates-into-the-dataset)
  - [Step 6: Exporting the Final Dataset](#step-6-exporting-the-final-dataset)
- [Output Files](#output-files)
- [Data Schema](#data-schema)
- [Python Concepts Used](#python-concepts-used)
- [How to Run](#how-to-run)
- [Example Output](#example-output)
- [Potential Extensions](#potential-extensions)

---

## Project Overview

This project answers a common data question: *What are all 50 U.S. state capitals, where are they located, and what are their addresses?* Rather than downloading a pre-made dataset, this project constructs the data manually in Python, processes it using core language features, and exports it into a structured JSON format — both with and without geographic coordinates (latitude/longitude).

The result is two clean JSON files that can be used as-is for mapping applications, geography quizzes, data analysis, or as a foundation for more complex projects.

---

## Repository Structure

```
├── state_capitals_project_final.ipynb   # Main Jupyter Notebook with all code
├── state_capitals.json                  # Output: capitals with addresses only
├── state_capitals_with_geocode.json     # Output: capitals with addresses + lat/lon
└── README.md                            # This file
```

---

## How It Works — Step by Step

### Step 1: Building the Dataset

The project begins by importing Python's built-in `json` module — the only import needed for the entire project.

```python
import json
```

The core dataset is defined as a **Python list of dictionaries**. Each dictionary represents one U.S. state and contains six fields:

| Field | Description | Example |
|---|---|---|
| `state` | Full state name | `"Georgia"` |
| `capital` | Capital city name | `"Atlanta"` |
| `address` | Street address of the state capitol building | `"206 Washington St SW"` |
| `city` | City name (same as capital) | `"Atlanta"` |
| `state_abbr` | Two-letter state abbreviation | `"GA"` |
| `zip` | ZIP code of the capitol building | `"30334"` |

All 50 states are included, from Alabama to Wyoming. The data was manually researched and hardcoded directly into Python — no web scraping, no CSV imports, no external APIs. This makes the dataset fully self-contained and reproducible.

```python
state_capitals = [
    {"state": "Alabama", "capital": "Montgomery", "address": "600 Dexter Ave",
     "city": "Montgomery", "state_abbr": "AL", "zip": "36130"},
    # ... all 50 states
]
```

---

### Step 2: Writing to JSON

Once the list is built in memory, it's serialized to disk using `json.dumps()` inside a `with open()` block. The `indent=2` argument makes the output human-readable (pretty-printed).

```python
with open('state_capitals.json', 'w') as f:
    f.write(json.dumps(state_capitals, indent=2))
```

**Why this approach?**
- `with open(...) as f` is the Pythonic way to handle files — it automatically closes the file when the block exits, even if an error occurs.
- `'w'` mode creates the file if it doesn't exist or overwrites it if it does.
- `json.dumps()` converts the Python list of dicts into a JSON-formatted string. The `indent=2` parameter formats it with 2-space indentation for readability.

---

### Step 3: Reading Back the JSON

The saved JSON file is immediately read back to verify it was written correctly and to load it into a new variable for further processing.

```python
with open('state_capitals.json', 'r') as f:
    capitals = json.load(f)
```

**Key distinction — `json.load()` vs `json.loads()`:**
- `json.load(f)` reads directly from a file object and parses the JSON into a Python object (in this case, a list of dicts).
- `json.loads(s)` (note the `s`) parses a JSON *string* — used when the data is already in memory as a string.

After this step, `capitals` is a Python list identical in structure to the original `state_capitals` variable.

---

### Step 4: Adding Geographic Coordinates

A second dictionary — `coordinates` — is defined to map each capital city name to its latitude and longitude. This dictionary uses the **capital city name as the key**, making lookups fast and straightforward.

```python
coordinates = {
    "Montgomery": {"capital": "Montgomery", "latitude": 32.3668, "longitude": -86.2999},
    "Juneau":     {"capital": "Juneau",     "latitude": 58.3005, "longitude": -134.4197},
    # ... all 50 capitals
}
```

All 50 capital cities are covered. Coordinates are decimal degrees (the standard format used by mapping tools like Google Maps, Leaflet, and Mapbox).

---

### Step 5: Merging Coordinates into the Dataset

A `for` loop iterates over every state entry in `capitals` and enriches it with latitude and longitude data from the `coordinates` dictionary. The capital city name serves as the **shared key** that links the two data structures.

```python
for i in capitals:
    capital_name = i['capital']
    i['latitude'] = coordinates[capital_name]['latitude']
    i['longitude'] = coordinates[capital_name]['longitude']
```

**How this works:**
1. For each state dictionary `i` in the `capitals` list, the capital city name is extracted: `i['capital']`.
2. That name is used as a key to look up the matching entry in `coordinates`.
3. The `latitude` and `longitude` values are pulled out and added directly to the state dictionary as new key-value pairs.
4. Because Python dictionaries are mutable, this modifies each dictionary in-place — no need to create a new list.

This is a classic **dictionary lookup / data join** pattern — the same concept used in SQL joins and pandas merges, but done here with pure Python.

---

### Step 6: Exporting the Final Dataset

The enriched list — now containing all original fields plus latitude and longitude — is written to a new JSON file.

```python
with open('state_capitals_with_geocode.json', 'w') as f:
    f.write(json.dumps(capitals, indent=2))
```

This produces the final, geocoded dataset ready for use in mapping tools, data analysis, or any downstream application.

---

## Output Files

### `state_capitals.json`
Contains all 50 states with the following fields per entry:
- `state`, `capital`, `address`, `city`, `state_abbr`, `zip`

### `state_capitals_with_geocode.json`
Contains everything from the above file, plus:
- `latitude` — decimal latitude of the capital city
- `longitude` — decimal longitude of the capital city

---

## Data Schema

```json
{
  "state": "Georgia",
  "capital": "Atlanta",
  "address": "206 Washington St SW",
  "city": "Atlanta",
  "state_abbr": "GA",
  "zip": "30334",
  "latitude": 33.749,
  "longitude": -84.388
}
```

---

## Python Concepts Used

| Concept | Where Used |
|---|---|
| Lists of dictionaries | Primary data structure for the dataset |
| Dictionary key lookups | Merging coordinates using capital name as key |
| `for` loop iteration | Looping over all 50 states to add coordinates |
| In-place dictionary mutation | Adding `latitude`/`longitude` to existing dicts |
| `with open()` context manager | Safe file reading and writing |
| `json.dumps()` | Serializing Python objects to JSON strings |
| `json.load()` | Deserializing JSON files back into Python objects |
| `import json` | Python standard library — no pip install needed |

---

## How to Run

**Requirements:** Python 3.x (no external packages needed)

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/state-capitals-project.git
   cd state-capitals-project
   ```

2. Open the notebook:
   ```bash
   jupyter notebook state_capitals_project_final.ipynb
   ```

3. Run all cells top to bottom (`Kernel → Restart & Run All`).

4. Two JSON files will be created in the same directory:
   - `state_capitals.json`
   - `state_capitals_with_geocode.json`

---

## Example Output

After running the notebook, `state_capitals_with_geocode.json` will look like this (abbreviated):

```json
[
  {
    "state": "Alabama",
    "capital": "Montgomery",
    "address": "600 Dexter Ave",
    "city": "Montgomery",
    "state_abbr": "AL",
    "zip": "36130",
    "latitude": 32.3668,
    "longitude": -86.2999
  },
  {
    "state": "Alaska",
    "capital": "Juneau",
    "address": "120 4th St",
    "city": "Juneau",
    "state_abbr": "AK",
    "zip": "99801",
    "latitude": 58.3005,
    "longitude": -134.4197
  }
  ...
]
```

---

## Potential Extensions

Here are some ways this project could be expanded:

- **Interactive map** — Load `state_capitals_with_geocode.json` into Folium or Plotly to plot all 50 capitals on a map of the United States.
- **Flask/FastAPI web app** — Serve the dataset as a REST API endpoint so other apps can query capital info by state name or abbreviation.
- **Quiz generator** — Write a Python script that randomly picks states and prompts the user to name the capital.
- **Distance calculator** — Use the latitude/longitude coordinates and the Haversine formula to compute the distance between any two capitals.
- **pandas integration** — Load the JSON into a pandas DataFrame for filtering, sorting, and statistical analysis (e.g., find the northernmost or southernmost capital).
- **CSV export** — Add a step to write the data as a `.csv` file for use in Excel or Google Sheets.
