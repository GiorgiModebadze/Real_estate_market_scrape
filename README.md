## This project intends to monitor price change on Georgian Real Estate Market

### Step 1:
First, one popular Georgian Real Estate Market web-page is scraped.
General Strategy :

Page uses simple logic for specific items.

    https://www.myhome.ge/en/pr/"itemID"
To access data about specific item only change of _itemID_ is necessary.

For that reason first we scrape main page where we get all item ids and create
list of it. 
Then this list is provided to the special function which goes one by one and gets
data regarding each specific item.

### Scraped data: 

All the relevant data that can be used for analysis is scraped

Example:
```json
{
    "id": "9420744",
    "link": "https://www.myhome.ge/en/pr/9420744",
    "address": "ანა  პოლიტკოვსკაიას 27 ბინა 3, Saburtalo, Saburtalo District, Tbilisi",
    "lat": "41.720836902992",
    "long": "44.710566957012",
    "price_gel": "122,600",
    "price_usd": "43,000",
    "b_type": "Old Building",
    "area": "54",
    "d_original": "იყიდება 2 ოთახიანი ბინა ა.პოლიტკოვსკაიას N27 (ყოპილი ჯიქია) ბინა არის ახალი გარემონტებული,  ბინას აქვს დუპლექსის პერსპეკტივა, რომელიც არის რეესტრში დამოწმებული, ჭერის საერთო სიმაღლე შეადგენს 5 მეტრს, ამჟამად არის 3,20 გადატიხრული, ასევე შესაძლებელია სარდაფის და აივმის გაკეთება, ბინაში არის ცენტრალური გათბობა. 593 57 57 29 gia",
    "d_translated": "2 bedroom apartment for sale. Politkovskaya&#39;s N27 (former jikia) apartment is newly renovated, the apartment has a duplex prospectus that is certified in the registry, the total ceiling height is 5 meters, is currently 3,20 bundled, it is also possible to make basement and hvim in the apartment Central heating. 593 57 57 29 gia",
    "amenities": [
      "Newly renovated",
      "Nonstandard",
      "Ceiling height 3.20 M",
      "Bedroom 1",
      "Bath Bathrooms 1",
      "Heating Central Heating System",
      "Hot water Central Heating System",
      "Gas",
      "Internet"
    ],
    "similar_items": [
      "8950564",
      "9039188",
      "9160931",
      "9162857",
      "9280085",
      "8710682",
      "9163160",
      "9218598",
      "9322883",
      "9364654",
      "9366955",
      "9377714",
      "9387999",
      "9394602",
      "9398971"
    ]
}
```

### DB Strategy

As for now for saving file simple JSON files are used.

Files are saved incrementally as the whole web-page is big and some errors might
occur during process. 

So with this we avoid data loss as much as possible


### Next Steps.
1) Scrape whole webpage
2) Add date to the data
3) Create list of already scraped items and check before scraping
if they are already scraped
4) Exploratory Data Analysis
5) Interactive Dashboard 