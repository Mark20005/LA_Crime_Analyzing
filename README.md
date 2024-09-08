![Los Angeles skyline](la_skyline.jpg)

Los Angeles, California 😎. The City of Angels. Tinseltown. The Entertainment Capital of the World! 

Known for its warm weather, palm trees, sprawling coastline, and Hollywood, along with producing some of the most iconic films and songs. However, as with any highly populated city, it isn't always glamorous and there can be a large volume of crime. That's where you can help!

You have been asked to support the Los Angeles Police Department (LAPD) by analyzing crime data to identify patterns in criminal behavior. They plan to use your insights to allocate resources effectively to tackle various crimes in different areas.

## The Data

They have provided you with a single dataset to use. A summary and preview are provided below.

It is a modified version of the original data, which is publicly available from Los Angeles Open Data.

# crimes.csv

| Column     | Description              |
|------------|--------------------------|
| `'DR_NO'` | Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits. |
| `'Date Rptd'` | Date reported - MM/DD/YYYY. |
| `'DATE OCC'` | Date of occurrence - MM/DD/YYYY. |
| `'TIME OCC'` | In 24-hour military time. |
| `'AREA NAME'` | The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles. |
| `'Crm Cd Desc'` | Indicates the crime committed. |
| `'Vict Age'` | Victim's age in years. |
| `'Vict Sex'` | Victim's sex: `F`: Female, `M`: Male, `X`: Unknown. |
| `'Vict Descent'` | Victim's descent:<ul><li>`A` - Other Asian</li><li>`B` - Black</li><li>`C` - Chinese</li><li>`D` - Cambodian</li><li>`F` - Filipino</li><li>`G` - Guamanian</li><li>`H` - Hispanic/Latin/Mexican</li><li>`I` - American Indian/Alaskan Native</li><li>`J` - Japanese</li><li>`K` - Korean</li><li>`L` - Laotian</li><li>`O` - Other</li><li>`P` - Pacific Islander</li><li>`S` - Samoan</li><li>`U` - Hawaiian</li><li>`V` - Vietnamese</li><li>`W` - White</li><li>`X` - Unknown</li><li>`Z` - Asian Indian</li> |
| `'Weapon Desc'` | Description of the weapon used (if applicable). |
| `'Status Desc'` | Crime status. |
| `'LOCATION'` | Street address of the crime. |

## Exploratory Data Analysis (EDA) of Crimes Dataset
This section contains the Exploratory Data Analysis (EDA) conducted on the crimes dataset to identify trends and patterns in crime occurrences based on time and location.

## Crimes by Hour
`Description`:
This plot illustrates the number of crimes committed throughout the day, categorized by the victim's sex (`M` - Male, `F` - Female, `X` - Unknown, `H` - Hypothetical). The X-axis represents the hours of the day, while the Y-axis shows the count of crimes.

`Analysis`:
The plot reveals that the highest crime activity occurs at noon (`12 PM`), with significant peaks for both male and female victims. During the early morning hours (`0–6 AM`), crime activity is significantly lower but gradually increases towards noon. After noon, crime occurrences rise again and remain relatively high until late evening. This suggests that the majority of crimes happen during the day or evening, potentially indicating busier times when people are more active.
![Crimes by hour](Plots/plot_2024-09-08%2014-37-26_0.png)
## Crimes by Area Name
`Description`:
This plot shows the number of crimes in different areas, broken down by the victim's sex. Each bar represents a specific area, with color coding indicating the victim's sex (`F` - Female, `M` - Male, `X` - Unknown, `H` - Hypothetical).

`Analysis`:
The `Central` area displays the highest crime rate among all victim categories, particularly for female victims. Other areas, such as `Hollywood`, `Southwest`, and `Olympic`, also exhibit high crime rates. This indicates that certain areas have a higher crime rate, possibly due to factors such as higher population density or socio-economic conditions. Analyzing these patterns can help in understanding crime dynamics and focusing law enforcement efforts in areas with elevated crime rates.
![Crimes by Area Name](Plots/plot_2024-09-08%2014-37-26_1.png)

## Crimes per Age Group
`Description`:
This plot visualizes the density of crimes committed across different victim age groups. A kernel density estimate (KDE) plot is used to display the distribution of crimes for various age groups of victims. The X-axis represents the age of the victims(`0-17`,`18-25`,`26-34`,`35-44`,`45-54`,`55-64`, `65+`), while the Y-axis shows the density of crimes.

`Analysis`:
The `KDE` plot reveals how crime occurrences are distributed among different age groups. Peaks in the plot at `26-34` and `18-25` groups indicate that this age groups are in higher crime densities, showing which age ranges are more susceptible to being victims of crimes. This information can be valuable for understanding crime patterns based on age and can help in tailoring preventive measures or policies for different age demographics.
![Crimes per Age Group](Plots/plot_2024-09-08%2014-37-26_3.png)