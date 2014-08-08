"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from content_display.views import search_test



# Testing cities
class search(TestCase) :
    query = ""
    dic = search_test(query)
    def test_and_none(self):
        query = ""
        dic = search_test(query)
        
        self.assertEqual(dic[cbool], 0)
        self.assertEqual(dic[abool], 0)
        self.assertEqual(dic[lbool], 0)
        
    def test_or_none(self):
        query = ""
        dic = search_test(query)

        self.assertEqual(dic[cobool], 0)
        self.assertEqual(dic[aobool], 0)
        self.assertEqual(dic[lobool], 0)

    def test_and_single(self):
        query = "shark"
        dic = search_test(query)
        
        self.assertEqual(dic[cities], "")
        self.assertEqual(dic[activities], [{"Shark Diving": "Cape Town is known for Great White Shark Diving. The region attracts people from across the world for this very adventurous attraction."}])
        self.assertEqual(dic[languages], "")
        
    def test_or_single(self):
        query = "shark"
        dic = search_test(query)

        self.assertEqual(dic[co], "")
        self.assertEqual(dic[ao], [{"Shark Diving": "Cape Town is known for Great White Shark Diving. The region attracts people from across the world for this very adventurous attraction."}])
        self.assertEqual(dic[lo], "")


    def test_and_multi(self):
        query = "shark africa"
        dic = search_test(query)

        self.assertEqual(dic[cities], "")
        self.assertEqual(dic[activities], "")
        self.assertEqual(dic[languages], "")

    def test_or_multi(self):
        query = "shark africa"
        dic = search_test(query)
        
        self.assertEqual(dic[co], [{"Cape Town": "Cape Town is the second-most populous city in South Africa, after Johannesburg, and the provincial capital and primate city of the Western Cape. The City is famous for its harbour, for its natural setting in the Cape floral kingdom, as well as the such well known landmarks as Table Mountain and Cape Point. Cape Town is located on the shore of Table Bay"}])
        self.assertEqual(dic[ao], [{"Shark Diving": "Cape Town is known for Great White Shark Diving. The region attracts people from across the world for this very adventurous attraction.", "Table Mountain":"Table Mountain Table Mountain is a flat-topped mountain forming a prominent landmark overlooking the city of Cape Town in South Africa, and is featured in the Flag of Cape Town and other local government insignia. It is a significant tourist attraction, with many visitors using the cableway or hiking to the top. The mountain forms part of the Table Mountain National Park"}])
        self.assertEqual(dic[lo], [{"Arabic": "Arabic is a name for what are traditionally considered the descendants of the Classical Arabic language of the 6th century. This includes both the literary language and varieties of Arabic spoken in a wide arc of territory, stretching across the Middle East, North Africa, the Horn of Africa. Arabic belongs to the Afro-Asiatic family"}])
        
    def test_and_multi2(self):
        query = "travel somewhere"
        dic = search_test(query)

        self.assertEqual(dic[cities], "")
        self.assertEqual(dic[activities], "")
        self.assertEqual(dic[languages], "")

    def test_or_multi2(self):

        query = "travel somewhere"
        dic = search_test(query)

        self.assertEqual(dic[co], [{"Rio de Janeiro": "Rio was founded in 1565 by Portuguese. It recieves the most visitors per year of any city in South America 2.82 million international tourists a year. Rio is the most awarded destination by World Travel Awards in the South American category as the best destination", "Cancun" : "Cancun has the distinction of being the one Caribbean destination with the infrastructure, modern amenities and service philosophy to rival leisure destinations worldwide. Unlike many other parts of the Caribbean and Mexico, Cancun was built for tourism, and continues to meet the needs of its over 3.3 million annual visitors. Cancun delivers to travelers the best of many worlds: the Caribbean and Mexico; modern and ancient; action packed and laid back. Cancun is unequaled in its ability to offer cultural treasures, natural beauty, infinite activities and North American-style conveniences" }])
        self.assertEqual(dic[ao], "")
        self.assertEqual(dic[lo], "")

    def test_and_multi3(self):
        query = "beach hotel california"
        dic = search_test(query)

        self.assertEqual(dic[cities], "")
        self.assertEqual(dic[activities], "")
        self.assertEqual(dic[languages], "")

    def test_or_multi3(self):
        query = "beach hotel california"
        dic = search_test(query)

        self.assertEqual(dic[co], "")
        self.assertEqual(dic[ao], [{"Shelly Beach":"Shelly Beach (also known as Shelley Beach) is a beach located in Manly, a suburb of Sydney, New South Wales, Australia. It is adjacent to North Head and Fairy Bower. Shelly Beach is the only west facing beach on the eastern coast of Australia.","Table Bay Hotel":"Sitting on the buzzing Victoria & Alfred Waterfront, the Table Bay Hotel has one of the best locations in Cape Town, with views of Table Mountain, the harbor and notorious Robben Island. It was, in fact, the prisons most famous former inmate who opened the hotel in 1997: then-President Nelson Mandela. The neo-Victorian architecture exudes old-world elegance, as does the attentive service, which extends to helicopter transfers, personal shopping and the therapies at the Camelot Spa. Dining and cocktail options include The Atlantic, Camissa Brasserie, two bars and a lounge for afternoon tea. Dont miss the bronze statue honoring Oscar, a seal that often visited the waters by the hotel as it was being built and so charmed the staff that he became their mascot.","Kukulcan Plaza":"Kukulcan Plaza is the most exclusive and luxurious shopping center in all of Cancun and the Riviera Maya. It is located in the Hotel Zone, where the main Five Star and Grand Tourism hotels are situated. Kukulcan Plazas offerings range from boutiques of worldwide renown, jewelry shops with fine gems of prestigious designers, elegant perfumeries, and fine restaurants, to shops that offer handicrafts and even bowling! Shopping in Cancun is an excellent option.","Westin Regina Resort":"Lounge endlessly at our glorious private beaches and four outdoor pools. Pamper yourself at the luxurious Heavenly Spa by Westin. Or pick up the pace with countless water sports, plus tennis, golf, a top-notch gym, and fascinating local tours and day trips. Features & Activities Overview: Hotel Amenities, Beaches and Water Sports, Nearby Golf, WestinWORKOUT Fitness Studio, Westin Kids Club, Outdoor Lighted Tennis Courts, Heavenly Spa by Westin, Outdoor Pools, Internet Access, Environmental Practices, Pet Service, Tour Service, SPG Kids Pass, SuperFoodsRx, The Westin Eat Well Menu for Kids","Four Seasons Cairo":"Located on the west bank of the Nile, 5 km (3 miles) from downtown Cairo Birds eye views of the great Pyramids, the Zoological Gardens and the Nile. Part of the luxurious First Place Complex, a multi-use development with upscale shopping boutiques, restaurants and one of Cairos chic night-life venues and private residences 20 floors, rooms start on 5th. 269 rooms and 43 suites Extensive health club facilities including 24 hr state-of-the-art gym with views overlooking the Nile, Luxurious Spa and Wellness Center including couples suite. Elegant dining options with international flavours, including Thai, Syrian and contemporary Italian cuisine, two Lounge/Bar Outdoor pool, including dedicated childrens pool and stylish Bar area, an oasis in the heart of the city. Dedicated Kids Suite, first of its kind in Cairo. Offering a range of exciting, fun and educational activities from arts & crafts, Wii and Playstation game consoles, to a selection of childrens books. Hotel is integrated with three levels of the First Place Complex."}])
        self.assertEqual(dic[lo], "")

    