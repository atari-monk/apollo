# Endpoints

- VSCode extention `REST Client by publisher:"Huachao Mao".
- It has big manual.

- api_requests.http

```plaintext
# GET all notes
GET http://localhost:3000/api/notes

# POST a new note
POST http://localhost:3000/api/notes
Content-Type: application/json

{
    "title": "New Note",
    "content": "This is the content of the new note."
}

# GET a single note by ID
GET http://localhost:3000/api/notes/1

# PUT to update a note by ID
PUT http://localhost:3000/api/notes/1
Content-Type: application/json

{
    "title": "Updated Note",
    "content": "This is the updated content of the note."
}

# DELETE a note by ID
DELETE http://localhost:3000/api/notes/1
```
