from requests import get
import html2text as ht

h = ht.HTML2Text()
h.ignore_links = True # Ignore Links in HTML
# Get URL as object
url = get('https://docs.google.com/spreadsheets/d/e/2PACX-1vTib8OyUFKby5-vRkJHG3l5Ai9r0sC_NejOHHcnOQ498Tqx_q4BzqggD3L01IqZV41VYEg5zDAuNU8N/pubhtml?gid=1416997619&single=true&range=A8:J17&widget=false&headers=false&chrome=false')
text = h.handle(url.text) # Handle the ascii text of URL

# Remove characters such as | or -
filtered_txt = ''
for char in text:
	if char == '|':
		filtered_txt += ''
	else:
		filtered_txt += char
filtered_txt += '18\n'



# Slice Adgenda and Lunch From Text
def adgendaAndLunch():
	return 'Birthdays:' + filtered_txt[filtered_txt.index('13\n') + 2:filtered_txt.index('14\n')].title()


# Slice Athletics and Announcements from Text
def announcementsAndAthletics():
	string = filtered_txt[filtered_txt.index('11\n') + 2:filtered_txt.index('12\n')].replace('Welcome to', '')
	patched_string = string.replace('THE GUNSTON SCHOOL', '')
	return 'Athletics:' + patched_string.title()
