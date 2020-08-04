# dog_park_pals
Group Project: Irina, Lydia and Michelle

Lydia: Group Project Proposal, HTML, Models, views.py, Google Maps API
Irina: Wireframe Design, Log-in/Registration, Models, views.py, Google Maps API
Michelle: Coordinate collaboration (Zoom, Github, Liveshare), HTML support, Models, views.py, Google Maps API

Dog Buddy - Dog Park Connections

Concept

Dog Buddy is a website that allows dog owners or dog sitters to find others, in the area, who are taking their dogs to a park, so their dogs can have a buddy to play with at the park. This is especially helpful when visiting a new location or if you want to network and get to know other dog owners. 


Minimum Viable Product

1)	Dog Buddy will have a welcome page (index.html, /index = GET) when you initially pull up the website. Register or Login will be the second page once you click get started on the welcome page (/register or /login = POST), once you login/register you will redirected to the Dashboard (dashboard.html, /dashboard = GET)
	
2)	The dashboard (dashboardl.html) which will feature a table that shows “Your Playdates” with all the upcoming playdates that you have created and others you have joined. From here you can Edit (edit.html, playdates/edit/id = GET) or Remove (playdates/delete/id) a playdate that you had planned (you were the “creator”). You can also click on the playdate itself (show_one.html, playdates/id = GET)  to look at the details of that one playdate which would include those who are going on the trip. 

Below will be another table showing “Other People’s Playdates” so you can join (/add) those, which were created by other users. You cannot Edit or Remove those playdates because you are not the “creator.”. Clicking on those park names will also allow you to look at the details of that one playdate (show_one.html, playdates/id = GET which could include those who are going on the trip.

3)	From the Dashboard, you can create a new playdate (new.html, playdates/new to render = GET), where you will add the dog park name, human, address, date, start time, end time, dog breed, gender, and comments (such as “I need to leave around 1:00pm”, or “I’ll bring snacks to share.” From this page you can either cancel or submit (playdates/new = POST).

4)	Once submitted, the new playdate is created,  and you will be directed back to the Dashboard (/dashboard = GET).

5)	There will also be a Log-out button (/logout) on each page that will redirect you to the welcome page (index.html) and a Dashboard button to take you back to the Dashboard.


6)	We will be styling this with bootstrap, preferably using a nice picture background of a dog park or dogs, and then have opaque boxes that include the dashboard information and single trip information. 


Product Backlog (cool, but not crucial - numbering relates to sequence above):

1a or 2a)	You can update your profile to include info on your dog, name, type, age. A user can click on your name and see info about you and your dog. 

7)	Option for users to add a review, or perhaps just comments, to a dog park show_one page.

8)	Google Maps API so user can click on the dog park location, see it’s location on the map and get directions.

9)	There will be a page that when you click on the user you can see that user’s information and perhaps with google maps find the general area where they live and what dog they own and the latest parks they’ve visited. Letting the user upload an image of their dog here would be really cool too!
