# function that does the webscraping, checks if its been done
from bs4 import BeautifulSoup
import requests
from imageio import imread
from scipy.cluster.vq import whiten
from scipy.cluster.vq import kmeans
from PIL import Image
import urllib.request


def check_details(recipe):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
    r = requests.get(recipe.recipe, headers=headers, allow_redirects=True)
    print(r)
    soup = BeautifulSoup(r.content, 'html.parser')

    #loading the instructions
    if(not recipe.instruct):
        ins = soup.find('div', class_="comp recipe__steps-content mntl-sc-page mntl-block")
        for tag in ins.find_all('figcaption'):
            tag.decompose()
        instr = ins.find_all('p')
        lst_instr = []
        for i in instr:
            lst_instr.append(i.getText())
        recipe.instruct = lst_instr
    
    #loading the ingredients
    if(not recipe.ingres == " "):
        i = soup.find('div', class_="comp mntl-lrs-ingredients mntl-block")
        ingres = i.find('ul', class_="mntl-structured-ingredients__list")

        lst_ingre = []
        for ing in ingres:
            if(not ing.getText().isspace()):
                lst_ingre.append(ing.getText())
        recipe.ingres = lst_ingre
        recipe.save()

    try:
        i = soup.find('div', class_="img-placeholder")
        im = i.find('img', class_="loaded primary-img--noscript primary-image__image mntl-primary-image--blurry")
        recipe.image = im['src']
    except:
        try:
            i = soup.find('div', class_="figure-media")
            im = i.find('img')
            try:
                recipe.image = im['data-src']     
            except:
                recipe.image = im['src']
        except:
            print("no image")

    recipe.save()

def choose_colour(recipe):
    urllib.request.urlretrieve(recipe.image, "img.png")
    img = Image.open("img.png")
  
    img = img.copy()
    img.thumbnail((100, 100))
    print(img)

    paletted = img.convert('P', palette=Image.ADAPTIVE, colors=16)

    palette = paletted.getpalette()
    color_counts = sorted(paletted.getcolors(), reverse=True)
    palette_index = color_counts[0][1]
    dominant_color = palette[palette_index*3:palette_index*3+3]
    print(dominant_color)
    dominant_color = rgb2hex(dominant_color[0], dominant_color[1], dominant_color[2])
    return dominant_color

def rgb2hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)





        