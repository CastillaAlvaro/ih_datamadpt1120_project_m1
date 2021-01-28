# ih_datamadpt1120_project_m1

This project consists mainly in extracting some data from three differente sources, transforme it and be able to obtain insights.

- The first source used to retrieve some data, is a **.db file**. In this file you will find a sample of different european citizens answering several questions  related to politics. Furthermore, you will see some other relevant information such as **gender, age, country codes, level of studies, etc.** 

- The second source, is an API **(Open Skills Project)**. From this fount has been retrieved the job names that correspond to the several job codes that appear in the first source, the .db file. Otherwise, it would be difficult to understand which was the professional background of the people surveyed.

- Third source is the **Eurostat website**. In this site, it has been used some web scraping techniques in order to bring to our dataset the names of the countries, to understand from where the people surveyed come from. As mentioned before, in the first source we have the country codes, but in order to see the data more clear,it was needed to retrieve the names.




![](images/bigdata.jpeg)

---

Once checked the information provided by the API, I figured out that all job codes contained in the first dataset, were related to Data Analysis. The main **objective** was to be able to extract a table where it could be easy to see how many people living in a rural environment were employed, and what kind of profile could be found between the different countries.

## **Libraries used**
1. Sqlalchemy
2. BeautifulSoup
3. Pandas
4. Rquests
5. Numpy
6. Re



## :wrench: Configuration
Install Python 3.7 and mandatory dependencies listed before. 

If you are using the Anaconda distribution. Run the following command to activate the environment where you have all these dependencies installed.

```
conda activate name_env
```

**Note:** Environment managers differ from one another. It's strongly recommended to check its documentation.

### :see_no_evil: Usage
Parameters, return values, known issues, thrown errors.

### :file_folder: Folder structure
```
└── project
