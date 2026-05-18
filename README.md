# Steam Top Sellers Analysis

## Overview

This project analyzes Steam’s top-selling games using data collected from the Apify Steam Top Sellers Scraper.

The goal of the project is to compare active player counts between:
- Multiplayer games
- Singleplayer games
- Games with both gameplay types

The project uses Python, Pandas, Seaborn, and Matplotlib to collect, clean, and visualize Steam game data.

---

# Features

- Pulls top-selling Steam game data from Apify
- Cleans and processes the dataset
- Classifies games into gameplay categories
- Creates violin plots and boxplots
- Compares active player distributions between game types

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Apify Client

---

# Installation

Install required libraries:

```bash
pip install pandas numpy matplotlib seaborn apify-client requests
```

Or install from requirements.txt:

```bash
pip install -r requirements.txt
```

---

# Main Imports

```python
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from datetime import datetime
from pathlib import Path
from apify_client import ApifyClient
```

---

# Data Collection

The dataset is collected using the Apify Steam Top Sellers Scraper.

```python
from apify_client import ApifyClient
```

The scraper retrieves:
- top-selling Steam games
- current player counts
- genres
- review data
- pricing information

---

# Visualization

The main visualization compares active player distributions across gameplay categories using:
- violin plots
- boxplots
- bar graphs

The analysis uses:
- logarithmic scaling
- median comparisons
- distribution analysis

to better understand player engagement patterns.

---

# Example Questions

This project explores questions such as:

- Do multiplayer games have larger active player populations over singleplayer games?
- Are multiplayer games risker to release over singleplayer games?
- How do engagement patterns differ between singleplayer and multiplayer games?

---

# Project Structure

```text
Steam_top1000/
│
├── Data/
│   ├── steam_top_sellers_YYYY-MM-DD.csv
│
├── analysis.ipynb
│
├── requirements.txt
│
└── README.md
```

---

# Author

Cameron Walters