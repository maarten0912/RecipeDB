wget --quiet http://www.bbc.co.uk/food/sitemap.xml --output-document - | egrep -o "https?://www.bbc.co.uk/food/recipes/[^<;]+" | wget -i -
