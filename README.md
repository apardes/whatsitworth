whatsitworth
============

A simple Flask application that returns the average value of used products.

I created a Kimono Labs API to pull sold item values from eBay. The Flask 
app queries this API with the user's item and calculates a roughed-out "fair
market value" for your product.

**Does not work for products with values < $20. The algorithm
deliberately ignores values < 20.
