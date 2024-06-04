import random

class Codec:
    def __init__(self):
        # Initialize a dictionary to store mappings of integer keys to long URLs
        self.map = {}
        # Initialize a random number generator with a seed
        self.r = random.Random()
        # Generate an initial random key within the range of possible integers
        self.key = self.r.randint(0, 2**31 - 1)

    def encode(self, longUrl: str) -> str:
        # Get a reference to the current key
        key = self.key
        # Generate a new key until a unique key is found
        while key in self.map:
            key = self.r.randint(0, 2**31 - 1)
        # Store the long URL in the map with the generated key
        self.map[key] = longUrl
        # Return the short URL formed by appending the key to the base URL
        return "http://tinyurl.com/" + str(key)

    def decode(self, shortUrl: str) -> str:
        # Extract the key from the short URL
        key = int(shortUrl.split('/')[-1])
        # Retrieve the corresponding long URL from the map using the key
        return self.map[key]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))