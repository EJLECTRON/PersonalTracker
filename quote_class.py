from numpy.random import randint
class Quote:
    @staticmethod
    def get_quote(user):
        """
        Get quote from database
        :param user: User object
        :return: random quote from database
        """
        db = user.mongo_client.quotes

        key = randint(1, 35)

        quote = db.Quotes.find_one({str(key): {"$exists": True}}, {"_id": 0})

        return quote[str(key)]