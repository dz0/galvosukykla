#~ import cairosvg
""" Board game "spot the same object" card generator

example with ten cards (5 pictures in each),
where every card has just one same object with each other...
http://galvosukykla.lt/rodyk/thumbs.php?p=//stalo_zaidimai/10_cards-single_joins/png&dim=150

This is complete graph.
The most bruteforce would be to assign a different image for each vertex.

But then for N nodes, one needs (N-1)*N / 2 pictures.
and if I'd like to have 40 cards - I'd need ~800 pictures. I want to optimize.

And there the Combinatorics Adventure begins

Let's say for 10 cards bruteforce would need 9*10/2 = 45 pictures. 
But in my example there are only 20 images used :)
The idea is first to generate combinations 2 of 5 pictures.
it gives 10 different combinations, which have at most 1 same picture.
But this provides 30 vertexes! :)
and then each node still needs 3 extra vertexes, where I use 10*3/2=15 other images.

But If I want to increase to 15 cards, I quite fast run into problem, that I still run out of images :/



Problem: how to generate combinations keeping the number of images per card not too big (and I'd like up to 9 imges per card).
and so that Each card would be connected to another (and in ideal case - just one same image per 2 cards)

"""

import re
import os
import random
import json


cwd = os.getcwd()
#######################################################################
#         IMAGES 
#######################################################################

images=[]

for fname in os.listdir('svg'):
    #~ print (fname)
    name=fname[:-4]
    
    img_svg_code = open('svg/'+fname).read()
    img_width  = float( re.search('<svg[^>]+?width="([\d.]+)[^"]*"', img_svg_code).group(1) )
    img_height = float( re.search('<svg[^>]+?height="([\d.]+)[^"]*"', img_svg_code).group(1) )

    img_info =  dict(name=name, img_width=img_width, img_height=img_height, img_id=len(images) )
    images.append( img_info )   # img_id should be same as index in names list
    

    #~ with open('png/'+outfname, 'wb') as fout:        
        #~ cairosvg.svg2png(bytestring=img_svg_code,write_to=fout)
    if not os.path.exists( 'png/'+name+'.png' ):
        cmd = "inkscape -z -f %s -w %s -j -e %s" % ('svg/'+fname, 200, 'png/'+name+'.png')
        os.system(cmd)

    
with open("images.json", 'w') as f:
    f.write( json.dumps( images, sort_keys=True, indent=4) )
    
#######################################################################
#         COMBINATORICS
#######################################################################
def pair_combinations( k ) :
    return k*(k-1)/2

def nonDuplicating_joins( k_imgs ):
    return pair_combinations(k_imgs-1) * k_imgs

def generate_pair_combinations( n , values=None):
    if values == None:
        values=range(n)

    if len(values) < n:
        raise Exception("generate_pair_combinations values list too short: %s, %s" % (n, values) )
        
    pairs = []
    a = 0
    b = a+1
    for a in range(n-1):
        for b in range(a+1, n):
            x, y = values[a], values[b] 
            pairs.append( [ x, y ] )
    return pairs

def update_combinations_with_single_joins( combinations, next_unused_id ):
    if cardsN > len(combinations):
        raise(Exception("not enough combinations for Cards"))

    used_imgs_count = 0
    for i in range(cardsN-1):
        for j in range(i+1, cardsN):
            if not ( set(combinations[i]) & set(combinations[j]) ): # set intersection http://docs.python.org/2/library/sets.html#set-objects
                combinations[i].append( next_unused_id )
                combinations[j].append( next_unused_id )
                next_unused_id += 1
                used_imgs_count  += 1
    return used_imgs_count 

cardsN = 10
joinsN = cardsN*(cardsN-1)/2
imgsN = len(images)

imgs4pairsN = 2
while pair_combinations( imgs4pairsN ) < cardsN:
    imgs4pairsN += 1

joinsN_by_pairs = nonDuplicating_joins( imgs4pairsN )
print ("imgs4pairsN=%s gives pair_combinations: %s (of %s cards needed)" % (imgs4pairsN, pair_combinations( imgs4pairsN ) , cardsN ) )
print ("imgs4pairsN=%s gives joins: %s (of %s joins needed)" % (imgs4pairsN, joinsN_by_pairs, joinsN ) )
print("imgsN=%s: taken for pairs=%s, avalable for single=%s (of %s single joins needed)" % (imgsN, imgs4pairsN, imgsN-imgs4pairsN,  joinsN-joinsN_by_pairs ) )

print ("generate_pair_combinations (%s): " % imgs4pairsN, generate_pair_combinations( imgs4pairsN ) )


#######################################################################
#         CARDS
#######################################################################

# add paired images for joins 
pair_combinations = generate_pair_combinations( imgs4pairsN )
cards = pair_combinations[:cardsN]

#~ ### hacks to minimize required pictures (but gives double-joins)
more_pair_combinations = generate_pair_combinations( imgs4pairsN, range(imgs4pairsN, 2*imgs4pairsN) )
parallel_cards = more_pair_combinations[:cardsN]

#~ ###### hack1: random select
#~ random.shuffle( parallel_cards )
#~ cloned_cards = cards[:] 
#~ 
#~ for card, parallel_card in zip( cards, parallel_cards):
    #~ card.extend( parallel_card[:2] )
    #~ for card_as_donor in  cloned_cards:  # to take combinations which don't have joins already
        #~ if not ( set(parallel_card) & set(card_as_donor) ):
            #~ parallel_card.extend( card_as_donor[2:] )
            #~ cloned_cards.remove( card_as_donor )
            #~ break
