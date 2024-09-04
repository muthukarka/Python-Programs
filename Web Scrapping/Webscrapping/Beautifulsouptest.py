import requests
from bs4 import BeautifulSoup


# Making a GET request
r = requests.get('https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_81364f51-572f-4ccc-a7a9-e03c8341c87e_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y')

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

# s = soup.find('div', class_='col-lg-3')
# content = soup.find( class_ = "wrapper" )
#
# print("div ",content)
# # Parsing the HTML
class_list = set()

# Find the 'a' tag
a_tag = soup.find('div')

# Extract the value of the 'href' attribute
href_value = a_tag['class']

# get all tags
tags = {tag.name for tag in soup.find_all()}

# iterate all tags
for tag in tags:

    # find all element of tag
    for i in soup.find_all(tag):

        # if tag has attribute of class
        if i.has_attr("class"):

            if len(i['class']) != 0:
                class_list.add(" ".join(i['class']))

print(class_list)