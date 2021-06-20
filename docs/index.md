# Userbank API Documentation

## Routes

- [GET /api/user](#get-apiuser)
- [POST /api/user](#post-apiuser)
- [GET /api/user/\<id\>](#get-apiuserid)
- [PUT /api/user/\<id\>](#put-apiuserid)
- [DELETE /api/user/\<id\>](#delete-apiuserid)

### GET /api/user

Retrieves IDs of all current users.

The request body may be left empty. The response if the database query
succeeds has status code 200 and an `application/json` body matching
the schema below:
```typescript
{
    users: number[]
}
```
In case of database error, the response has status code 500 and no body.

### POST /api/user

Creates a new user.

The request body must be a JSON string matching the schema below:
```typescript
{
    firstName: string,
    lastName: string,
    email: string,
    phoneNum: string
}
```
These fields are validated as follows:
- all fields must be defined, correct data type
- firstName and lastName must be at least one character long
- email must match the pattern a@b.c
- phoneNum must be between 11-13 characters
- phoneNum must contain only 0-9 and + characters

If the database record was successfully created, the response has status
code 200. Otherwise a status code of 400 is set for validation failure,
or 500 for database error.

### GET /api/user/\<id\>

Retrieves full record for a particular user.

The requested `<id>` must be a positive integer, indicating the ID of
the user record to retrieve. If all is well the response has status
code 200 and a JSON body matching the schema below:
```typescript
{
    id: number,
    firstName: string,
    lastName: string,
    email: string,
    phoneNum: string
}
```

If the `<id>` is not a positive integer the response has status code
400 and no body. If there was a database error, such as no user by that
ID exists, the status code is 500.

### PUT /api/user/\<id\>

Updates fields for a particular user.

The requested `<id>` must be a positive integer, indicating the ID of
the user record to update. The fields to update are given in a JSON body
matching the schema below:
```typescript
{
    firstName?: string,
    lastName?: string,
    email?: string,
    phoneNum?: string
}
```
Note that all fields are optional. However to pass validation at least
one field must be defined. All present fields are otherwise validated
against the same criteria as the [POST /api/user](#post-apiuser) route.

The response has a status code 200 if successful, even if a user by the
given ID did not exist. In case of validation failure (including `<id>`
not being a positive integer) a status code of 400 is set. In case of
database error the status code is 500.

### DELETE /api/user/\<id\>

Deletes a particular user.

The requested `<id>` must be a positive integer, indicating the ID of
the user record to delete. If the record was successfully removed the
response has status code 200.

If the `<id>` is not a positive integer the response has status code
400 and no body. If there was a database error, such as no user by that
ID exists, the status code is 500.