#~ print "CLONED CARDS LEFT", cloned_cards
#~ random.shuffle( parallel_cards )
#~ for card, parallel_card in zip( cards, parallel_cards):
    #~ parallel_card.extend( card[:2] )

#~ ####### hack2:  nonoverlaping combinations preselected: just in case cardsN = 10
#~ nonoverlaping_combinations_out_of5 = [(0, 9), (1, 6), (2, 4),  (3, 7),  (5, 8)]
#~ for i, j in nonoverlaping_combinations_out_of5:
    #~ cards[i].extend( parallel_cards[i][:2] )
    #~ parallel_cards[i].extend( cards[j][:2] )
#~ 
    #~ cards[j].extend( parallel_cards[j][:2] )
    #~ parallel_cards[j].extend( cards[i][:2] )
#~ 
    #~ 
#~ cards.extend( parallel_cards  )
#~ cardsN *= 2
#~ 
#~ imgs4singlejoins_count = 0
#~ imgs4singlejoins_count = update_combinations_with_single_joins( cards, imgs4pairsN * 2 )
####### end hacks

# update with images for single joins
imgs4singlejoins_count = update_combinations_with_single_joins( cards, imgs4pairsN )


with open("cards.json", 'w') as f:
    f.write("images used: %s + %s \n" % (imgs4pairsN, imgs4singlejoins_count )  )
    f.write ( "\n".join( map(str, cards )) ) 
    #~ f.write( json.dumps(cards,  indent=4) )




svg_code = """<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" 
  "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg width="800" height="800" version="1.1"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
>
  <desc>Card
  </desc>

  <!-- Show outline of canvas using 'rect' element -->
  <rect x="0" y="0" width="800" height="800"
        fill="white" stroke="black" stroke-width="4pt" />

   <!--INCLUDE_IMAGES-->
   

</svg>
"""

img_svg_template = """
    <image
       y="%(img_y)s"
       x="%(img_x)s"
       id="image%(img_id)s"
       xlink:href="file://%(cwd)s/png/%(img_name)s.png"
       height="%(img_height)s"
       width="%(img_width)s"
       transform="%(img_transform)s" />
"""




doc_width, doc_height = 800, 800

config = {}
config['img_width'] = 200
config['img_margin'] = 50



# populate cards with images
for card_nr, img_set in enumerate( cards ):

    
    images_svg_codes = []
    img_in_card_nr = 0
    x, y = config['img_margin'], config['img_margin']
    #~ max_line_height = 0
    
    print
    print ( card_nr, img_set )
    print
    
    if len(img_set) < 9:
        img_set.extend( [None] * (9-len(img_set)) )  # ad blanks to distribute more in space
    random.shuffle( img_set  )
    
    for img_id in img_set:

        img_in_card_nr += 1
        if img_in_card_nr > 9:
            print ("Too much images in one card - should be no more than 9", img_set)
            break

        if img_id != None: 
            img_info = images[img_id]

            name = img_name = img_info['name']
            img_height = img_info['img_height']
            img_width = img_info['img_width']
            #~ print (img_id, name)
            if img_info['img_id'] != img_id:
                raise( Exception("Some missunderstanding with image id: expected %s, got %s, name %s" % (img_info['img_id'], img_id, name) ) ) 
            
            img_x = x
            img_y = y

                    
            proportion_hw = 1.0*img_height/img_width
            
            #~ img_width, img_height = config['img_width'], proportion_hw*config['img_width']
            img_width, img_height = 200, proportion_hw*200
            if img_height > 200:
                img_width, img_height = 200.0/proportion_hw, 200
                img_x += (200-img_width)/2
            else:
                img_y += (200-img_height)/2

            #~ print( "proportion_hw, img_height, img_width:", proportion_hw, img_height, img_width )

            # http://apike.ca/prog_svg_transform.html rotate a bit ;)
            img_transform = "rotate( %s , %s, %s)" % (random.randint(0, 360), img_x + img_width/2, img_y + img_height/2 )
            #~ img_transform = ""

            #~ print (img_info)
            #~ print( img_svg_template % locals() )
            
            images_svg_codes.append( img_svg_template % locals() )  # % img_info
            #~ print (images_svg_codes[-1])

        x += 200 + config['img_margin']
        #~ if img_height > max_line_height:
            #~ max_line_height = img_height
        #~ if x > doc_width:
        if img_in_card_nr %3 == 0:
            #~ y += max_line_height + config['img_margin']
            y += 200 + config['img_margin']
            x = config['img_margin']

    # Write Card
    #~ continue
    card_svg_code = svg_code.replace('<!--INCLUDE_IMAGES-->', "\n".join(images_svg_codes))
    with open("cards/card_%s.svg"%card_nr, "w") as f:
        f.write( card_svg_code )
    # http://stackoverflow.com/questions/6589358/convert-svg-to-png-in-python
    # http://stackoverflow.com/a/10130023
    cmdline = "inkscape -z -f cards/card_%s.svg -w 800 -j -e cards/png/card_%s.png" % (card_nr, card_nr)
    os.system(cmdline)




