## Profile

| Property | Type | Description |
| --- | --- | ------------- |
| uuid | string | a unique id for the profile |
| username | string | the username associated with the profile |
| group | string | a group this profile may be associated to |
| resource | string | a resource this profile may belong to |
| context | string | a context the profile may belong to |
| description | string | a description for this profile |
| firstname | string | the firstanme of the profile user |
| lastname | string | the lastname of the profile user |
| publickey | string | the lastname of the profile user |
| email | string | the email of the profile user |


## Paths

### /cloudmesh/profile/profiles

#### GET /cloudmesh/profile/profiles

##### Description

Returns all profiles

##### Responses

| Code | Description | Schema |
| --- | --- | ------------- |
| 200 | profile information | [Profile](#profile) |

##### PARAMETERS

#### PUT /cloudmesh/profile/profiles

##### Description

ERROR: missing

##### Responses

| Code | Description | Schema |
| --- | --- | ------------- |
| 201 | Created | |

##### PARAMETERS

| Name | Located in | Description | Required | Schema |
| --- | --- | ------------- | --- | --- |
| profile | body | The new profile to create | False | [](#) | |

### /cloudmesh/profile/profiles/{uuid}

#### GET /cloudmesh/profile/profiles/{uuid}

##### Description

Returns a the profile of a user

##### Responses

| Code | Description | Schema |
| --- | --- | ------------- |
| 200 | profile information | [Profile](#profile) |

##### PARAMETERS

| Name | Located in | Description | Required | Schema |
| --- | --- | ------------- | --- | --- |
| uuid | path | ERROR: missing | True | |

