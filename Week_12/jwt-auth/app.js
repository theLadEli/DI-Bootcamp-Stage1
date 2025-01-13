const express = require('express');
const cookieParser = require('cookie-parser');
const cors = require('cors');

const {db} = require('./config/db');

const app = express();

// Middleware
app.use(express.json());
app.use(cookieParser());
app.use(cors({
        credentials: true,
        // You can also limit where the requests come from
        // origin: ['http://localhost:3000']
    })
);

const {PORT} = process.env;

app.listen(PORT || 5001, () => {
    console.log(`Server is running on port ${PORT || 5001}`);
});

async function testConnection() {
    try {
        const response = await db.raw('select version()')
        console.log(response.rows);
    } catch (error) {
        console.error(error.message);
    }
}

testConnection();