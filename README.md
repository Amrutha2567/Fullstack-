# Full Stack Problem Statement
Objective:
Build a solution to manage and display dish information, including creating a database, API, and
a front-end dashboard. The dashboard should allow toggling the published status of dishes and
show real-time updates.
Tasks:
1. Database Creation
- Design a database schema to store dishes with the following fields:
- `dishId` (unique identifier)
- `dishName` (string)
- `imageUrl` (string)
- `isPublished` (boolean)
- Populate the database with this json data.
2. API Development
- Create an API to fetch the list of dishes from the database.
- Create an API to toggle the `isPublished` status of a dish.
3. Front-End Dashboard
- Use a framework (e.g., React.js) to build a dashboard.
- Display all dishes with their information.
- Include a button to toggle the published status, updating both the UI and backend.
Bonus: Real-Time Updates
- Implement real-time updates so the dashboard reflects changes made directly in the backend.
For example, if a dish is unpublished on the backend directly(Not from your dashboard), then
your dashboard should react to the change.
Submission:
- Provide a 1-minute video demonstrating the app.
- Provide a 1-minute video explaining the code.
- Submit the code on GitHub or as a ZIP file.
