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

