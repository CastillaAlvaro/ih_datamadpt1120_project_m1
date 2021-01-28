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
2. Argparse
3. BeautifulSoup
4. Pandas
5. Rquests
6. Numpy
7. Re



## :wrench: Configuration
Install Python 3.7 and mandatory dependencies listed before. 

If you are using the Anaconda distribution. Run the following command to activate the environment where you have all these dependencies installed.

```
conda activate name_env
```


### :see_no_evil: Usage

- Clone this repo locally.

- Open a terminal, activate the appropiate environment and navigate to the repo's path.

-  As we are using **argparse** you have to specify to parameter to run the script:
        
        '-p' '--path' (required) / '-c' '--country' (optional - Default=all)
        
                                            country_choices=['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czechia', 'Germany', 'Denmark', 'Estonia',
                                            'Spain', 'Finland', 'France','United Kingdom', 'Greece', 'Croatia', 'Hungary', 
                                            'Ireland', 'Italy', 'Lithuania','Luxembourg', 'Latvia', 'Malta','Netherlands', 
                                            'Poland','Portugal', 'Romania', 'Sweden', 'Slovenia', 'Slovakia']
                                 
                                  

### :file_folder: Folder structure
```
└── project
