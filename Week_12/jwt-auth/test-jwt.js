const jwt = require('jsonwebtoken');

// Creating a token (using the jwt.sign() method)
const myToken = jwt.sign({
    userid: 123,
    email: 'johndoe@gmail.com',
    username: 'johnhasgone'
    },
    // Secret (must be a string even if numbers)
    "123456",
    // Expire time
    {expiresIn: "1d"}
)

console.log(myToken)

const expiredToken = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyaWQiOjEyMywiZW1haWwiOiJqb2huZG9lQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoiam9obmhhc2dvbmUiLCJpYXQiOjE3MzY3NTU2MzMsImV4cCI6MTczNjg0MjAzM30.WFGwi-962jbyIMhQm8DDHclRAI9Z_S9qQk_Lt0uZ72s"

// Verifying a token (using the jwt.verify() method)
jwt.verify(
    // token
    expiredToken,
    // token-secret-code
    "123456",
    // error or decoded
    (err, decode) => {
        if (err) {
            console.log(err.message)
            return;
        }
        console.log(decode)
    }
)