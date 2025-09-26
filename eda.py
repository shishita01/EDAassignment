import pandas as pd
import zipfile
import docx
import matplotlib.pyplot as plt







# extract problem statement
zip_path = r"DSassignment4/EDA - Module 3 (1).zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    print("Files in the zip archive:", z.namelist())


    docx_file = 'EDA - Assignments/Problem Statement/DS Internship - EDA - ProblemStatement.docx'
    
    with z.open(docx_file) as f:
        doc = docx.Document(f)
        
        for para in doc.paragraphs:
            print(para.text)




print("\n")


# extract and read sales data
zip_path = r"DSassignment4/EDA - Module 3 (1).zip"

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extract('EDA - Assignments/Data/DS Internship - EDA - Data.xlsx', path='.')

file_path = 'EDA - Assignments/Data/DS Internship - EDA - Data.xlsx'


sales = pd.read_excel(file_path)

print(sales.head(10))




# Group sales by year
sales_by_year = sales.groupby("Year")["Sales"].sum().reset_index()

print("Total Sales by Year:")
print(sales_by_year)

# Plotting for better understanding
plt.figure(figsize=(8,5))
plt.bar(sales_by_year["Year"], sales_by_year["Sales"], color="skyblue")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.title("Total Sales by Year")
plt.show()





# Convert Store Modification Date to datetime
sales["Store Modification Date"] = pd.to_datetime(sales["Store Modification Date"], errors="coerce")


openings = sales[sales["Store Modification"].str.lower() == "opening"]

openings["Opening Year"] = openings["Store Modification Date"].dt.year

stores_1991 = openings[openings["Opening Year"] == 1991]["Store"].nunique()

print("Number of stores opened in 1991:", stores_1991)





# Filter rows where store modification contains 'remodel'
remodels = sales[sales["Store Modification"].str.lower().str.contains("remodel", na=False)]

remodelled_stores = remodels["Store"].nunique()

print("Number of stores remodelled during this period:", remodelled_stores)





# Calculate correlation
correlation = sales["Sales"].corr(sales["Total Sq Ft"])
print("Correlation between Sales and Total Sq. Ft.:", correlation)

# Scatter plot
plt.figure(figsize=(7,5))
plt.scatter(sales["Total Sq Ft"], sales["Sales"], alpha=0.3, color="purple")
plt.xlabel("Total Sq. Ft.")
plt.ylabel("Sales")
plt.title("Relationship between Sales and Store Size")
plt.show()





# Group sales by Super Division
sales_by_division = sales.groupby("Super Division")["Sales"].sum().reset_index()


most_profitable = sales_by_division.sort_values(by="Sales", ascending=False).head(1)

print("Total Sales by Super Division:")
print(sales_by_division)
print("\nMost Profitable Super Division:")
print(most_profitable)

# Bar plot
plt.figure(figsize=(8,5))
plt.bar(sales_by_division["Super Division"], sales_by_division["Sales"], color="orange")
plt.xlabel("Super Division")
plt.ylabel("Total Sales")
plt.title("Sales by Super Division")
plt.xticks(rotation=45)
plt.show()





# Identify closed stores
closed_stores = sales[sales["Store Modification"].str.lower().str.contains("close", na=False)]["Store"].unique()

# All unique stores in the dataset
all_stores = sales["Store"].unique()

# Active stores are those not in the closed stores list
active_stores = set(all_stores) - set(closed_stores)

print("Number of active stores as of today:", len(active_stores))






# Average sq. ft by Super Division
sqft_by_division = sales.groupby("Super Division")["Total Sq Ft"].mean().reset_index()


max_sqft_division = sqft_by_division.sort_values(by="Total Sq Ft", ascending=False).head(1)

print("Average Sq. Ft by Super Division:")
print(sqft_by_division)
print("\nSuper Division with highest average Sq. Ft:")
print(max_sqft_division)


plt.figure(figsize=(8,5))
plt.bar(sqft_by_division["Super Division"], sqft_by_division["Total Sq Ft"], color="green")
plt.xlabel("Super Division")
plt.ylabel("Average Sq. Ft")
plt.title("Average Store Size by Super Division")
plt.xticks(rotation=45)
plt.show()





# Total sales by state
sales_by_state = sales.groupby("State")["Sales"].sum().reset_index()


top_states = sales_by_state.sort_values(by="Sales", ascending=False).head(3)

print("Top 3 potential states for new stores:")
print(top_states)

plt.figure(figsize=(7,5))
plt.bar(top_states["State"], top_states["Sales"], color="teal")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.title("Top 3 States for New Stores")
plt.show()





# Total sales by month
sales_by_month = sales.groupby("Month")["Sales"].sum().reset_index()


best_month = sales_by_month.sort_values(by="Sales", ascending=False).head(1)

print("Sales by Month:")
print(sales_by_month)
print("\nBest time of year to open a store (highest sales month):")
print(best_month)


plt.figure(figsize=(8,5))
plt.plot(sales_by_month["Month"], sales_by_month["Sales"], marker="o", color="red")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Sales Trend by Month")
plt.xticks(range(1,13))
plt.show()





# Filter closures
closures = sales[sales["Store Modification"].str.lower().str.contains("close", na=False)]

closures_by_outlet = closures.groupby("Outlet Type")["Store"].nunique().reset_index()
closures_by_outlet.rename(columns={"Store": "Closed Stores"}, inplace=True)

print("Closures by Outlet Type:")
print(closures_by_outlet)


plt.figure(figsize=(7,5))
plt.bar(closures_by_outlet["Outlet Type"], closures_by_outlet["Closed Stores"], color="brown")
plt.xlabel("Outlet Type")
plt.ylabel("Number of Closed Stores")
plt.title("Store Closures by Outlet Type")
plt.show()

