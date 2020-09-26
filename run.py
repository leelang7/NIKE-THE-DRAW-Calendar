import api
from pprint import pprint

soup = api.get_request('/launch')

launch_items = soup.find_all('a', class_='comingsoon')
drawable_items = []

for launch_item in launch_items:
  soldout_button = launch_item.find('span', class_='btn-soldout')
  if (soldout_button and soldout_button.text == 'THE DRAW 진행예정'):
    launch_item_image = launch_item.find('img', class_='img-component')

    drawable_items.append({
      'title': launch_item.attrs['title'],
      'theme': launch_item_image.attrs['alt'],
      'image': launch_item_image.attrs['data-src'],
      'href': launch_item.attrs['href'],
    })

pprint(drawable_items)
