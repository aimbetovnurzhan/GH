require("dotenv").config();
const express = require("express");
const bodyParser = require("body-parser");
const apicache = require("apicache");
const v1WorkoutRouter = require("./v1/routes/workoutRoutes");
const { swaggerDocs: V1SwaggerDocs } = require("./v1/swagger");
const connectDB = require("./database/mongo");

const app = express();
const cache = apicache.middleware;
const PORT = process.env.PORT || 3000;

app.get("/", (req,res) => {
    res.send(`<h2>It's working!</h2>`);
});


app.use(bodyParser.json());
app.use(cache("2 minutes"));
app.use("/api/v1/workouts", v1WorkoutRouter);

//console.log("MONGO_URI =", process.env.MONGO_URI);
connectDB().then(() => {
  app.listen(PORT, () => {
    console.log(`API is listening on port ${PORT}`);
    V1SwaggerDocs(app, PORT);
  });
});