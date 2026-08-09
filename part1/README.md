HBnB Evolution — Part 1 Technical Documentation
0) High-Level Package Diagram (Architecture)
High-Level Package Diagram

Explanation

Presentation Layer: API/controllers handle requests/responses and call the facade.
Business Logic Layer: entities + rules; exposes use cases through the facade.
Persistence Layer: repositories/database operations (DB details in Part 3).
Facade pattern: single entry point between Presentation and Business Logic.
1) Detailed Class Diagram — Business Logic Layer
Business Logic Class Diagram

Explanation

All entities include: id (UUID4), created_at, updated_at.
User 1 → * Place (a user can own many places).
Place 1 → * Review (a place can have many reviews).
Place * ↔ * Amenity (many-to-many association).
2) Sequence Diagrams (API Calls)
2.1 User Registration (POST /users)
User Registration Sequence

Flow (summary)

Client sends registration data to API.
API calls facade register_user.
Facade validates and asks repository to save user.
API returns 201 Created.
2.2 Place Creation (POST /places)
Place Creation Sequence

Flow (summary)

Client sends place data to API.
API calls facade create_place.
Facade validates owner + data, persists place.
API returns 201 Created.
2.3 Review Submission (POST /places/{place_id}/reviews)
Review Submission Sequence

Flow (summary)

Client submits rating/comment.
API calls facade create_review.
Facade validates user/place + rating, persists review.
API returns 201 Created.
2.4 Fetch Places List (GET /places)
List Places Sequence

Flow (summary)

Client requests places list (optional filters).
API calls facade list_places.
Facade asks repository for places.
API returns 200 OK with list.