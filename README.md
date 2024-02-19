BEHAVIOUR OF EACH FUNCTION

  # Tank API


## Endpoints

### 1. Get all tanks

- **HTTP Method:** GET
- **Endpoint:** `/tank`
- **Description:** Retrieves the list of all tanks.

### 2. Get tank by ID

- **HTTP Method:** GET
- **Endpoint:** `/tank/{id}`
- **Description:** Retrieves a specific tank by its ID.
- **Error Handling:** Raises an HTTP 404 error if the tank is not found.

### 3. Add a new tank

- **HTTP Method:** POST
- **Endpoint:** `/tank`
- **Description:** Adds a new tank to the list of tanks.
- **Request Body:** JSON object representing the new tank.
- **Success Response:** Returns the created tank with a status code of 201.

### 4. Update a tank

- **HTTP Method:** PATCH
- **Endpoint:** `/tank/{id}`
- **Description:** Updates an existing tank by its ID.
- **Request Body:** JSON object representing the updated tank fields.
- **Success Response:** Returns the updated tank with a status code of 200.
- **Error Handling:** Raises an HTTP 404 error if the tank is not found.

### 5. Delete a tank

- **HTTP Method:** DELETE
- **Endpoint:** `/tank/{id}`
- **Description:** Deletes a specific tank by its ID.
- **Success Response:** Returns an empty response with a status code of 200.
- **Error Handling:** Raises an HTTP 404 error if the tank is not found.

  

REASON FOR WRITING CODE

  This code was written for the ECSE3038 Lab #3, to get accustomed to the technologies used in designing and implementing a RESTful API server.
  

TWO TRUTHS AND A LIE
  1. I can play 3 different kinds of instruments.
  2. I have broken the same arm twice.
  3. I love seafood.