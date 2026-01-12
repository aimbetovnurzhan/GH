const Record = require("../models/Record");

const getRecordForWorkout = async (workoutId) => {
  try {
    const records = await Record.find({ workout: workoutId });

    if (!records || records.length === 0) {
      throw {
        status: 400,
        message: `Can't find records for workout with id '${workoutId}'`,
      };
    }

    return records;
  } catch (error) {
    throw { status: error?.status || 500, message: error?.message || error };
  }
};

module.exports = { getRecordForWorkout };