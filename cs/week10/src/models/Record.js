const mongoose = require("mongoose");

const RecordSchema = new mongoose.Schema({
  id: { type: String, required: true },
  workout: { type: String, required: true },
  record: { type: String, required: true },
  member: { type: String }
});

module.exports = mongoose.model("Record", RecordSchema);
