

# Status Codes and Error Responses

In case of an error or a successful response, the response header
contains a HTTP code (see <https://tools.ietf.org/html/rfc7231>). The
response body usually contains the following:

- The HTTP response code;

- An accompanying message for the HTTP response code; and

- A field or object where the error occurred.

Table 1: HTTP Response Codes

  HTTP Response  Description Code
  -------------- -------------------------------------------------------------------------------------------------
  200            *OK* success code, for GET or HEAD request.
  201            *Created*    success code, for POST request.
  204            *No Content* success code, for DELETE request.
  300            The value returned when an external ID exists in more than one record.
  304            The request content has not changed since a specified date and time.
  400            The request could not be understood.
  401            The session ID or OAuth token used has expired or is invalid.
  403            The request has been refused.
  404            The requested resource could not be found.
  405            The method specified in the Request-Line isn't allowed for the resource specified in the URI.
  415            The entity in the request is in a format that's not supported by the specified method.


