from autoscraper import AutoScraper

url = "https://www.amazon.com/s?k=iphones&crid=2G7PP2ZPIOG63&sprefix=iphone%2Caps%2C408&ref=nb_sb_noss_1"

wanted_list = ["$124.95", "Apple iPhone SE 2nd Generation, US Version, 64GB, Black - Unlocked (Renewed)", "15579"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
# scraper.get_result_similar(result, grouped=True)
print(result)


