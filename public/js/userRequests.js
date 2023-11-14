async function getBooks() {
    const response = await fetch('http://localhost:5008/books');
    const books = await response.json();
    return books;
}

async function onLoad() {
    let table = document.getElementById("body-book-data");
    let books = await getBooks();

    books.forEach(book => {
        table.innerHTML += createTableRow(book.title, book.author, book.genres);
    });
}

function createTableRow(title = "N/A", author = "N/A", genres = "N/A") {
    // Create a table row
    var row = "<tr>";

    // Add table data cells with the provided values
    row += "<td>" + title + "</td>";
    row += "<td>" + author + "</td>";
    row += "<td>" + genres + "</td>";

    // Close the table row
    row += "</tr>";

    // Return the constructed table row
    return row;
}

// Add the event listener
window.addEventListener("load", onLoad);
