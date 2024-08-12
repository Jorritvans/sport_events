# Sportify
Sportify is a dynamic platform where users can discover, participate in, and engage with various sports events. This web application allows users to register, book events, and interact with other sports enthusiasts through comments.

### Portfolio Project - Django Web Application
The purpose of this project was to build an interactive web application using Django that allows users to explore and engage with sports events in their area.

## Link to app

[Link to Sportify](https://your-deployment-link.com)

## How to Use

In Sportify, users can browse through a list of available sports events, view details about each event, book tickets, and leave comments. To access these features, users need to register an account and log in.

- **Register:** Create a new user account to start booking events and leave comments.
  
- **Login:** Access your account to view and manage your bookings and interact with events.
  
- **Browse Events:** Explore the homepage to find upcoming sports events.
  
- **Event Details:** Click on an event to view more details, including the description, date, location, and price.
  
- **Book Tickets:** Book your spot for an event by selecting the number of tickets you want to purchase.
  
- **Comments:** Leave a comment on an event to engage with other participants.

## Features
- **User Registration:** Users can create a new account by providing a username, email, and password.
- **User Login:** Users can log in to access their account and view their bookings.
- **Event Booking:** Users can book tickets for events and manage their bookings.
- **Comment System:** Users can leave comments on events, edit their comments, and delete them if necessary.
- **Responsive Design:** The application is fully responsive and accessible on various devices.

## Technologies Used

- **Programming Languages:**
  - Python
  - HTML
  - CSS
  - JavaScript
- **Framework:**
  - Django
- **Database:**
  - SQLite (during development)
  - PostgreSQL (for production)
- **Deployment:**
  - Heroku
- **Version Control:**
  - Git
  - GitHub

## Development

The development of this application involved setting up Django models, views, and templates to manage user interactions with events. The comment system was implemented to allow users to engage with events and other participants.

## Data Model

- **Events:** Each event includes a title, description, date, location, price, and image.
- **Bookings:** Users can book tickets for events, with each booking linked to a specific event and user.
- **Comments:** Users can leave comments on events, and each comment is linked to a specific event and user.

## Testing

### Manual Testing

The following table summarizes the tests performed on various components of the Sportify platform:

| Feature                | Expected Behavior          | Result  |
| ---------------------- |:--------------------------:| -------:|
| Home Page Link         | Clicking the "Home" link redirects to the homepage displaying upcoming events.      | Pass |
| About Page Link        | Clicking the "About" link redirects to the About Us page with information about the platform.    | Pass |
| Contact Page Link      | Clicking the "Contact" link redirects to the Contact Us page with contact details.    | Pass |
| Register Button        | Clicking the "Register" button opens the registration form for a new user account. | Pass |
| Login Button           | Clicking the "Login" button opens the login form for existing users. | Pass |
| Logout Button          | Clicking the "Logout" button logs out the current user and redirects to the homepage. | Pass |
| Event Detail Page      | Clicking on an event redirects to the event's detail page displaying full details about the event. | Pass |
| Book Now Button        | Clicking the "Book Now" button allows the user to book tickets for the event (requires login). | Pass |
| My Bookings Link       | Clicking "My Bookings" shows a list of all events the user has booked. | Pass |
| Edit Booking           | Clicking "Edit" on a booking allows the user to change the number of tickets. | Pass |
| Cancel Booking         | Clicking "Cancel" on a booking deletes the booking after user confirmation. | Pass |
| Leave a Comment        | Logged-in users can submit a comment on an event's detail page. | Pass |
| Edit Comment           | Logged-in users can edit their own comments on an event's detail page. | Pass |
| Delete Comment         | Logged-in users can delete their own comments from an event's detail page. | Pass |
| Login Required Redirect | Attempting to book an event or leave a comment while not logged in redirects the user to the login page. | Pass |
| Error Messages         | Proper error messages are shown for invalid actions, like trying to book without selecting tickets or submitting an empty comment. | Pass |

### Automated Testing

In addition to manual testing, basic unit tests were written to ensure that core functionalities like user registration, event booking, and commenting work as expected.

### Validation

- **HTML Validation:** Passed through W3C HTML Validator with no significant errors.
- **CSS Validation:** Passed through W3C CSS Validator with no significant errors.
- **JavaScript Validation:** Validated using JSHint, with adjustments made to ensure compatibility with ES6.
- **Python Code Validation:** Passed PEP8 validation with no significant issues.

## Deployment
This project was deployed using Heroku.

- **Steps for deployment:**
  - Fork or clone this repository.
  - Create a new Heroku app.
  - Set the buildpacks to Python and NodeJS in the appropriate order.
  - Link the Heroku app to the repository.
  - Click on DEPLOY.

## Credits 
- **This project was developed entirely by me.**
- Special thanks to the Django documentation for guidance on setting up the application.
- Inspiration and ideas were gathered from various online tutorials and the Django documentation.
- Code Institute for the deployment terminal.

## Advice and Experience
This project involved setting up a comprehensive Django application with user authentication, event management, and a comment system. One of the challenges was ensuring the application was fully responsive and worked well on various devices.

## Acknowledgements
A special thanks to my mentor for their advice and guidance throughout the development of this project.
