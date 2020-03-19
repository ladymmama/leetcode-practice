class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # TC:O(n), SC: O(1)
        ip = address.split(".")
        return "[.]".join(ip)
    