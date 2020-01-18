from review_classifier_service import ReviewClassifierService

service = ReviewClassifierService()

positive_sample = "It was great"
negative_sample = "It was horrible"
print(service.classify(positive_sample))
print(service.classify(negative_sample))
