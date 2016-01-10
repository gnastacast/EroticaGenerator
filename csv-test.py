import csv
import StringIO
import os
from MarkovChain import MarkovChain

def parse_porn_csv(csv_file, title_index):
    markov_db_filename = './{csv}_markov_db'.format(csv=csv_file)
    if os.path.isfile('./{csv}_markov_db'.format(csv=csv_file)):
        return MarkovChain(markov_db_filename)
    porn_titles = StringIO.StringIO()
    with open(csv_file) as porn_csv:
        reader = csv.DictReader(porn_csv, delimiter='|', fieldnames=[
            'iframe', 'thumbnail', 'samples', 'title', 'tags', 'more_tags', 'unknown', 'length','views','likes','dislikes'
        ])
        for row in reader:
            porn_titles.write(row['title'] + '.')
    mc = MarkovChain(markov_db_filename)
    mc.generateDatabase(porn_titles.getvalue())
    mc.dumpdb()
    return mc

if __name__ == '__main__':
    mc = parse_porn_csv('pornhub.com-db.csv', 4)
    for i in range(100):
        print(mc.generateString())