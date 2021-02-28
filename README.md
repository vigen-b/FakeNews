# FakeNews
Simple FakeNews app with Django

## Requirements

### Publishing

- Code should be put on a public GitHub/GitLab with a Readme with details
- Running the application should be put on a cloud server like  AWS, Azure, or Google Cloud, and access provided to review

### Task

Create simple news portal using Django framework.

#### Administaractor part (Django Admin UI):

- The administrator should be able to create and modify news from the admin panel using a rich text editor.
- The administrator should be able to create categories and assign them to the news.
- Any news can have one or more categories but only one of them should be defined as "The main category". News
- News without the main category is not allowed. Example of categories: "Politics" "Business" "Tech" "Science" "Health", etc.
- Example of categories: "Politics" "Business" "Tech" "Science" "Health", ets.
- Add list views for categories and news
- Add category and date filters for news list
- Frontend part (Custom HTML/CSS (framework is optional)):

Site should consists of next pages:
#### Home page:
- list of categories
- list of all news from all categories

#### Category page:
- list of categories.
- selected category should be higlited
- list of all news filtered selected category


#### News detail page:
- title of news
- all related categories
- news content

Each item news in the listing should represent title, main category and creation date.
News in the listing should be paginated by 10 items.
News in the listing should be ordered by creation date.

Only backend functionality will be evaluated. There are no any specific requirements for the frontent part.
Any additional css and frontend frameworks are not required but may be used on personal initiative only after required part will be done.


