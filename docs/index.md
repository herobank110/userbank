# Userbank API Documentation

## Routes

- [GET /api/user](#get-apiuser)
- [POST /api/user](#post-apiuser)
- [GET /api/user/\<id\>](#get-apiuserid)
- [UPDATE /api/user/\<id\>](#update-apiuserid)
- [DELETE /api/user/\<id\>](#delete-apiuserid)

### GET /api/user

Retrieves IDs of all current users.

The request body may be left empty. The response if the database query
succeeds is has status code 200 and an `application/json` body matching
the schema below:
```typescript
{
    /** Array of user IDs. */
    result: number[]
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

If validation passed and a database record was successfully created, the
response has status code 200. Otherwise a status code of 400 is set for
validation failure, and 500 is set for database insertion error.
