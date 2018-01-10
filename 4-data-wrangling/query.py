"""
Queries
"""

import csv, sqlite3

def number_of_nodes():
	result = cur.execute('SELECT COUNT(*) FROM nodes')
	return result.fetchone()[0]

def number_of_ways():
	result = cur.execute('SELECT COUNT(*) FROM ways')
	return result.fetchone()[0]

def number_of_unique_users():
	result = cur.execute('SELECT COUNT(DISTINCT(e.uid)) \
            FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways) e')
	return result.fetchone()[0]

def top_contributing_users():
	users = []
	for row in cur.execute('SELECT e.user, COUNT(*) as num \
            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
            GROUP BY e.user \
            ORDER BY num DESC \
            LIMIT 10'):
		users.append(row)
	return users

if __name__ == '__main__':

	con = sqlite3.connect("./suginami_tokyo.db")
	cur = con.cursor()

	print "Number of unique users: " , number_of_unique_users()
	print "Number of nodes: " , number_of_nodes()
	print "Number of ways: " , number_of_ways()
	print "Top contributing users: " , top_contributing_users()
