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

# iOS
.DS_Store

# PyCharm
.idea

3. Hide credentials
4. Add some code
5. Update readme
6. Fix the code



## **Formatting**
Your readers will most likely view your README in a browser so please keep that in mind when formatting its content: 
- Use proper format when necesary (e.g.: `import pandas as pd`). 
- Categorize content using two or three levels of header beneath. 
- Make use of **emphasis** to call out important words. 
- Link to project pages for related libraries you mention. Link to Wikipedia, Wiktionary, even Urban Dictionary definitions for words of which a reader may not be familiar. Make amusing cultural references. 
- Add links to related projects or services. 

> Here you have a markdown cheatsheet [Link](https://commonmark.org/help/) and tutorial [Link](https://commonmark.org/help/tutorial/).


## **Start writing ASAP:**
*Last but not least, by writing your README soon you give yourself some pretty significant advantages. Most importantly, you’re giving yourself a chance to think through the project without the overhead of having to change code every time you change your mind about how something should be organized or what should be included.*


## **Suggested Structure:**

### :raising_hand: **Name** 
Self-explanatory names are best. If the name sounds too vague or unrelated, it may be a signal to move on. It also must be catchy. Images, Logo, Gif or some color is strongly recommended.

### :baby: **Status**
Alpha, Beta, 1.1, Ironhack Data Analytics Final Project, etc... It's OK to write a sentence, too. The goal is to let interested people know where this project is at.

### :running: **One-liner**
Having a one-liner that describes the pipeline/api/app is useful for getting an idea of what your code does in slightly greater detail. 

### :computer: **Technology stack**
Python, Pandas, Scipy, Scikit-learn, etc. Indicate the technological nature of the software, including primary programming language(s), main libraries and whether the software is intended as standalone or as a module in a framework or other ecosystem.

### :boom: **Core technical concepts and inspiration**
Why does it exist? Frame your project for the potential user. Compare/contrast your project with other, similar projects so the user knows how it is different from those projects. Highlight the technical concepts that your project demonstrates or supports. Keep it very brief.

## :wrench: Configuration
Install Python 3.7 and mandatory dependencies listed in the requirements file. 

If you are using the Anaconda distribution. Run the following command to create a new environment named "name environment here!"

```
conda env create -f requirements.yml
```

**Note:** Environment managers differ from one another. It's strongly recommended to check its documentation.

### :see_no_evil: Usage
Parameters, return values, known issues, thrown errors.

### :file_folder: Folder structure
```
└── project
