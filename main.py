import argparse
from p_acquisition.m_acquisition import acquire
from p_wrangling.m_wrangling import build_data
from p_analysis.m_analysis import result_table


def argument_parser():
    """
    parse arguments to script
    ArgumentParser -> Class
    parser -> Instance
    parser.add_argument -> method
    parse_args() -> method que parsea los argumentos
    """

    parser = argparse.ArgumentParser(description='pass the path of a database and a possible filter by country')

    parser.add_argument("-p", "--path", help="specify the path where the database is", type=str, required=True)
    parser.add_argument("-c", "--country",
                        action='store',
                        help="By default all countries. Option to choose between any contained in choices.",
                        required=False,
                        choices=['Austria', 'Belgium', 'Bulgaria', 'Cyprus', 'Czechia', 'Germany', 'Denmark', 'Estonia',
                                 'Spain', 'Finland', 'France',
                                 'United Kingdom', 'Greece', 'Croatia', 'Hungary', 'Ireland', 'Italy', 'Lithuania',
                                 'Luxembourg', 'Latvia', 'Malta',
                                 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Sweden', 'Slovenia', 'Slovakia'],
                        default=None)

    args = parser.parse_args()

    return args


def main(arguments):
    print('Starting process...')

    path = arguments.path
    country = arguments.country

    dfs_merged_raw = acquire(path)
    dfs_merged_processed = build_data(dfs_merged_raw)
    result_table(dfs_merged_processed, country)

    print('Finished process...')


if __name__ == '__main__':
    arguments = argument_parser()
    main(arguments)
