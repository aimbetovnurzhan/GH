const mongoose = require("mongoose");

const WorkoutSchema = new mongoose.Schema({
  id: { type: String, required: true },
  name: String,
  mode: String,
  equipment: [String],
  exercises: [String],
  createdAt: String,
  updatedAt: String,
  trainerTips: [String],
});

module.exports = mongoose.model("Workout", WorkoutSchema);