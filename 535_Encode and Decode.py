import string
import random

long_to_short = {}
short_to_long = {}
letters = string.ascii_letters + string.digits


class Solution:

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """

        def shortpart():  # use random.randint(0,61) to generate the random number between 0 to 61(both include)
            ans = ''  # generate 6 digit for suffix
            temp = ''  # total number in (0,61) is 62
            for i in range(6):
                temp = letters[random.randint(0, 61)]
                ans += temp
            return ans

        if longUrl in long_to_short:  # if we already input the same longUrl before, we just return the shortUrl
            return "http://tinyurl.com/" + long_to_short[longUrl]
        else:
            suffix = shortpart()  # otherwise, we generate a suffix for longUrl and store it into our 2 dict.
            long_to_short[longUrl] = suffix
            short_to_long[suffix] = longUrl
            return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        a = shortUrl.split("/")[-1]  # if suffix in the dict, we can get the longUrl
        if a in short_to_long:  # otherwise, nothing to decode.
            return short_to_long[a]
        else:
            return None

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))