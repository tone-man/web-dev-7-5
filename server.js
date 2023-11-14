const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const path = require('path');

const db = new sqlite3.Database('library.db');

const port = process.env.PORT || 5008;
const app = express();

app.use("/", express.static(__dirname));

app.get('/', (req, res) => {
    let options = {
        root: path.join(__dirname, "views")
    }

    res.sendFile("index.html", options, (err) => {
        if (err) {
            console.log(err);
        } else {
            console.log('Sent: index.html');
        }
    });
});

app.get('/books', (req, res) => {

    const sql = 'SELECT * FROM Books;';

    db.all(sql, (err, result) => {
        if(err) {
            throw err;
        }
        res.send(result);
    });
});

app.listen(port, function() {
    console.log('Listening on', port);
});


