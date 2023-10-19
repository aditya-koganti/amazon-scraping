const express = require("express");
const app           = express();
const bodyParser = require("body-parser");

// ======= Basic Configuration ======= //

app.use(bodyParser.urlencoded({
    extended: true
}))
app.use(express.static("public"))
app.set("view engine", "ejs")


// ======== Routes ========= //

app.get("/", function(req, res){
    res.render("home")
})

app.post("/scrape", (req, res) => {
    var link = req.body.link
})


// ======== Deploying ========= //
app.listen(3000,function(){
    console.log("listening on https://localhost:3000")
})