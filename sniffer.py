import csv
import StringIO
import os
from MarkovChain import MarkovChain

def sniff_porn_csv(csv_file, title_index):
	porn_titles = StringIO.StringIO()
	with open(csv_file) as porn_csv:
		dialect = csv.Sniffer().sniff(porn_csv.read(1024))
		porn_csv.seek(0)
		#reader = csv.DictReader(porn_csv, dialect)
		reader = csv.DictReader(porn_csv, delimiter='|', fieldnames=[
			'iframe', 'thumbnail', 'samples', 'title', 'tags', 'more_tags', 'unknown', 'length','views','likes','dislikes'
		])
		print(reader.fieldnames)
		for row in reader:
			print(row)
			porn_titles.write(row['title'] + '.')
			break
		
	return

if __name__ == '__main__':
    mc = sniff_porn_csv('Data/pornhub.com-db.csv', 4)