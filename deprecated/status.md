# Status Codes and Error Responses

In case of an error or a successful response, the response header
contains a HTTP code (see <https://tools.ietf.org/html/rfc7231>). The
response body usually contains the following:

- The HTTP response code;

- An accompanying message for the HTTP response code; and

- A field or object where the error occurred.

Table 1: HTTP Response Codes

  HTTP Response    Operation             Description
  ---------------- ---------------------- ------------------------------------------------------------------
  200 Ok           GET, PUT, DELETE       No error, operation successful.
  201 Created      POST                   Successful creation of a resource.
  204 No Content   GET, PUT, DELETE       Successful but no content.
  400 Bad Request  GET, POST, PUT, DELETE The request could not be understood.
  401 Unauthorized GET, POST, PUT, DELETE User must authorize.
  403 Forbidden    GET, POST, PUT, DELETE The request has been refused due to authorization failure.
  404 Not Found    GET, POST, PUT, DELETE The requested resource could not be found.
  405 Not Allowed  GET, POST, PUT, DELETE The method is not allowed on the resource.
  500 Server Error GET, POST PUT          Internal Server error.

