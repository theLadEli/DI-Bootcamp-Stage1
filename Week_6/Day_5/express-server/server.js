const express = require('express');
const cors = require ('cors');
const {products} = require('./config/data.js')

// console.log(products)

const app = express();
app.use(cors());

// Uses '__dirname' so always knows exactly the directory the servers located
app.use('/', express.static(__dirname+'/public'))

const port = 3003;

const users = [
    {name:'Eli',email:'eli@gmail.com'},
    {name:'Henry',email:'henry@gmail.com'},
    {name:'Natan',email:'natan@gmail.com'},
    {name:'Matan',email:'matan@gmail.com'},
    {name:'Emma',email:'emma@gmail.com'}
]

app.listen(port, () => {
    console.log(`Run on port ${port}`)
})

app.get('/', (req, res) => {
    // Can use html inside the send()
    res.send(`<h1>Hello from my express server.</h1>`)
})

app.get('/users', (req, res) => {
    // If you're sending json, altho you can use send(), better to send as res.json() - faster.
    res.json(users)
})

// ----- PRODUCTS -----

app.get('/api/products', (req,res) => {
    res.json(products)
})

// below accepts requests like this "localhost:3003/api/products/101" where you can call url with params
app.get('/api/products/:id', (req,res) => {
    console.log(req.params)
    const {id} = req.params
    const myProduct = products.find(item => item.id == id)
    // if product does not exist, you can send 404 status
    if(!myProduct) return res.sendStatus(404)
    res.json(myProduct)
})

app.get('/api/search', (req, res) => {
    console.log(req.query)
    const {name} = req.query
    console.log(name)
    const filtered = products.filter(item => {
        return item.name.toLowerCase().includes(name.toLowerCase())
    })

    if (filtered.length == 0) return res.status(404).json({message:'No products matched your search'})
    res.send(filtered)
})