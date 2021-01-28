import numpy as np


def result_table(dfs_merged_clean, country):
    """
    Application of filters and aggregation functions to get the final df which is the information we were required
    to extract.
    """

    filter_country = dfs_merged_clean['Country'] == country
    filter_rural = dfs_merged_clean['Living Zone'] == 'Rural'
    filter_job = dfs_merged_clean['Full Time Job'] == 'Yes'

    if country == None:

        filter_full = filter_rural & filter_job
        df_filtered = dfs_merged_clean[filter_full]

        result = df_filtered.groupby(['Country', 'Job Title', 'Living Zone'],
                                           as_index=False)['Quantity'].agg(np.sum)

        result['Percentage'] = (result['Quantity'] / len(result['Quantity']) * 100).round(2)

        result.to_csv('./data/result/df_rural.csv', index=False)

    elif country is not None:

        filter_full = filter_country & filter_rural & filter_job
        df_filtered = dfs_merged_clean[filter_full]

        result_country = df_filtered.groupby(['Country', 'Job Title', 'Living Zone'],
                                           as_index=False)['Quantity'].agg(np.sum)
        result_country['Percentage'] = (result_country['Quantity'] / len(result_country['Quantity']) * 100).round(2)

        result_country.to_csv(f'./data/result/df_rural_{country}.csv', index=False)




