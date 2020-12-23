#now we create a worldmap of Continents
            # like SA,NA,CA,ASIA

from pygal.maps.world import World

wm = World()

#wm.force_uri_protocol = 'http'
wm.title = 'North, Central, and South America,Asia,Arab'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
    'gy', 'pe', 'py', 'sr', 'uy', 've'])
wm.add("Asia",["in","jp","cn","id","th","sg"])
wm.add("Arab",["eg","iq","dz","bh","jo","sa","ae"])
wm.render_to_file('americas.svg')
