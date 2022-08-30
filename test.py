html_doc = """



"""

from bs4 import BeautifulSoup
import csv

soup = BeautifulSoup(html_doc, 'html.parser')
job_elements = soup.find_all("div", class_="two-column-container discussioncontainer")

# write to csv
with open('Manpower_Leveling.csv', mode='w') as csv_file:

	# fieldnames = ['network', 'network_num', 'name', 'address', 'post', 'date_time', 'date', 'time']
	fieldnames = ['network', 'network_num', 'name', 'date_time', 'date', 'time']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
	writer.writeheader()

	for job_element in job_elements:
		network = job_element.find(class_="font9").get_text().strip()
		network_num = network[8:]
		print(network)
		print(network_num)

		name = job_element.find(class_="font14").get_text().strip()
		print(name)

		# address = job_element.find(class_="col-br#text") #not working yet
		# print(address)
		print("address should be here ......")

		# post_outer_div = job_element.find("span" string="threadContentText")
		# print(post_outer_div)
		
		# post = job_element.find(class_="font14").get_text() #not working yet
		# print(post)
		print("post should be here ......")
		
		posted_date_time = job_element.find(class_="comment-time").get_text().strip()
		date_time = posted_date_time[8:]
		date = date_time[:-8]
		# date = date_time[:12]
		time = date_time[13:]
		print(date_time)
		print(date)
		print(time)
		
		writer.writerow({
							'network': network,
							'network_num': network_num,
							'name': name,
							# 'address': address,
							# 'post': post,
							'date_time': date_time,
							'date': date,
							'time': time
						})