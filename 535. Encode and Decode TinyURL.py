# 535. Encode and Decode TinyURL
# Time:  O(1)
# Space: O(N)

# build bi-directional mappings from long to short and short to long (two dicts)
class Codec:
    
    def __init__(self):
        self.alphanumeric = string.ascii_letters + '0123456789'
        self.code2url = {}
        self.url2code = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        # keep generating new short urls until no duplication
        while longUrl not in self.url2code:
            code = ''.join(random.choice(self.alphanumeric) for _ in range(6))
            if code not in self.code2url:
                self.code2url[code] = longUrl
                self.url2code[longUrl] = code
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))