import os
import sys
import utils

wd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(wd, "deps/"))

import giphy_client
from giphy_client.rest import ApiException

def handler(event, context):
    api_key = os.environ.get('giphy_api_key')
    gif_width = int(os.environ.get('gif_width', '800'))
    tag = os.environ.get('giphy_tag', 'vaporwave')
    api_intance = giphy_client.DefaultApi()

    try:
        random_gif = api_intance.gifs_random_get(api_key, tag=tag)
        gif_id = random_gif.data.id
        width = int(random_gif.data.image_width)
        scale_ratio = gif_width / width
        
        width = int(width * scale_ratio)
        height = int(int(random_gif.data.image_height) * scale_ratio)
    except ApiException:
        gif_id = os.environ.get('default_gif_id', '3oz8xZ1t7hxPfe19M4')
        width = gif_width
        height = gif_width

    embed_url = f'https://giphy.com/embed/{gif_id}'
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html'
        },
        'body': utils.get_html(embed_url, width, height)
    }