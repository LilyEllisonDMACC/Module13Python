import csv
import matplotlib.pyplot as plt

# Initialize three empty lists
county_label,county_population,county_num_households = ([] for i in range(3))
with open('Example CSV(1).csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        # skip the first line in the file because it is the header
        if line_count == 0:
            line_count += 1
            continue
        county_label.append(row[0])
        county_population.append(int(row[1].replace(",", ""))) #removes commas when adding to list
        county_num_households.append(int(row[2].replace(",",""))) #removes commas when adding to list

# plot_count just has a list of numbers based on how many points are being plotted
plot_count = []
for v in range(len(county_label)):
    plot_count.append(v)

# Bar chart of population by county
plt.bar(plot_count, county_population, color='red')
# line chart of number of households by county
plt.plot(plot_count, county_num_households, color='green')
# Override plot_count values with proper labels
plt.xticks(plot_count, county_label)
# chart title
plt.title('County Population and Number of Households')
# chart x-axis label
plt.xlabel('County')
# chart y-axis label
plt.ylabel('Population/Num Households')