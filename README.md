# Foodie Review
### Data Centric Development Project (Code Institute)

This project is built as a webpage for food lovers to read and write reviews about foods from various restaurants..

![Mockup image](https://res.cloudinary.com/dhktrng6p/image/upload/v1596277181/Screenshot_2020-08-01_at_6.19.24_PM_wjyjjp.png "Devices Mockup")

## Objective
Food is a basic necessity for all. The modern world is a food paradise and people are willing to queue and try new and fun food. To ensure that their time and effort is worth it, people will usually check on food reviews to ensure the quality of food. 

For a demand side, people love taking photos of their “Instagram-worthy” food but are all the “Instagram-worthy” delicious and worth the hype?

This platform enables users to share their love for food and experience by publishing reviews and sharing with the community. By providing a review, they are paying it forward and help others in making good food choices. 


External user’s goal:
To share the love for food by publishing reviews and clock points to get exclusive discount codes.

Site owner’s goal:
Provide a platform for food reviews to share the love for food and expand the user base to attract restaurant owners to purchase advertising space eventually.

## UX
The idea behind the UX is for simple navigation and to provide minimal steps for users to access the desired information required, with a clean and unclutered web interface.

Information on the several restaurants such as website and address can be found on the home page. Users can be easily redirected to the several restaurants’ website if they would like to find out more. Search button is displayed prominently at the top menu bar to enable users to search for their preferred restaurants.

When clicking into the respective restaurant to find out more information, there is a “Back to Main Page” on the top banner to navigate back to the home page. The “New Review” button is also placed at the top of the page to allow users to add a review without looking through the other reviews. All the past reviews are ranked based on dates. The food item that was reviewed is also clearly displayed in the title of the reviews to enable easy viewing. Users can also do real-time updates of the reviews. Upon completion of the review, there is also a button to return to the main page. If users accidentally click the “Delete” button, there is an error message to prompt users that the action is irreversible and to confirm the action. Users can click “Cancel” to go back to the home page.

With the tagging of halal and type of cuisine, the website enables users to filter the results based on their preferences and dietary requirements.

Users are directed back the home page if there are no reviews for the restaurant which they are interested in.

## UI

### Features
The webpage has the following features:

- The home page layout displays the image of the restaurant in a structured and standardized format with essential information within one glance. 
    - The restaurants are displayed as cards in a masonry layout for a modern and clean look.
- Only key information such as address and website is reflected to prevent overcrowding of the home page. 
- Information about each restaurant can be easily retrieved by clicking on the image of the restaurant or the “View More” button. 
- Upon hovering of the mouse over the buttons, the buttons will be highlighted. 
    - Blue is used as a neutral colour to indicate update. 
    - Red is used for delete to ensure that users do not click on the button. 
    - Green is used for addititional information.
    - Dark grey is to indicate navigating backwards.
- Consistent background and orange background is consistent across all the webpages, as orange gives off a vibrant and energetic mood which synergizes with the idea of food.

### Future Features
- User authentication to be added such that users can only edit the reviews which they have uploaded 
- Restaurants that appear on the Home page indicate the number of reviews
- Star ranking system to rate the restaurants to indicate positivity of reviews
- Ranking of each of the restaurants based on the star system in order
- Creation of advertising space for restaurants who would like to be featured
- A points system for users based on the number of reviews to earn perks in the future
- To provide an advanced filtering of restaurants according to the type of cuisines, halal certified restaurants, etc.

## Technologies Used
The following programming languages and tools were used to build the website:
* HTML 5
* CSS 
* JavaScript 
* Bootstrap v4.4 toolkit to organize the elements in the page
* jQuery library for DOM manipulation
* Python 
* Flask
* Gitpod for the writing of codes and testing of website
* Mongodb Atlas for the hosting of database
* W3C Markup Validation Service for HTML and CSS validation
* GitHub
* Cloudinary image hosting

## Database
- Mongodb was selected as the choice of database due to its simplicity, as the database required for this project is a simple and structured way of storing the necessary information based on:
    1. First level of data to be restaurant details 
    2. Second level of data to be an array of several reviews
        - Reviews to be stored as objects, each with an unique id.
- The database is hosted and stored in MongoDB Atlas

## Testing
The website has been tested for viewing and responsiveness on various screen sizes, including but not limited to the following web browsers and devices:

* Apple Safari Web Browser
    1. macOS 
    2. Windows 10
    3. iOS
    4. iPadOS
* Mozilla Firefox Web Browser
    1. macOS
    2. Windows 10
    3. Android 10
* Microsoft Edge Web Browser
    1. macOS
    2. Windows 10
    3. Android 10
* Google Chrome Web Browser
    1. macOS
    2. Windows 10
    3. Android 10

- HTML, CSS validated by W3C Markup Validation
- JavaScript Syntax validated by Esprima

1.  Testing was first done by applying CRUD to the database and images uploading onto cloudinary using the built web interface. Upon successful CRUD operations and image uploading, the hosted webpage is then provided to random testers to test out the CRUD operations and UX and their feedback is taken into consideration.
2. After the testing is done, additional features are added based on priority versus estimated time required to implement, remaining features will be added in the future. 
3. The web application is then tested on various web browsers and device screens for compatibility purposes.
4. The edited final web application is then updated onto the host server

## Deployment
The website is deployed on Heroku, using GitHub to host the project repository. The website can be found at this [link](http://foodiereview.herokuapp.com).
- Database passwords and session keys are stored in the .env file which is included in the .gitignore.


## Credits
This website was built using tools and data from various sources, including but not limited to the following:

- [Heroku](https://www.heroku.com) for the hosting of the web application.

- Background image was obtained from [Unsplash](https://unsplash.com/).

- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) for the hosting and storage of database.

- Sample data images from [eatbook.sg](https://eatbook.sg)

Last but not least, to [Trent Global](https://www.trentglobal.edu.sg/diplomainsoftwaredevelopment/?gclid=EAIaIQobChMI8M3ezf6t6QIV2BwrCh2R6A44EAAYASAAEgL6__D_BwE) and [Code Institute](https://codeinstitute.net) for the teachings and support to have made this project possible. 