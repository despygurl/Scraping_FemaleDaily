import scrapy

class PostsSpider(scrapy.Spider):
    name = "review"
    allowed_urls = ['https://femaledaily.com']
    start_urls = ['https://reviews.femaledaily.com/?page={hal}'.format(hal = i)for i in range(0,1000)]


    def parse(self, response):
        for post in response.css('.jsx-837185867.home-component-review-card'):
            yield {
                'Username': post.css('.profile-username a::text').get(),
                'User Age': post.css('.profile-description::text').get().split(sep=',')[-1],
                'User Skin Condition': post.css('.profile-description::text').get().split(sep=',')[:-1],
                'Recommendation Status' : post.css('p.recommend b::text').get(),
                'Usage Period' : post.css('.information-wrapper b::text')[1].get(),
                'Purchase Point' : post.css('.information-wrapper b::text')[3].get(),
                'Product Brand' : post.css('.product-brand a::text').get(),
                'Product Name' : post.css('.product-name a::text').get(),
                'Product Rating' : post.css('.rating-text::text').get(),
                'Total Users Rated' : post.css('.rating-total::text')[1].get(),
                'User Review' : post.css('.text-content span::text').get()
            }