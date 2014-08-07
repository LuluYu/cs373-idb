"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from content_display.models import Cities, Activities, Languages
import urllib2
import json
import requests
from requests.exceptions import HTTPError



# Testing Cities api with real data
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


# Testing Languages api with real data
class LanguagesApiTest(TestCase) :
    url = "http://flappybirds.pythonanywhere.com/api/"
    def test_cities(self):
        response = requests.get(self.url + "languages/")
        self.assertEqual(response.status_code, 200)
        content = response.json()
        resp = [{"id": 1, "name": "arabic", "description": "Arabic is a name for what are traditionally considered the descendants of the Classical Arabic language of the 6th century. This includes both the literary language and varieties of Arabic spoken in a wide arc of territory, stretching across the Middle East, North Africa, the Horn of Africa. Arabic belongs to the Afro-Asiatic family."},{"id": 2, "name": "cantonese", "description": "Cantonese is a language that originated in the vicinity of Canton (i.e., Guangzhou) in southern China, and is spoken by approximately 62 million speakers worldwide.[4] It is often regarded as the prestige dialect of Yue. It is an official language in Hong Kong (along with English) and in Macau (along with Portuguese). It is sometimes also known as Guangfuhua a broader definition which also includes the Guangzhou dialect, Hong Kong dialect, Xiguan dialect, Wuzhou dialect, and Tanka dialect."},{"id": 3, "name": "greek", "description": "Greek is an independent branch of the Indo-European family of languages, native to the southern Balkans, the Aegean Islands, western Asia Minor and Cyprus. It has the longest documented history of any Indo-European language, spanning 34 centuries of written records.[10] Its writing system has been the Greek alphabet for the majority of its history; other systems, such as Linear B and the Cypriot syllabary, were used previously. The alphabet arose from the Phoenician script and was in turn the basis of the Latin, Cyrillic, Coptic, and many other writing systems."},{"id": 4, "name": "vietnamese", "description": "Vietnamese is the national, official language of Vietnam. It is the native language of Vietnamese people (Kinh), and of about three million Vietnamese residing elsewhere. It also is spoken as a first or second language by many ethnic minorities of Vietnam."},{"id": 5, "name": "punjabi", "description": "Punjabi is an Indo-Aryan language spoken by 130 million native speakers worldwide, making it the 10th most widely spoken language (2013) in the world. It is the native language of the Punjabi people who inhabit the historical Punjab region of Pakistan and India. It is the only tonal language among the Indo-Aryan languages."},{"id": 6, "name": "hindi", "description": "Hindi, or more precisely Modern Standard Hindi, is a standardised and Sanskritised register of the Hindustani language. Hindustani is the native language of most people living in Delhi, Uttar Pradesh, Uttarakhand, Chhattisgarh, Himachal Pradesh, Chandigarh, Bihar, Jharkhand, Madhya Pradesh, Haryana, and Rajasthan. Modern Standard Hindi is one of the official languages of India."},{"id": 7, "name": "urdu", "description": "Urdu, or more precisely Modern Standard Urdu, is a standardized register of the Hindustani language. Urdu is historically associated with the Muslims of the region of Hindustan. It is the national language and lingua franca of Pakistan, and an official language of six Indian states and one of the 22 scheduled languages in the Constitution of India. Apart from specialized vocabulary, Urdu is mutually intelligible with Standard Hindi, which is associated with the Hindu community. Since the end of the Mughal period in the nineteenth century, varieties of Hindustani have been the lingua franca for much of South Asia."},{"id": 8, "name": "marathi", "description": "Marathi is an Indo-Aryan language. It is the official language of Maharashtra state of India and is one of the 23 official languages of India. There were 73 million speakers in 2001; Marathi has the fourth largest number of native speakers in India. The major dialects of Marathi are called Standard Marathi and Warhadi Marathi. There are a few other sub-dialects like Ahirani, Dangi, Vadvali, Samavedi, Khandeshi, and Malwani. Standard Marathi is the official language of the State of Maharashtra."},{"id": 9, "name": "gujarati", "description": "Gujarati is an Indo-Aryan language native to the west Indian region of Gujaray. It is part of the greater Indo-European language family. Gujaraui is descended from Old Gujarati (c. 1100 - 1500 AD), which is also the ancestor of modern Rajasthani. In India, it is the chief language in the state of Gujarat, as well as an official language in the union territories of Daman and Diu and Dadra and Nagar Haveli."},{"id": 10, "name": "Russian", "description": "A Slavic language mainly spoken in the Russian Federation, Belarus, and Krygyzstan. It belongs to the family of Indo-European languages and is one the three living members of the East Slavic languages. It is written in Cyrillic script."},{"id": 11, "name": "Thai", "description": " Thai, or Siamese, is the national and official language of Thailand. It is a memeber of the Tai group of the Tai-Kadai language family. It heavly borrows words from Pali, Sanskrit, and Old Khnmer languages. The Thai Script has 44 consonant letters and 15 vowel symbols."},{"id": 12, "name": "Portuguese", "description": "Portuguese is a Romance language and the sole official language of Portugal, Brazil, Mozambique, Angola, Cape Verde, Guinea-Bissau, and São Tomé and Príncipe. It also has co-official language status in Macau (China), Equatorial Guinea and East Timor. As the result of expansion during colonial times, Portuguese speakers are also found in Goa, Daman and Diu in India, in Batticaloa on the east coast of Sri Lanka, and in Malacca in Malaysia."},{"id": 13, "name": "Chinese", "description": "After the fall of the Northern Song dynasty, and during the reign of the Jin and Yuan dynasties in northern China, a common speech developed based on the dialects of the North China Plain around the capital, a language referred to as Old Mandarin. The present Chinese language varieties developed from regional variants of Old Chinese and Middle Chinese. In the early years of the Republic of China, intellectuals of the New Culture Movement, such as Hu Shih and Chen Duxiu, successfully campaigned for the replacement of Literary Chinese as the written standard by written vernacular Chinese, which was based on northern dialects. A parallel priority was the definition of a standard national language. After much dispute between proponents of northern and southern dialects and an abortive attempt at an artificial pronunciation, the National Language Unification Commission finally settled on the Beijing dialect in 1932, which is retained till today."},{"id": 14, "name": "German", "description": "German is a West Germanic language. It derives most of its vocabulary from the Germanic branch of the Indo-European language family. It is the only official language of Germany, Austria, and Liechtenstein; one of the official languages of Switzerland, Luxembourg, and Belgium; and a recognised minor language in many other countries, such as Italy, Slovenia, Hungary, Namibia, and Poland. The history of the language begins with the High German consonant shift during the migration period, separating Old High German dialects from Old Saxon. As Germany was divided into many different states, the only force working for a unification or standardization of German for several hundred years was the general wish of writers to be understood by as many readers as possible."},{"id": 15, "name": "English", "description": "English is a West Germanic language that was first spoken in early medieval England and is now a global lingua franca.[4][5] It is spoken as a first language by the majority populations of several sovereign states, including the United Kingdom, the United States, Canada, Australia, Ireland, New Zealand and a number of Caribbean nations; and it is an official language of almost 60 sovereign states. It is the third-most-common native language in the world, after Mandarin Chinese and Spanish.[6] It is widely learned as a second language and is an official language of the European Union, many Commonwealth countries and the United Nations, as well as in many world organisations."},{"id": 16, "name": "Italian", "description": " Italian is a Romance language spoken mainly in Europe: Italy, Switzerland, San Marino, Vatican City, as a second language in Malta, Slovenia and Croatia, by minorities in Eritrea, France, Libya, Monaco, Montenegro, and Somalia, and by expatriate communities in the Americas and Australia. Many speakers are native bilinguals of both standardised Italian and other regional languages. According to the Bologna statistics of the European Union, Italian is spoken as a native language by 59 million people in the EU (13% of the EU population), mainly in Italy, and as a second language by 14 million (3%).Including the Italian speakers in non-EU European countries (such as Switzerland and Albania) and on other continents, the total number of speakers is around 85 million."},{"id": 17, "name": "Spanish", "description": "Spanish is a Romance language that originated in Castile, a region of Spain. Approximately 414 million people speak Spanish as a native language, making it second only to Mandarin in terms of its number of native speakers worldwide.[1][2] There are more than 500 million Spanish speakers as a first or second language, and 20 million students of Spanish as a foreign language.[4] Spanish is one of the six official languages of the United Nations, and it is used as an official language by the European Union, Mercosur, and the Pacific Alliance. Spanish is spoken fluently by 15% of all Europeans, making it the 5th-most spoken language in Europe."},{"id": 18, "name": "Egyptian Arabic", "description": "Egyptian Arabic is the language spoken by most contemporary Egyptians. It is more commonly known locally as the Egyptian colloquial language or Egyptian dialect. Egyptian Arabic is a variety of the Arabic languages of the Semitic branch of the Afroasiatic language family. It originated in the Nile Delta in Lower Egypt around the capital Cairo. Descended from the spoken Arabic brought to Egypt during the seventh-century AD Muslim conquest, its development was influenced by the indigenous Coptic of pre-Islamic Egypt, and later by other languages such as Turkish/Ottoman Turkish, Italian, French and English. The 80 million Egyptians speak a continuum of dialects, among which Cairene is the most prominent. It is also understood across most of the Arab World due to the predominance of Egyptian media, making it the most widely spoken and one of the most widely studied varieties of Arabic."}]
        self.assertTrue(content==resp)

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
        resp = [{"id": 10, "name": "Grand Canyon National Park", "description": "Grand Canyon is in the northwest corner of Arizona, close to the borders of Utah and Nevada. The Colorado River, which flows through the canyon, drains water from seven states, but the feature we know as Grand Canyon is entirely in Arizona. Most of the Grand Canyon lies within Grand Canyon National Park and is managed by the National Park Service. "}]
        self.assertTrue(content==resp)


