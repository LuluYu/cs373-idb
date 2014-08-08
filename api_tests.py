"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
import requests



# Testing cities
class CitiesApiTest(TestCase) :
    url = "http://flappybirds.pythonanywhere.com/api/"
    def test_cities(self):
        response = requests.get(self.url + "cities/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 1, "name": "Sydney", "description": "Sydney is the state capital of New South Wales and the most populous city in Australia. It is on Australias south-east coast, on the Tasman Sea. In June 2010 the greater metropolitan area had an approximate population of 4.76 million people. Inhabitants of Sydney are called Sydneysiders, comprising a cosmopolitan and international population."},{"id": 2, "name": "New Delhi", "description": "New Delhi is the capital of India and seat of the executive, legislative, and judiciary branches of the Government of India. It is also the centre of the Government of the National Capital Territory of Delhi. New Delhi is situated within the metropolis of Delhi and is one of the eleven districts of Delhi National Capital Territory. With a population of 22 million in 2011, Delhi metropolitan region is the worlds second most populous city and the largest city in India and also one of the largest in the world in terms of area. After Mumbai it is also the wealthiest city in India, and has the 2nd highest GDP of any city in South, West or Central Asia."},{"id": 3, "name": "Saint Petersburg", "description": "Saint Petersburg was established in May 27, 1703 with the idea for it to be a city that rivaled Europes greatest capitals. Since then it has grown into Russias second largest city. It is know for being the cultural capital of Russia with one of the largest art museums in the world , The Hermitage."},{"id": 4, "name": "Bangkok", "description": "Bangkok is both the capital of Thailand and most populated. The city was founded by King Rama in 1782 and is now the home for 12.6% of Thailands population. Thailand is one of Asias most cosmopolitan cities with magnificent temples and palaces, authentic canals, busy markets and a vibrant nightlife that has something for everyone."},{"id": 5, "name": "Cape Town", "description": "Cape Town is the second-most populous city in South Africa, after Johannesburg, and the provincial capital and primate city of the Western Cape. The City is famous for its harbour, for its natural setting in the Cape floral kingdom, as well as the such well known landmarks as Table Mountain and Cape Point. Cape Town is located on the shore of Table Bay."},{"id": 6, "name": "Rio de Janeiro", "description": "Rio was founded in 1565 by Portuguese. It recieves the most visitors per year of any city in South America 2.82 million international tourists a year. Rio is the most awarded destination by World Travel Awards in the South American category as the best destination."},{"id": 7, "name": "Nanjing", "description": "Located in the lower Yangtze River drainage basin and Yangtze River Delta economic zone, Nanjing has long been one of Chinas most important cities. Having been the capital city of six different dynasties since 3 A.D., it is recognized as one of the Four Great Ancient Capitals of China."},{"id": 8, "name": "Lijiang", "description": "Lijiang is a prefecture-level city in the northwest of Yunnan, China. It has an area of 8,193 sq. mi and had a population of 1,244,769 at the 2010 census. Lijiang City replaced the former administrative region of Lijiang Prefecture which was under the rule of the Mu family local commanders during the Ming Dynasty and Qing Dynasty. In ancient times, it used to be the center of silk embroidery in the southwest of China and the most important place of the Ancient Southern Silk Road, also called the Ancient Tea and Horse Road or Ancient tea route."},{"id": 9, "name": "Vatican City", "description": "Vatican City is one of the most popular tourist destination in Italy. The vatican state is the center of the Roman Catholic faith, it houses one of the most beautiful masterpieces of art in places such as the Sistine Chapel. Not only does the Vatican contain wonderful museums, they also have exotic gardens and more for those who wish to see more than the buildings of the Vatican state. "},{"id": 10, "name": "Grand Canyon National Park", "description": "Grand Canyon is in the northwest corner of Arizona, close to the borders of Utah and Nevada. The Colorado River, which flows through the canyon, drains water from seven states, but the feature we know as Grand Canyon is entirely in Arizona. Most of the Grand Canyon lies within Grand Canyon National Park and is managed by the National Park Service. "},{"id": 11, "name": "Cancun", "description": "Cancun has the distinction of being the one Caribbean destination with the infrastructure, modern amenities and service philosophy to rival leisure destinations worldwide. Unlike many other parts of the Caribbean and Mexico, Cancun was built for tourism, and continues to meet the needs of its over 3.3 million annual visitors. Cancun delivers to travelers the best of many worlds: the Caribbean and Mexico; modern and ancient; action packed and laid back. Cancun is unequaled in its ability to offer cultural treasures, natural beauty, infinite activities and North American-style conveniences."},{"id": 12, "name": "Giza", "description": "Giza is the third largest city in Egypt. It is located on the west bank of the Nile, some 20 km (12.43 mi) southwest of central Cairo. Along with Cairo Governorate, Shubra El-Kheima, Helwan, 6th October City and Obour, the five form Greater Cairo metropolis. The city of Giza is the capital of the Giza Governorate, and is located near the northeast border of this governorate in coordinates. It is located right on the banks of the River Nile. Giza is most famous as the location of the Giza Plateau: the site of some of the most impressive ancient monuments in the world."}]
        self.assertTrue(content==resp)

    def test_cities_404(self):
        response = requests.get(self.url + "cities/bogus/")
        self.assertEqual(response.status_code, 404)


    def test_cities_id_1(self):
        response = requests.get(self.url + "cities/1/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 1, "name": "Sydney", "description": "Sydney is the state capital of New South Wales and the most populous city in Australia. It is on Australias south-east coast, on the Tasman Sea. In June 2010 the greater metropolitan area had an approximate population of 4.76 million people. Inhabitants of Sydney are called Sydneysiders, comprising a cosmopolitan and international population."}]
        self.assertTrue(content==resp)

    def test_cities_id_2(self):
        response = requests.get(self.url + "cities/2/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 2, "name": "New Delhi", "description": "New Delhi is the capital of India and seat of the executive, legislative, and judiciary branches of the Government of India. It is also the centre of the Government of the National Capital Territory of Delhi. New Delhi is situated within the metropolis of Delhi and is one of the eleven districts of Delhi National Capital Territory. With a population of 22 million in 2011, Delhi metropolitan region is the worlds second most populous city and the largest city in India and also one of the largest in the world in terms of area. After Mumbai it is also the wealthiest city in India, and has the 2nd highest GDP of any city in South, West or Central Asia."}]
        self.assertTrue(content==resp)

    def test_cities_id_3(self):
        response = requests.get(self.url + "cities/3/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 3, "name": "Saint Petersburg", "description": "Saint Petersburg was established in May 27, 1703 with the idea for it to be a city that rivaled Europes greatest capitals. Since then it has grown into Russias second largest city. It is know for being the cultural capital of Russia with one of the largest art museums in the world , The Hermitage."}]
        self.assertTrue(content==resp)

    def test_cities_id_4(self):
        response = requests.get(self.url + "cities/4/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 4, "name": "Bangkok", "description": "Bangkok is both the capital of Thailand and most populated. The city was founded by King Rama in 1782 and is now the home for 12.6% of Thailands population. Thailand is one of Asias most cosmopolitan cities with magnificent temples and palaces, authentic canals, busy markets and a vibrant nightlife that has something for everyone."}]
        self.assertTrue(content==resp)

    def test_cities_id_5(self):
        response = requests.get(self.url + "cities/5/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 5, "name": "Cape Town", "description": "Cape Town is the second-most populous city in South Africa, after Johannesburg, and the provincial capital and primate city of the Western Cape. The City is famous for its harbour, for its natural setting in the Cape floral kingdom, as well as the such well known landmarks as Table Mountain and Cape Point. Cape Town is located on the shore of Table Bay."}]
        self.assertTrue(content==resp)

    def test_cities_id_7(self):
        response = requests.get(self.url + "cities/7/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 7, "name": "Nanjing", "description": "Located in the lower Yangtze River drainage basin and Yangtze River Delta economic zone, Nanjing has long been one of Chinas most important cities. Having been the capital city of six different dynasties since 3 A.D., it is recognized as one of the Four Great Ancient Capitals of China."}]
        self.assertTrue(content==resp)

    def test_cities_id_8(self):
        response = requests.get(self.url + "cities/8/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 8, "name": "Lijiang", "description": "Lijiang is a prefecture-level city in the northwest of Yunnan, China. It has an area of 8,193 sq. mi and had a population of 1,244,769 at the 2010 census. Lijiang City replaced the former administrative region of Lijiang Prefecture which was under the rule of the Mu family local commanders during the Ming Dynasty and Qing Dynasty. In ancient times, it used to be the center of silk embroidery in the southwest of China and the most important place of the Ancient Southern Silk Road, also called the Ancient Tea and Horse Road or Ancient tea route."}]
        self.assertTrue(content==resp)

    def test_cities_id_9(self):
        response = requests.get(self.url + "cities/9/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 9, "name": "Vatican City", "description": "Vatican City is one of the most popular tourist destination in Italy. The vatican state is the center of the Roman Catholic faith, it houses one of the most beautiful masterpieces of art in places such as the Sistine Chapel. Not only does the Vatican contain wonderful museums, they also have exotic gardens and more for those who wish to see more than the buildings of the Vatican state. "}]
        self.assertTrue(content==resp)

    def test_cities_id_10(self):
        response = requests.get(self.url + "cities/10/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 10, "name": "Grand Canyon National Park", "description": "Grand Canyon is in the northwest corner of Arizona, close to the borders of Utah and Nevada. The Colorado River, which flows through the canyon, drains water from seven states, but the feature we know as Grand Canyon is entirely in Arizona. Most of the Grand Canyon lies within Grand Canyon National Park and is managed by the National Park Service. "}]
        self.assertTrue(content==resp)

#Testing Activities
class ActivitiesApiTest(TestCase) :
    url = "http://flappybirds.pythonanywhere.com/api/"
    def test_activities(self):
        response = requests.get(self.url + "activities/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        reps = [{"id": 2, "name": "Sydney Opera House", "description": "The Sydney Opera House is a multi-venue performing arts centre in Sydney, New South Wales, Australia. Situated on Bennelong Point in Sydney Harbour, close to the Sydney Harbour Bridge, the facility is adjacent to the Sydney central business district and the Royal Botanic Gardens, between Sydney and Farm Coves.", "city": 1},{"id": 3, "name": "Shelly Beach", "description": "Shelly Beach (also known as Shelley Beach) is a beach located in Manly, a suburb of Sydney, New South Wales, Australia. It is adjacent to North Head and Fairy Bower. Shelly Beach is the only west facing beach on the eastern coast of Australia.", "city": 1},{"id": 4, "name": "Taj Mahal", "description": "The Taj Mahal from Persian and Arabic, crown of palaces is a white marble mausoleum located in Agra, Uttar Pradesh, India. It was built by Mughal emperor Shah Jahan in memory of his third wife, Mumtaz Mahal. The Taj Mahal is widely recognized as the jewel of Muslim art in India and one of the universally admired masterpieces of the worlds heritage.", "city": 2},{"id": 5, "name": "Buzzaria", "description": "Buzzaria is a retail destination store full of very interesting,quirky ethnic Indian products.Coined from an hindi word Bajaria meaning village market place and the word Buzz.Carrying over 50000 products.From Saris to handmade soaps to fashion to handcrafted products to jewelry to some amazing cushion covers.Open most days of the year,a shoppers paradise and a creative and buzzing hot spot.A place overflowing with passion and color and happiness.", "city": 2},{"id": 6, "name": "Thyagaraj Sports Complex", "description": "The Thyagaraj Sport Complex is a sports stadium in New Delhi, India. It is owned by the Government of National Capital Territory of Delhi, and was built from scratch at a cost of Rs. 300 crore (US$65m).It was designed by leading architects PTM of Australia and Kapoor&Associates of Delhi. The venue was built as a venue for the 2010 Commonwealth Games, and was named after the South Indian music composer Thyagaraj.", "city": 2},{"id": 7, "name": "The Hermitage", "description": "The Hermitage is a museum of art and culture in Saint Petersburg, Russia. It is one of the largest and oldest museums in the world, as it was found in 1764 by Catherine the Great and opened to the public in 1852. It host over three million items which only a small portion is on permanent display.", "city": 3},{"id": 8, "name": "Church of the Savior on Blood", "description": "Known by many different names such as Church of Spilled Blood, Church on Split Blood, and Cathedral of the Resurrection of Christ was built in honor of the assasinated Tsar Alexander II. Construction of the church began in 1883 and was completed in 1907. It is considered a State Historical Museum by Russia and is one of the main attractions of Saint Petersburg. One of the churchs main features are its colorful onion domes.", "city": 3},{"id": 9, "name": "Catherine Palace", "description": "The Catherine Palace is only 25km from the city of Saint Petersburg is one of the top tourist destinations for tourist of Saint Petersburg. the Boaroque 18th-century place was where the Russian royal family spent their summers. It was first constructed 1717, but since has been remodeled through the year by multiple Tsars. It is most known for its beautiful light blue walls of the palace.", "city": 3},{"id": 10, "name": "Wat Arun", "description": "The Wat Arun, or Temple of Dawn is a Buddhist temple in the Bangkok Yai district of Bangkok. It is among the most know landmarks in Thailand and the first light of the monrning reflects of the surcface of the temple with pearly iridescence. It was founded before 1656 BE so it makes it one of Bangkok oldest temples.", "city": 4},{"id": 11, "name": "Ayutthaya", "description": "Located outside of Bangkok, this ancient city was founded over 600 years ago. Amidst the remaining temple structures, you can relive its history.", "city": 4},{"id": 12, "name": "Grand Palace", "description": "At the hearth of Bangkok, the Grand Palace was the official residence of the Kings of Siam since 1782. It is made up by a large number of individual buildings that make it one of Bangkoks premier attractions. Even though royalty has moved from the palace, it still used for official events.", "city": 4},{"id": 13, "name": "Shark Diving", "description": "Cape Town is known for Great White Shark Diving. The region attracts people from across the world for this very adventurous attraction.", "city": 5},{"id": 14, "name": "Table Mountain", "description": "Table Mountain is a flat-topped mountain forming a prominent landmark overlooking the city of Cape Town in South Africa, and is featured in the Flag of Cape Town and other local government insignia. It is a significant tourist attraction, with many visitors using the cableway or hiking to the top. The mountain forms part of the Table Mountain National Park.", "city": 5},{"id": 15, "name": "Table Bay Hotel", "description": "Sitting on the buzzing Victoria & Alfred Waterfront, the Table Bay Hotel has one of the best locations in Cape Town, with views of Table Mountain, the harbor and notorious Robben Island. It was, in fact, the prisons most famous former inmate who opened the hotel in 1997: then-President Nelson Mandela. The neo-Victorian architecture exudes old-world elegance, as does the attentive service, which extends to helicopter transfers, personal shopping and the therapies at the Camelot Spa. Dining and cocktail options include The Atlantic, Camissa Brasserie, two bars and a lounge for afternoon tea. Dont miss the bronze statue honoring Oscar, a seal that often visited the waters by the hotel as it was being built and so charmed the staff that he became their mascot.", "city": 5},{"id": 16, "name": "Football (Soccer)", "description": "Football (Soccer) is the most popular sport in Rio de Janeiro. Rio is home to five soccer teams: Vasco da Gama, Botafogo, Fluminense, Flamengo, and America Football Club. ", "city": 6},{"id": 17, "name": "Cristo Redentor Statue", "description": "Cristo Redentor (Christ the Redeemer) is an Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil. It was considered the largest Christ statue in the world from 1931 until 2010 when it was topped by the Christ the King statue in Poland. It is 30 metres (98 ft) tall, not including its 8 metres (26 ft) pedestal, and its arms stretch 28 metres (92 ft) wide.", "city": 6},{"id": 18, "name": "Gate of China", "description": "The city wall of Nanjing was built from 1360 to 1386 under the founder of the Ming dynasty, the Hongwu Emperor Zhu Yuanzhang. In 1368, Zhu Yuanzhang was crowned Emporor, and made Nanjing his capital. The southern and eastern sections of the old city wall from the Tang dynasty were incorporated into the enw wall. The northern and eastern sections were built afresh. The city wall was 33.676 kilometres long. It was 14-21 m high; 14.5m thick at its base, and 4.9m think at the top. Thirteen gates were built into the wall, and the enclosed area was the largest of any walled city in China. The gate today known as the Gate of China was built on the site of the south gate of the capital city of the Southern Tang dynasty. It was the largest among the thirteen gates of Nanjing. In 1931, after the Republic of China government established Nanjing as its capital, the gate was renamed the Gate of China.", "city": 7},{"id": 19, "name": "Qinhuai Lantern Fair", "description": "Qinhuai Lantern Fair is a popular folk custom celebration of the Lantern Festival in the Nanjing area. Modern usage refers to the large-scale fair held yearly at the Confucius Temple of Nanjing between Spring Festival and Lantern Festival. The origin of the fairs can be traced back to Eastern Wu. During that time, the act of hanging lanterns was used in festivals and celebrations. When armies returned in triumph, government officials and civilians would gather to hang up lanterns around the city to welcome them home. Nanjing was the capital during Eastern Jin and Southern Dynasties. Many nobles and members of the gentry lived on the banks of Qinhuai River. When Lantern Festival came, these people would hang up lanterns and decorations, mimicking the Palace.", "city": 7},{"id": 20, "name": "Old Town of Lijiang", "description": "The Old Town of Li Jiang and its residential architecture have a history of more than 800 years and was once a confluence for trade along the old tea horse road. It is famous for its orderly system of waterways, bridges, and architecture of its traditional residents, the Nakhi people. The town has retained a historic townscape of high quality and authenticity. Its architecture is noteworthy for the blending of elements from several cultures that have come together over the centuries.", "city": 8},{"id": 21, "name": "Jade Dragon Snow Mountain", "description": "Jade Dragon Snow Mountain (Yulong Mountain) is the southernmost glacier in the Northern Hemisphere. Consisting of 13 peaks, among which Shanzidou is the highest with an altitude of 5,600 meters (18,360 feet), the mountain stretches a length of 35 kilometers (22 miles) and a width of 20 kilometers (13 miles). Looking from Lijiang Old Town in the south which is 15 kilometers (nine miles) away, the snow-covered and fog-enlaced mountain resembles a jade dragon lying in the clouds, hence the name.", "city": 8},{"id": 22, "name": "Lugu Lake", "description": "Lugu Lake is called the mother lake by the Mosuo people. The lakes shores are inhabited by many minority ethnic groups, such as the Mosuo, Norzu, Yi, Pumi and Tibetan. The most numerous of these are the Mosuo people, said to be a sub clan of the Naxi people (as per Chinese records of Minorities in China) with ancient family structure considered as a live fossil for researching the marital development history of Human beings and the last quaint Realm of Matriarchy.", "city": 8},{"id": 23, "name": "Pudacuo National Park", "description": "The Pudacuo (Potatso) National Park is located in one of the most biodiverse regions of the world. While the region comprises only 0.7 percent of Chinas land area, it contains more than 20 percent of the countrys plant species, about one-third of its mammal and bird species and almost 100 endangered species.", "city": 8},{"id": 24, "name": "Ristorante dei Musei Vaticani", "description": "The Ristorante dei Musei Vaticani is steps away from St. Peters Square and the historical center, almost opposite the entrance to the Vatican Museums, the Vatican Museum metro station is a five minute walk away.", "city": 9},{"id": 25, "name": "Basilica souveneir shops", "description": "There are various gift stores in the Vatican where you can find outstanding items that are associated with the Catholic faith and the Vatican in general. You can find gift shops in the Vatican Library, Museums and others stores specified for this purpose.", "city": 9},{"id": 26, "name": "St peters square", "description": "St. Peters Square, is a massive plaza located directly in front of St. Peters Basilica in the Vatican City, the papal enclave surrounded by Rome, directly west of the neighbourhood or rione of Borgo.", "city": 9},{"id": 27, "name": "Grand Canyon Village", "description": "Grand Canyon Village is the most popular entryway into the park and, as such, often suffers from heavy crowds during the peak seasons in spring, summer and fall.", "city": 10},{"id": 28, "name": "North Rim", "description": "The North Rim has a reputation for its rugged, isolated trails, its sparse facilities appeal in the eyes of the tourist mainstream.Popular spots in the North Rim include Bright Angel Point, which allows views of the Roaring Springs, the North Rims only water source. You should also swing by the 8,803-foot Point Imperial, the highest point on the North Rim. Lodging is available at the Grand Canyon Lodge, the only available lodge on the North Rim. Rates run in the high $100s, and reservations (the earlier the better) are an absolute must.", "city": 10},{"id": 29, "name": "Colorado River Rafting", "description": "To see the Grand Canyon from a different point of view, consider taking a rafting trip down the Colorado River or Hualapai River.", "city": 10},{"id": 30, "name": "Blue Bayou", "description": "Elegant dining, considered one of the most romantic restaurants in Cancun, featuring Cajun & Creole specialties from New Orleans, in a lush Bayou setting with live Jazz music. Blue Bayou is the only restaurant in Cancun claming the Dirona award (Distinguished Restaurant of North America) since 1998. and The AAA Four Diamond Award Since 2003.", "city": 11},{"id": 31, "name": "Kukulcan Plaza", "description": "Kukulcan Plaza is the most exclusive and luxurious shopping center in all of Cancun and the Riviera Maya. It is located in the Hotel Zone, where the main Five Star and Grand Tourism hotels are situated. Kukulcan Plazas offerings range from boutiques of worldwide renown, jewelry shops with fine gems of prestigious designers, elegant perfumeries, and fine restaurants, to shops that offer handicrafts and even bowling! Shopping in Cancun is an excellent option.", "city": 11},{"id": 32, "name": "Westin Regina Resort", "description": "Lounge endlessly at our glorious private beaches and four outdoor pools. Pamper yourself at the luxurious Heavenly Spa by Westin. Or pick up the pace with countless water sports, plus tennis, golf, a top-notch gym, and fascinating local tours and day trips. Features & Activities Overview: Hotel Amenities, Beaches and Water Sports, Nearby Golf, WestinWORKOUT Fitness Studio, Westin Kids Club, Outdoor Lighted Tennis Courts, Heavenly Spa by Westin, Outdoor Pools, Internet Access, Environmental Practices, Pet Service, Tour Service, SPG Kids Pass, SuperFoodsRx, The Westin Eat Well Menu for Kids", "city": 11},{"id": 33, "name": "Giza Zoo", "description": "The Giza Zoo is a zoological garden in Giza, Egypt. It is one of the few green areas in the city, and includes Gizas largest park. The zoo covers about 80 acres, and is home to many endangered species, as well as a selection of endemic fauna.", "city": 12},{"id": 34, "name": "Giza Plateau", "description": "The Giza Plateau (Arabic) is a plateau that is located in Giza, Egypt. The famous Giza Necropolis is located in this geographical area, which is characterized by a sandy, desert climate and terrain with little vegetation. The plateau and its monuments have been recorded in the Giza Plateau Mapping Project run by Ancient Egypt Research Associates, directed by Dr. Mark Lehner. Modern Gizas layout is accessed by two main roads. The first from the North leads to Khufus pyramids and the other road leads near the sphinxs forecourt from the East. They crossed [the Nile River] from the East bank and followed the causeway westward. Dominating the plateau and running in a South-West diagonal through the site are the three pyramids of the kings [Khufu],[Khafra]and [Menkaura]. The northern most and the largest one belong the king Khufu. King Khafras pyramid is build precisely on a south-west diagonal to his fathers pyramid king Khufu, swell of been build on higher ground to create the illusions of been bigger. The pyramid of King Menkaura is much smaller and is not align along the same diagonal line as the other two pyramids.", "city": 12},{"id": 35, "name": "Egyptian Museum", "description": "The Museum of Egyptian Antiquities, known commonly as the Egyptian Museum or Museum of Cairo, in Cairo, Egypt, is home to an extensive collection of ancient Egyptian antiquities. It has 120,000 items, with a representative amount on display, the remainder in storerooms.", "city": 12},{"id": 36, "name": "Four Seasons Cairo ", "description": "Located on the west bank of the Nile, 5 km (3 miles) from downtown Cairo Birds eye views of the great Pyramids, the Zoological Gardens and the Nile. Part of the luxurious First Place Complex, a multi-use development with upscale shopping boutiques, restaurants and one of Cairos chic night-life venues and private residences 20 floors, rooms start on 5th. 269 rooms and 43 suites Extensive health club facilities including 24 hr state-of-the-art gym with views overlooking the Nile, Luxurious Spa and Wellness Center including couples suite. Elegant dining options with international flavours, including Thai, Syrian and contemporary Italian cuisine, two Lounge/Bar Outdoor pool, including dedicated childrens pool and stylish Bar area, an oasis in the heart of the city. Dedicated Kids Suite, first of its kind in Cairo. Offering a range of exciting, fun and educational activities from arts & crafts, Wii and Playstation game consoles, to a selection of childrens books. Hotel is integrated with three levels of the First Place Complex.", "city": 12}]
        self.assertTrue(content==reps)

    def test_activities_404(self):
        response = requests.get(self.url + "activities/bogus/")
        self.assertEqual(response.status_code, 404)

    def test_activities_id_2(self):
        response = requests.get(self.url + "activities/2/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 2, "name": "Sydney Opera House", "description": "The Sydney Opera House is a multi-venue performing arts centre in Sydney, New South Wales, Australia. Situated on Bennelong Point in Sydney Harbour, close to the Sydney Harbour Bridge, the facility is adjacent to the Sydney central business district and the Royal Botanic Gardens, between Sydney and Farm Coves.", "city": 1}]
        self.assertTrue(content==resp)

    def test_activities_id_3(self):
        response = requests.get(self.url + "activities/3/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 3, "name": "Shelly Beach", "description": "Shelly Beach (also known as Shelley Beach) is a beach located in Manly, a suburb of Sydney, New South Wales, Australia. It is adjacent to North Head and Fairy Bower. Shelly Beach is the only west facing beach on the eastern coast of Australia.", "city": 1}]
        self.assertTrue(content==resp)

    def test_activities_id_4(self):
        response = requests.get(self.url + "activities/4/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 4, "name": "Taj Mahal", "description": "The Taj Mahal from Persian and Arabic, crown of palaces is a white marble mausoleum located in Agra, Uttar Pradesh, India. It was built by Mughal emperor Shah Jahan in memory of his third wife, Mumtaz Mahal. The Taj Mahal is widely recognized as the jewel of Muslim art in India and one of the universally admired masterpieces of the worlds heritage.", "city": 2}]
        self.assertTrue(content==resp)

    def test_activities_id_5(self):
        response = requests.get(self.url + "activities/5/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 5, "name": "Buzzaria", "description": "Buzzaria is a retail destination store full of very interesting,quirky ethnic Indian products.Coined from an hindi word Bajaria meaning village market place and the word Buzz.Carrying over 50000 products.From Saris to handmade soaps to fashion to handcrafted products to jewelry to some amazing cushion covers.Open most days of the year,a shoppers paradise and a creative and buzzing hot spot.A place overflowing with passion and color and happiness.", "city": 2}]
        self.assertTrue(content==resp)

    def test_activities_id_7(self):
        response = requests.get(self.url + "activities/7/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 7, "name": "The Hermitage", "description": "The Hermitage is a museum of art and culture in Saint Petersburg, Russia. It is one of the largest and oldest museums in the world, as it was found in 1764 by Catherine the Great and opened to the public in 1852. It host over three million items which only a small portion is on permanent display.", "city": 3}]
        self.assertTrue(content==resp)

    def test_activities_id_8(self):
        response = requests.get(self.url + "activities/8/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 8, "name": "Church of the Savior on Blood", "description": "Known by many different names such as Church of Spilled Blood, Church on Split Blood, and Cathedral of the Resurrection of Christ was built in honor of the assasinated Tsar Alexander II. Construction of the church began in 1883 and was completed in 1907. It is considered a State Historical Museum by Russia and is one of the main attractions of Saint Petersburg. One of the churchs main features are its colorful onion domes.", "city": 3}]
        self.assertTrue(content==resp)

    def test_activities_id_9(self):
        response = requests.get(self.url + "activities/9/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 9, "name": "Catherine Palace", "description": "The Catherine Palace is only 25km from the city of Saint Petersburg is one of the top tourist destinations for tourist of Saint Petersburg. the Boaroque 18th-century place was where the Russian royal family spent their summers. It was first constructed 1717, but since has been remodeled through the year by multiple Tsars. It is most known for its beautiful light blue walls of the palace.", "city": 3}]
        self.assertTrue(content==resp)

    def test_activities_id_10(self):
        response = requests.get(self.url + "activities/10/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 10, "name": "Wat Arun", "description": "The Wat Arun, or Temple of Dawn is a Buddhist temple in the Bangkok Yai district of Bangkok. It is among the most know landmarks in Thailand and the first light of the monrning reflects of the surcface of the temple with pearly iridescence. It was founded before 1656 BE so it makes it one of Bangkok oldest temples.", "city": 4}]
        self.assertTrue(content==resp)




#Testing languages
class LanguagesApiTest(TestCase) :
    url = "http://flappybirds.pythonanywhere.com/api/"

    def test_languages_404(self):
        response = requests.get(self.url + "languages/bogus/")
        self.assertEqual(response.status_code, 404)


    def test_languages_id_1(self):
        response = requests.get(self.url + "languages/1/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 1, "name": "arabic", "description": "Arabic is a name for what are traditionally considered the descendants of the Classical Arabic language of the 6th century. This includes both the literary language and varieties of Arabic spoken in a wide arc of territory, stretching across the Middle East, North Africa, the Horn of Africa. Arabic belongs to the Afro-Asiatic family."}]
        self.assertTrue(content==resp)

    def test_languages_id_2(self):
        response = requests.get(self.url + "languages/2/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 2, "name": "cantonese", "description": "Cantonese is a language that originated in the vicinity of Canton (i.e., Guangzhou) in southern China, and is spoken by approximately 62 million speakers worldwide.[4] It is often regarded as the prestige dialect of Yue. It is an official language in Hong Kong (along with English) and in Macau (along with Portuguese). It is sometimes also known as Guangfuhua a broader definition which also includes the Guangzhou dialect, Hong Kong dialect, Xiguan dialect, Wuzhou dialect, and Tanka dialect."}]
        self.assertTrue(content==resp)

    def test_languages_id_3(self):
        response = requests.get(self.url + "languages/3/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 3, "name": "greek", "description": "Greek is an independent branch of the Indo-European family of languages, native to the southern Balkans, the Aegean Islands, western Asia Minor and Cyprus. It has the longest documented history of any Indo-European language, spanning 34 centuries of written records.[10] Its writing system has been the Greek alphabet for the majority of its history; other systems, such as Linear B and the Cypriot syllabary, were used previously. The alphabet arose from the Phoenician script and was in turn the basis of the Latin, Cyrillic, Coptic, and many other writing systems."}]
        self.assertTrue(content==resp)

    def test_languages_id_4(self):
        response = requests.get(self.url + "languages/4/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 4, "name": "vietnamese", "description": "Vietnamese is the national, official language of Vietnam. It is the native language of Vietnamese people (Kinh), and of about three million Vietnamese residing elsewhere. It also is spoken as a first or second language by many ethnic minorities of Vietnam."}]
        self.assertTrue(content==resp)

    def test_languages_id_5(self):
        response = requests.get(self.url + "languages/5/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 5, "name": "punjabi", "description": "Punjabi is an Indo-Aryan language spoken by 130 million native speakers worldwide, making it the 10th most widely spoken language (2013) in the world. It is the native language of the Punjabi people who inhabit the historical Punjab region of Pakistan and India. It is the only tonal language among the Indo-Aryan languages."}]
        self.assertTrue(content==resp)

    def test_languages_id_7(self):
        response = requests.get(self.url + "languages/7/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 7, "name": "urdu", "description": "Urdu, or more precisely Modern Standard Urdu, is a standardized register of the Hindustani language. Urdu is historically associated with the Muslims of the region of Hindustan. It is the national language and lingua franca of Pakistan, and an official language of six Indian states and one of the 22 scheduled languages in the Constitution of India. Apart from specialized vocabulary, Urdu is mutually intelligible with Standard Hindi, which is associated with the Hindu community. Since the end of the Mughal period in the nineteenth century, varieties of Hindustani have been the lingua franca for much of South Asia."}]
        self.assertTrue(content==resp)

    def test_languages_id_8(self):
        response = requests.get(self.url + "languages/8/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 8, "name": "marathi", "description": "Marathi is an Indo-Aryan language. It is the official language of Maharashtra state of India and is one of the 23 official languages of India. There were 73 million speakers in 2001; Marathi has the fourth largest number of native speakers in India. The major dialects of Marathi are called Standard Marathi and Warhadi Marathi. There are a few other sub-dialects like Ahirani, Dangi, Vadvali, Samavedi, Khandeshi, and Malwani. Standard Marathi is the official language of the State of Maharashtra."}]
        self.assertTrue(content==resp)

    def test_languages_id_9(self):
        response = requests.get(self.url + "languages/9/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 9, "name": "gujarati", "description": "Gujarati is an Indo-Aryan language native to the west Indian region of Gujaray. It is part of the greater Indo-European language family. Gujaraui is descended from Old Gujarati (c. 1100 - 1500 AD), which is also the ancestor of modern Rajasthani. In India, it is the chief language in the state of Gujarat, as well as an official language in the union territories of Daman and Diu and Dadra and Nagar Haveli."}]
        self.assertTrue(content==resp)

    def test_languages_id_10(self):
        response = requests.get(self.url + "languages/10/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        reps = [{"id": 10, "name": "Russian", "description": "A Slavic language mainly spoken in the Russian Federation, Belarus, and Krygyzstan. It belongs to the family of Indo-European languages and is one the three living members of the East Slavic languages. It is written in Cyrillic script."}]
        self.assertTrue(content==reps)


