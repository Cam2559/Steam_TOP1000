Steam Market Analysis: Game Performance and Market Trends

This project explores the Steam gaming market using data collected from the Steam Market Intelligence: Top Sellers & Opportunity Tracker API. The analysis examines game performance, short-term changes in the Steam market, and factors that may indicate potential market opportunities. The project demonstrates data cleaning, relational database development, SQL analysis, and data visualization using Python.

Getting Started

Clone the repository and create a virtual environment.

Windows
python -m venv .venv
.venv\Scripts\activate
Mac or Linux
python3 -m venv .venv
source .venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

Open the Jupyter Notebook to view and run the analysis.

Running the API is not required to reproduce the analysis. The data used in the project has already been collected and is included with the project, allowing the notebooks and analysis to be run without making additional API requests.

Research Questions

This analysis examines several aspects of Steam game performance, including:

What characteristics are associated with higher-performing games?
How stable are the highest-performing games across the collected snapshots?
How does player activity vary across different discount levels?
What short-term changes can be observed in the Steam market?
Which games or characteristics may indicate potential market opportunities?
Findings So Far

The analysis has identified several patterns within the collected data:

Player activity differs substantially between discount levels, but larger discounts do not consistently correspond with higher player counts.
The highest-performing games were not completely stable across the snapshots, with some games changing positions over time.
Current player counts vary considerably between games, with a relatively small number of games reaching exceptionally high player counts.
Review information, pricing, rankings, and player activity provide useful measures for comparing game performance.
The scoring and intelligence data provide additional measures for identifying games that may represent potential market opportunities.
Data

The data for this project comes from the Steam Market Intelligence: Top Sellers & Opportunity Tracker API, lokki/steam-top-sellers-scraper. The API provides information about Steam's top-selling games, including game rankings, prices, discounts, reviews, player counts, release dates, developers, publishers, genres, tags, and supported platforms.

Data was collected at multiple points during 2026 to create snapshots of the Steam market. These snapshots allow game performance and market activity to be compared over a short period of time.

The collected data was cleaned and transformed before being organized into a relational SQLite database. The database separates information about individual games from information that changes between snapshots, allowing game performance to be examined over time.

The original API is included as the data collection source, but it is not required to run the completed analysis. The project uses the previously collected data stored in the repository.

Database Structure

The project uses a relational database containing tables for:

Game
Developer
Publisher
Snapshot
GameSnapshot
Score
Intelligence
Genre
Tag
Platforms
GameGenre
GameTag
GamePlatform

The database separates information about individual games from information collected at each snapshot. GameSnapshot connects games to their snapshot-specific performance data, while the junction tables (GameGenre, GameTag, and GamePlatform) manage the many-to-many relationships between games and their genres, tags, and supported platforms.

Tools
Python
Jupyter Notebook
Pandas
NumPy
Matplotlib
Seaborn
SQLite
SQL
Steam Market Intelligence: Top Sellers & Opportunity Tracker API

AI tools were also used during development for code assistance, troubleshooting, and visualization design decisions.

Author

Cameron Walters