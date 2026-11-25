# Weather Data Analysis: speeches for 3 speakers

Each speech is about 3 to 3.5 minutes at a calm pace. The same text is in the speaker notes of each slide in Group01_Weather.pptx. Replace [Speaker 1] with your name.

## Speaker 1: dataset, method, cleaning, Task 1

*About 450 words.*

### Slide 1: Title

Good afternoon! We are Group 01, and our project is a weather data analysis of five cities in Kazakhstan. My name is [Speaker 1]. I will present the dataset, our method, the data cleaning and the first task. Then my teammates will continue with the other tasks.

### Slide 2: Our dataset

Our dataset is weather.csv. It has 1,830 rows: daily records for five cities, Almaty, Astana, Shymkent, Atyrau and Oskemen, for every day of 2024. That is 366 days per city, because 2024 was a leap year. Each row has the date, the city, the temperature in degrees Celsius, the precipitation in millimetres and the wind speed in kilometres per hour. We chose this dataset because everyone feels the weather every day, and Kazakhstan is a huge country, so the cities have very different climates.

### Slide 3: Goals and method

Our goal was to answer five questions: the average temperature for each month, which city gets the most precipitation, the temperature trend for one city, how temperature, wind and precipitation are connected, and which day had the most stable temperature in each city. We worked in five steps: load the data, clean it, analyze it with pandas and NumPy, draw charts with matplotlib, and interpret the results. All the code is in one Python script that we run in VS Code. It prints every result and saves every chart as a picture.

### Slide 4: Data cleaning

Data cleaning is the first and most important step. First, we checked missing values with isna().sum(). Our file had none, but the code is ready: if a number is missing, we fill it with the median, because the median is not affected by extreme values. Second, duplicates: one city can have only one record per day, so we drop repeated date and city pairs. We found zero. Third, outliers. We used the IQR rule with NumPy's percentile function. Q1 is the value where 25 percent of the data is lower, Q3 is where 75 percent is lower, and IQR is Q3 minus Q1. A value is an outlier if it is more than one and a half IQR below Q1 or above Q3. We found 100 outliers in precipitation, 10 in wind and none in temperature. We kept them, because they are real weather events like heavy rain or a storm, not mistakes.

### Slide 5: Task 1, average temperature by month

Task one: the average temperature for each month. We group the data by month with groupby and take the mean, and then plt.bar draws one bar for each month. July is the warmest month with 22 degrees on average, and January is the coldest with minus 3.8. December, January and February are below zero, and from May to September it is above 15 degrees. Now my teammate will continue with tasks two and three.

## Speaker 2: tools, Task 2, Task 3

*About 390 words.*

### Slide 6: Our tools, pandas, NumPy and matplotlib

Thank you. Before the next tasks, I want to explain our tools. We used three basic libraries. pandas works with the table: it reads the CSV file, groups the rows, and calculates sums, averages and correlation. NumPy does fast math on numbers: we used it to find the percentiles for outliers and the absolute value of temperature changes. matplotlib draws the charts: bar charts, line charts and scatter plots. You may ask why we did not use seaborn. Seaborn is a library on top of matplotlib that makes fancy charts shorter. But matplotlib already draws every chart we need, so there is one less library to install, and every line of our code is easy to explain. As you can see, every chart in our code follows the same five steps: create a new picture, draw the data, add a title, add labels, and save it as a PNG file. Our whole project is one script of about 120 lines that runs in VS Code.

### Slide 7: Task 2, where it rains the most

Task two: which city has the most precipitation. We group the data by city, add up all the precipitation with sum, and sort from the biggest to the smallest. Almaty is the clear winner with 597 millimetres in the year. That makes sense, because Almaty is next to the mountains, and mountains catch clouds. Second is Shymkent with 461, then Oskemen with 448 and Astana with 272. Atyrau, in the west, is the driest city: only 130 millimetres, four and a half times less than Almaty. Atyrau is in the Caspian lowland, which is semi-desert.

### Slide 8: Task 3, temperature trend in Almaty

Task three: the temperature trend for a selected city. We chose Almaty, but in the code you can change one variable, city_name, to see any other city. Daily temperature jumps a lot, so the light line is noisy. To see the real trend we used a 7-day rolling average, the dark red line. For each day it takes the average of the last seven days. The trend is a smooth wave: cold in January, rising in spring, the peak in June and July, then falling again in autumn. The hottest day in Almaty was 30.8 degrees, in June, and the coldest was minus 12.9, in January. So in one year the temperature in Almaty changes by more than 43 degrees. Now my teammate will present the last two tasks.

## Speaker 3: Task 4, Task 5, results, conclusion

*About 390 words.*

### Slide 9: Task 4, correlation

Thank you. Task four: the correlation between temperature, wind speed and precipitation. We used the Pearson correlation in pandas, with one line: df.corr(). The value goes from minus one to plus one. Plus one means two things grow together, minus one means one grows when the other falls, and zero means no connection. Temperature and wind: minus 0.15, a weak negative link, so on colder days the wind is a little stronger. Temperature and precipitation: 0.00, no link at all. Wind and precipitation: minus 0.09, also very weak. So the main insight is that these three measures are almost independent. You cannot predict rain from the temperature or the wind in this data. The scatter plot shows the same thing: the points form a big cloud with no clear line.

### Slide 10: Task 5, the most stable day

Task five: the day with the most stable temperature in each city. We have only one temperature per day, so we defined stability as the smallest change from the day before. In the code, diff() inside groupby calculates the change for each city separately, NumPy's np.abs makes it positive, and idxmin() finds the day with the smallest change. In four cities the temperature on that day did not change at all, zero degrees. For example, in Atyrau on the 6th of June it stayed at 18.9 degrees, the same as the day before. We also calculated the average daily change for each city. Oskemen has the most stable weather, with 4.96 degrees per day, and Atyrau the least stable, with 5.46.

### Slide 11: Key results

Let me summarize the key results. July is the warmest month and January is the coldest. Almaty gets the most precipitation and Atyrau is the driest. In Almaty the temperature goes from minus 12.9 to 30.8 during the year. Temperature, wind and precipitation are almost not connected. And Oskemen has the most stable day-to-day temperature.

### Slide 12: Conclusion

In conclusion, Python with just pandas, NumPy and matplotlib let us clean, analyze and visualize a whole year of weather in five cities with one short script. Our recommendations: Almaty should plan for rain and needs good drainage. Astana needs strong heating and winter planning for three months below zero. Atyrau, the driest city, should save water. In the future we would add more years and more variables, like humidity, to study climate change. Thank you for your attention! We are happy to answer your questions.
