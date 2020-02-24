class GoogleFactory:
    @staticmethod
    def get_API(API_type):
        try:
            if API_type == "Drive":
                return 