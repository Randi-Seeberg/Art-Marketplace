class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
    
  def __repr__(self):
    return "{artist}. \"{title}\". {year}, {medium}. {owner_name}, {owner_location}.".format(artist = self.artist, title = self.title, year = self.year, medium = self.medium, owner_name = self.owner.name, owner_location = self.owner.location)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, expired_listing):
    self.listings.remove(expired_listing)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)
      
class Client:
  def __init__(self, name, location, is_museum, wallet):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"
    self.wallet = wallet
  def print_wallet(self):
    print(str(self.wallet) + " USD")
  
  def sell_artwork(self, artwork, price, expiration_date):
    if artwork.owner == self:
      new_listing = Listing(artwork, price, self, expiration_date)
      veneer.add_listing(new_listing)
  
  def buy_artwork(self, artwork):
    if artwork.owner != self:
      art_listing = None
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = listing
          break
      if art_listing != None:
        self.wallet -= listing.price
        artwork.owner.wallet += listing.price
        artwork.owner = self
        veneer.remove_listing(art_listing)
  
  wishlist = []
  def add_to_wishlist(artwork):
    for listing in veneer.listings:
      if listing.art == artwork:
        wishlist.append(listing)


from datetime import datetime, date        
class Listing:
  def __init__(self, art, price, seller, expiration_date):
    self.art = art
    self.price = price
    self.seller = seller
    self.expiration_date = datetime.strptime(expiration_date, '%Y-%m-%d')
    if self.expiration_date == datetime.now:
       veneer.remove_listing(self)
    
  
  def __repr__(self):
    return "{name}, {price}.".format(name = self.art.title, price = self.price)      

veneer = Marketplace()

edytta = Client("Edytta Halpirt", None, False, 10000000)

girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandolin (Fanny Tellier)", "oil on canvas", "1910", edytta)

edytta.sell_artwork(girl_with_mandolin, 6000000, '2020-07-01')

print(girl_with_mandolin)

moma = Client("The MOMA", "New York", True, 100000000)

edytta.print_wallet()
moma.print_wallet()

moma.buy_artwork(girl_with_mandolin)

print(girl_with_mandolin)

edytta.print_wallet()
moma.print_wallet()

veneer.show_listings()





  
  
  
  
    