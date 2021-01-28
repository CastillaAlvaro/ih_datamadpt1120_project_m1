def build_data(dfs_merged):

    """
    Applying different methods in order to clean our DataFrame.
    """

    dfs_merged['Quantity'] = 1

    dfs_merged.rename(columns={'id': 'Id',
                               'gender': 'Gender',
                               'country_code': 'Country Code',
                               'living_zone': 'Living Zone',
                               'age': 'Age',
                               'age_group': 'Age Group',
                               'children': 'Children',
                               'education_level': 'Education Level',
                               'full_time_job': 'Full Time Job',
                               'job_code': 'Job Code',
                               'answer_awareness': 'Qs_Awareness',
                               'answer_vote': 'Qs_Vote',
                               'answer_effect': 'Qs_Effect',
                               'answer_arguments_for': 'Qs_Arguments For',
                               'answer_arguments_against': 'Qs_Arguments Against',
                               'title': 'Job Title'}, inplace=True)

    columns = ['Id',
               'Gender',
               'Country Code',
               'Country',
               'Living Zone',
               'Age',
               'Age Group',
               'Children',
               'Education Level',
               'Full Time Job',
               'Job Title',
               'Job Code',
               'Qs_Awareness',
               'Qs_Vote',
               'Qs_Effect',
               'Qs_Arguments For',
               'Qs_Arguments Against',
               'Quantity']

    dfs_merged['Id'] = [id.split('-0a81e8b09a82')[0] if '-0a81e8b09a82' in id else id for id in dfs_merged['Id']]

    dfs_merged['Gender'].replace({'male': 'Male', 'female': 'Female', 'FeMale': 'Female', 'Fem': 'Female'},
                                 inplace=True)

    dfs_merged['Living Zone'].replace(
        {'urban': 'Urban', 'city': 'City', 'rural': 'Rural', 'countryside': 'CountrySide'},
        inplace=True)

    dfs_merged['Age Group'].replace({'juvenile': '0_13'}, inplace=True)

    dfs_merged['Children'].replace({'yES': 'Yes', 'YES': 'Yes', 'nO': 'No', 'NO': 'No'}, inplace=True)

    dfs_merged['Education Level'].replace({'medium': 'Medium', 'high': 'High', 'low': 'Low', 'no': 'No'}, inplace=True)

    dfs_merged['Full Time Job'].replace({'yes': 'Yes', 'no': 'No'}, inplace=True)

    dfs_merged['Qs_Effect'].replace({'‰Û_ spend more time with my family': 'Spend more time with my family',
                                     '‰Û_ gain additional skills': 'Gain additional skills',
                                     '‰Û_ look for a different job': 'Look for a different job',
                                     '‰Û_ work less': 'Work less',
                                     '‰Û_ do more volunteering work': 'Do more volunteering work',
                                     '‰Û_ work as a freelancer': 'Work as a freelancer',
                                     '‰Û_ stop working': 'Stop working'}, inplace=True)

    dfs_merged = dfs_merged[columns]
    dfs_merged.to_csv('./data/processed/dfs_merged.csv', index=False)

    return dfs_merged
