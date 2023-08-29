# Zeroed
**Zeroed** is a website where anyone can write, share, and comment blogs. 

Table of contents:
* [Overview/main page](#overviewmain-page)
* ['About' page](#about-page)
* [Login and registration](#login-and-registration)
* [User/author profile](#userauthor-profile)
* [Blog page](#blog-page)
* [Writing a blog](#writing-a-blog)
* [Getting in touch](#getting-in-touch)

## Overview/main page
* The first page a user sees contains a list with all blogs. There is information about each blog: author, date, views, rating (number of likes), and content type(s). 
* The user can sort the list based on the available options and move through the pages of blogs. 
* The blog's title and author's username are clickable and will lead to the blog page and author profile, correspondingly.

https://github.com/nikalinov/zeroed/assets/92603661/e6db3080-917a-4901-9239-f79d5638c45e

## 'About' page
* This page briefly explains the purpose of the website.

![Screenshot of 'About' page](https://github.com/nikalinov/zeroed/assets/92603661/22fa7d9a-903b-49f5-9278-5b0f3099e440)

## Login and registration
* To register, one should fill all the necessary fields. The password's length must be at least 8 characters and include 1 lowercase, 1 uppercase, 1 number, and 1 symbol.
* After that, the account must be activated by following the link which is sent to the email from the registration form.
* Using the activated account credentials, a new user can log in with their email and password.
* If a user forgets the password, they can reset it using the 'Forgot your password?' link on the login page.

https://github.com/nikalinov/zeroed/assets/92603661/1ca504b6-9481-4043-9b22-93932011b51a

## User/author profile
* A profile consists of some user data (username, full name, social networks, etc.) and blogs if the user has written them.
* The blogs can be sorted in the same way as on [the main page](#overviewmain-page).
* If a user is viewing their own profile, they can edit it: change any visible fields or the profile picture.

https://github.com/nikalinov/zeroed/assets/92603661/26aefb4c-3c15-4f5c-800b-f96fee78d889

## Blog page
* A user can find links to blogs either on the main page or a user's page (see [User/author profile](#userauthor-profile) part).
* There is custom background, title, and blog data (author, likes, and views) at the header section.
* Blog body can contain both text and media (images, videos, etc.) content.
* At the bottom, there is comment section, where logged-in users can leave their comments about the blog.

https://github.com/nikalinov/zeroed/assets/92603661/13b2d8a5-ab16-4e2f-ac5c-cd90699ad647

## Writing a blog
* 'Write' link in the navigation bar redirects to the writing page.
* A user should set a title, language, content type(s), and background image (optional, the default is a light monotone background).
* In the editor, the text can be stylized within the available range of formatting options (setting headings, bold/italic text, font size/color, etc.)
* If a writer wishes, they can upload media in the blog body.
* After publishing, there is an option to delete the blog.

https://github.com/nikalinov/zeroed/assets/92603661/3720d2c0-09c0-4b66-9102-8369171320ed

## Getting in touch
* If a user has a query, they can follow the 'Contact' link in the navigation bar (the user must be logged in)
* After filling in the subject and message, the email will be sent to the website support's mailbox.

https://github.com/nikalinov/zeroed/assets/92603661/63ac35c1-0db3-4956-a110-9a2b9597d552

## Technologies used
* [Python 3](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com/)
* HTML, CSS
* [Amazon Simple Email Service (SES)](https://aws.amazon.com/ses/)
* [Quill editor](https://quilljs.com/)
* Javascript (minor usage)
