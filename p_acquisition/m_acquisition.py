from sqlalchemy import create_engine
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

sql_query = """SELECT personal_info.uuid as id, 
gender, 
country_code, 
rural as living_zone, 
age, 
age_group,
dem_has_children as children,
dem_education_level as education_level,
dem_full_time_job as full_time_job,
normalized_job_code as job_code,
question_bbi_2016wave4_basicincome_awareness as answer_awareness,
question_bbi_2016wave4_basicincome_vote as answer_vote,
question_bbi_2016wave4_basicincome_effect as answer_effect,
question_bbi_2016wave4_basicincome_argumentsfor as answer_arguments_for,
question_bbi_2016wave4_basicincome_argumentsagainst answer_arguments_against
FROM personal_info
JOIN country_info
on country_info.uuid = personal_info.uuid
JOIN career_info
on career_info.uuid = country_info.uuid
JOIN poll_info
on poll_info.uuid = career_info.uuid"""

url_api = 'http://api.dataatwork.org/v1/jobs/'

url_eurostat = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'


def get_data(path, query):
    """
    set connection string and engine to get a pd.DataFrame from a SQL query.
    """
    engine = create_engine(f'sqlite:///{path}')

    return pd.read_sql_query(query, engine)


def acquisitionInfoApi(path, query, api_url):
    """
    connection to de API and retrieving Job Titles using job_code from df_sql_query.
    """

    df_sql_query = get_data(path, query)
    codes_to_request = df_sql_query['job_code'].unique().tolist()

    api_request = [requests.get(f'{api_url}{job_code}').json() for job_code in codes_to_request if job_code is not None]
    df_api = pd.DataFrame(api_request)

    return df_api


def acqWebScrapping(url):
    """
    acquisition with web scraping a list of countries and codes to add to our final DataFrame.
    """

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')

    full_content = soup.find('div', {'class': 'mw-content-ltr'})
    filtered_content = full_content.find_all('tr', class_=False, id=False)[0:10]

    country_name_code_lst = [str(i) for i in filtered_content]
    name_code_str = ''.join(country_name_code_lst)

    country_lst = re.findall('[A-Z][a-z]+', name_code_str)
    country_lst.remove('Kingdom')
    country_lst[-1] = 'United Kingdom'

    code_lst = re.findall('[A-Z]{2}', name_code_str)
    code_lst[1] = 'GR'
    code_lst[-1] = 'GB'

    df_countries = pd.DataFrame({'Code': code_lst, 'Country': country_lst})

    return df_countries


def acquire(path):

    print(f'Setting up the connection string and creating the engine using sqlite:///{path}...')
    df_sql_query = get_data(path, sql_query)
    print(f'Connection made and pd.DataFrame obtained!')
    df_sql_query.to_csv('./data/raw/df_sql_query.csv', index=False)

    print(f'Using the job codes to extract the different job positions names\nfrom {url_api}...')
    df_api = acquisitionInfoApi(path, sql_query, url_api)
    df_api.to_csv('./data/raw/df_api.csv', index=False)

    print(f'Retrieving from {url_eurostat}\nthe names and codes from the countries we are interested in ...')
    df_countries = acqWebScrapping(url_eurostat)
    df_countries.to_csv('./data/raw/df_countries.csv', index=False)

    first_merger = pd.merge(left=df_sql_query, right=df_api, how='left', left_on='job_code', right_on='uuid')
    dfs_merged = pd.merge(left=first_merger, right=df_countries, how='left', left_on='country_code', right_on='Code')

    return dfs_merged
