import bpy
import requests

coins = ['ADA', 'XRP', 'LINK', 'SOL', 'XMR']
width = 1
coin_spacing = 1.5
interval = 0

# Loop through the list of coins and fetch their prices.
for i, coin in enumerate(coins):
    response = requests.get(
        f'https://min-api.cryptocompare.com/data/price?fsym={coin.rstrip()}&tsyms=USD,EUR')
    coin_data = response.json()
    bpy.ops.mesh.primitive_cube_add(size=1)
    coin_bar = bpy.context.object

    usd_price = coin_data['USD']

    # Loop through vertices
    for vert in coin_bar.data.vertices:
        vert.co[1] += 0.5
        vert.co[0] += i * coin_spacing + 0.5
    # Add Animations
    coin_bar.scale = [0, 0, 0]
    coin_bar.keyframe_insert(data_path="scale", frame=10 + interval)
    coin_bar.scale = [1, 1, 5]
    coin_bar.keyframe_insert(data_path="scale", frame=50 + interval)
    coin_bar.scale = [1, 1, .5]
    coin_bar.keyframe_insert(data_path="scale", frame=70 + interval)
    coin_bar.scale = (width, float(usd_price), 1)
    coin_bar.keyframe_insert(data_path="scale", frame=80 + interval)

    # Add text
    bpy.ops.object.text_add()
    bpy.context.object.data.align_x = 'RIGHT'
    bpy.context.object.data.align_y = 'CENTER'
    bpy.ops.transform.rotate(value=1.5708)
    bpy.ops.transform.translate(value=(i*coin_spacing+0.5, -0.5, 0))
    bpy.context.object.data.body = f"{coin} {usd_price}"
    interval += 1
