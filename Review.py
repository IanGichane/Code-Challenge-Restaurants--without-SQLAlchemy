class Review:
    count_reviews = 0
    all_reviews  = []
    def __init__(self,customer,restaurant,rating):

        if not isinstance(rating,(float,int)):
            raise TypeError
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        Review.count_reviews +=1
        Review.all_reviews.append(self)


    @classmethod
    def get_all_reviews(cls):
        return cls.all_reviews 
        
     
review = Review('John','res',5)
print(review.rating)     